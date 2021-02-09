
#include <omp.h>

void BuildTrnSys(TSys &ASys) {

  ASys.Clear();

  SetupVarPreds();

  vector<TDatRec*> pnts(Trn.size());
  for(unsigned int i = 0; i < Trn.size(); ++i)
    pnts[i] = &Trn[i];

  int maxreps, maxvars;
  int expcnt = SelectDatRecs(pnts, maxreps, maxvars);

  SetupLocPreds(pnts);

  unsigned int nextexp = 0;
  #pragma omp parallel
  {
    TSys sys(SYS_TERM_CNT);
    TBuffer2D<double> buf;
    buf.SetSize(maxreps, maxvars);
    TImpute_B imp;
    imp.Init(maxvars, maxreps, maxreps);
    for(unsigned int i = 1, f = 0; i <= pnts.size(); ++i) {
      if((i != pnts.size()) && (pnts[i]->id == pnts[i-1]->id))
        continue;
      #pragma omp critical
      {
        if(nextexp <= f)
          nextexp = i;
        else
          f = i;
      }
      if(f >= i)
        continue;

//      if(f % 10 > 2) {
//      if(f % 10 != 0) {
//        f = i;
//        continue;
//      }

      buf.Resize(pnts[f]->exp_repc, pnts[f]->exp_varc);
      buf.InitData(NaNDouble.d);
      for(unsigned int j = f; j < i; ++j)
        buf.Row(pnts[j]->exp_rep)[pnts[j]->exp_var] = pnts[j]->yield;

      while(f < i) {
        TDatRec* pnt = pnts[f++];
        if(!IsFinite(pnt->yield))
          continue;
        
        double *pv = &(buf.Row(pnt->exp_rep)[pnt->exp_var]);
        *pv = NaNDouble.d;

        imp.MakePredictions(pnt->exp_var, pnt->exp_rep, buf);
        pnt->exp_preds[0] = imp.PredDM;
        pnt->exp_preds[1] = imp.PredCDM;
        pnt->exp_preds[2] = imp.PredB;
        pnt->exp_preds[3] = imp.PredCB;
        pnt->exp_preds[4] = imp.PredWB;
        if(EXP_PRED_CNT > 5) {
          pnt->exp_preds[5] = imp.PredB1;
          pnt->exp_preds[6] = imp.PredCB1;
          pnt->exp_preds[7] = imp.PredWB1;
        }

        *pv = pnt->yield;

        if(pnt->GetSysTerms(sys.terms))
          sys.AddEquation(sys.terms, pnt->yield, QdtRecWeights[pnt->qdt_type]);
      }
    }
    #pragma omp critical
    {
      ASys.AddSys(sys);
    }
  }

#ifdef PRINT_INFO
  int n = (int)pnts.size();
  fprintf(stderr, "trn build %d points %d equations processed\n", n, ASys.eqcnt);
#ifdef PRINT_TRAIN_INFO
  ASys.Solve(ASys.loads);
  double err = 0.0;
  double errc = 0.0;
  int errcnt = 0;
  for(int ti = 0; ti < n; ++ti)
    if((IsFinite(pnts[ti]->yield)) && (pnts[ti]->GetSysTerms(ASys.terms))) {
      double e = 0.0;
      for(int k = 0; k < SYS_TERM_CNT; ++k)
        e += ASys.terms[k]*ASys.loads[k];
      e = Sqr(e-pnts[ti]->yield);
      err += e;
      errc += min(CAP_VAL2, e);
      errcnt++;
    }
  if(errcnt > 0) {
    err = sqrt(err/errcnt);
    errc = sqrt(errc/errcnt);
  }
  fprintf(stderr, "trn build terms %d residual: sup %d/%d err %g/%g (%g)\n", 
    int(SYS_TERM_CNT), errcnt, n, err, errc, 1e6/max(1e-6,errc));
#endif
  fflush(stderr);
#endif

}
