import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;

public class PedigreeYieldPredictor {
    
    boolean submit = true;
    boolean format = true;
    int luckynum = 1001;
    
    class Entry{
        int exp;
        int loc;
        int repno;
        int var;
        double yield;
        int year;
        int rep;
    }
    
    class Query{
        int loc;
        int year;
        int rep;
        int[] var = new int[36];
        double[] real = new double[36];
    }
    
    class Stat{
        int[] rep;
        int[] loc;
        int[] var;
    }
    Stat stat = null;
    
    Entry[] train = null;
    Query[] test = null;
    
    double[] bias_rep = null;
    double[] bias_loc = null;
    double[] bias_var = null;
    double[] bias_vary = null;
    double[] bias_year = null;
    
    double[][] m_rep = null;
    double[][] m_loc = null;
    double[][] m_var = null;
    double[][] m_vary = null;
    
    int T = 20;
    int round = 100;
    
    double gamma = 1E-2;
    double lambda_rep = 0.1;
    double lambda_var = 0.7;
    double sigma_real = 0.1;
    double sigma_pred = 0.2;
    
    //tool
    int repnum, varnum, locnum, trainnum, quenum;
    
    HashMap<Integer,Integer> repID = null;
    HashMap<Integer,Integer> locID = null;
    HashMap<String,Integer> varID = null;
    
    HashMap<Integer,String> pedigree = null;
    
    Random random = new Random(luckynum);
    
    private String[] trainingData;
    private String[] droughtMonitor;
    private String[] droughtNOAA;
    private String[] locations;
    private String[] material;
    private String[] reps;

    public String[] predictYield(String[] trainingData,
            String[] droughtMonitor, String[] droughtNOAA, String[] locations,
            String[] material, String[] reps) {
        try{
            this.trainingData = trainingData;
            this.droughtMonitor = droughtMonitor;
            this.droughtNOAA = droughtNOAA;
            this.locations = locations;
            this.material = material;
            this.reps = reps;
            
            repnum = 0;//locations.length;
            locnum = 0;
            varnum = 0;//varieties.length;
            trainnum = trainingData.length;
            quenum = reps.length;
            
            repID = new HashMap<Integer,Integer>();
            locID = new HashMap<Integer,Integer>();
            varID = new HashMap<String,Integer>();
            
            pedigree = new HashMap<Integer,String>();
            
            for (int i=0;i<material.length;i++){
                String[] label =material[i].split(",");
                pedigree.put(Integer.parseInt(label[0]),label[1]);
                
            }
            
            HashSet<String> testVar = new HashSet<String>();
            HashSet<Integer> testLoc = new HashSet<Integer>();
            for (int i=0;i<quenum;i++){
                String[] label;
                label = reps[i].split(",");
                for (int c=0;c<36;c++){
                    if (!format) {
                        int var = Integer.parseInt(label[c+2]);
                        testVar.add(pedigree.get(var));
                    }
                    else testVar.add(label[c+2]);
                }
                testLoc.add(Integer.parseInt(label[0]));
            }
            
            
            train = new Entry[trainnum];
            test = new Query[quenum];
            
            for (int i=0;i<trainnum;i++){
                if (i%100000==0) System.out.println("doing trainnum "+i);
                String[] label;
                label = trainingData[i].split(",");
                
                int expid = Integer.parseInt(label[0]);
                
                int loc = -1;
                if (!label[1].equals("NULL")){
                    loc = Integer.parseInt(label[1]);
                    //if (!testLoc.contains(loc))  continue;
                    Integer iloc = locID.get(loc);
                    if (iloc==null) {
                        locID.put(loc, locnum);
                        locnum++;
                        iloc = locID.get(loc);
                    }
                    loc = iloc;
                }
                
                int repidno = Integer.parseInt(label[2]);
                
                int var =-1;
                if (!label[3].equals("NULL")){
                    var = Integer.parseInt(label[3]);
                    //if (!testVar.contains(pedigree.get(var)))  continue;
                    Integer ivar = varID.get(pedigree.get(var));
                    if (ivar==null) {
                        varID.put(pedigree.get(var), varnum);
                        varnum++;
                        ivar = varID.get(pedigree.get(var));
                    }
                    var = ivar;
                }
                
                double yield = Double.parseDouble(label[4]);
                
                String[] data;
                int year=-1;
                if (!label[6].equals("NULL")){
                    data = label[6].split("-|/");
                    year = Integer.parseInt(data[0])-1990;
                    if (year<0) year = 0;
                    if (year>29) year = 29;
                }
                
                
                if (loc>=0 && year>=0 && var>=0){
                    int rep = loc*30+year;
                    Integer irep = repID.get(rep);
                    if (irep==null) {
                        repID.put(rep, repnum);
                        repnum++;
                        irep = repID.get(rep);
                    }
                    rep = irep;
                    
                    
                    train[i] = new Entry();
                    Entry t = train[i];
                                
                    t.exp = expid;
                    t.repno = repidno;
                    t.loc = loc;
                    t.var = var;
                    t.yield = yield;
                    t.year = year;
                    t.rep = irep;
                }
            }
            
          //init queries
            for (int i=0;i<quenum;i++){
                if (i%100==0) System.out.println("doing query "+i);
                String[] label;
                label = reps[i].split(",");
                
                int loc = -1;
                if (!label[0].equals("NULL")){
                    loc = Integer.parseInt(label[0]);
                    Integer iloc = locID.get(loc);
                    if (iloc==null) {
                        locID.put(loc, locnum);
                        locnum++;
                        iloc = locID.get(loc);
                    }
                    loc = iloc;
                }
                
                String[] data;
                int year=-1;
                if (!label[1].equals("NULL")){
                    data = label[1].split("-|/");
                    year = Integer.parseInt(data[0])-1990;
                    if (year<0) year = 0;
                    if (year>29) year = 29;
                }
                
                int rep = loc*30+year;
                Integer irep = repID.get(rep);
                if (irep==null) {
                    repID.put(rep, repnum);
                    repnum++;
                    irep = repID.get(rep);
                }
                rep = irep;
                
                test[i] = new Query();
                Query t = test[i];
                t.loc = loc;
                t.year = year;
                t.rep = rep;
                for (int v=0;v<36;v++){
                    int var =-1;
                    String vars;
                    if (!format) vars = pedigree.get(Integer.parseInt(label[v+2]));
                    else vars = label[v+2];
                    Integer ivar = varID.get(vars);
                    if (ivar==null) {
                        varID.put(vars, varnum);
                        varnum++;
                        ivar = varID.get(vars);
                    }
                    var = ivar;
                    
                    t.var[v] = var;
                    
                    if (!submit) t.real[v] = Double.parseDouble(label[v+38]);
                }
                
            }
            
            System.out.println("repnum: "+repnum+" locnum: "+locnum+" varnum: "+varnum);
            
            stat = new Stat();
            stat.rep = new int[repnum];
            stat.loc = new int[locnum];
            stat.var = new int[varnum];
            
            int new_trainnum = 0;
            for (int i=0;i<trainnum;i++)
                if (train[i]!=null) {
                    new_trainnum++;
                    stat.rep[train[i].rep]++;
                    stat.loc[train[i].loc]++;
                    stat.var[train[i].var]++;
                }
            Entry[] new_train = new Entry[new_trainnum];
            int tt=0;
            for (int i=0;i<trainnum;i++)
                if (train[i]!=null){
                    new_train[tt] = train[i];
                    tt++;
                }
            train = new_train;
            trainnum = new_trainnum;
            
                        
            bias_rep = new double[repnum];
            bias_loc = new double[locnum];
            bias_var = new double[varnum];
            bias_vary = new double[varnum*30];
            bias_year = new double[30];
            
            
            m_rep = new double[repnum][T];
            m_loc = new double[locnum][T];
            m_var = new double[varnum][T];
            m_vary = new double[varnum*30][T];
            
            for (int i=0;i<repnum;i++)
                for (int k=0;k<T;k++)
                    m_rep[i][k] = (random.nextDouble()-0.5)/T;
            for (int i=0;i<locnum;i++)
                for (int k=0;k<T;k++)
                    m_loc[i][k] = (random.nextDouble()-0.5)/T;
            for (int i=0;i<varnum;i++)
                for (int k=0;k<T;k++)
                    m_var[i][k] = (random.nextDouble()-0.5)/T;
            for (int i=0;i<varnum*30;i++)
                for (int k=0;k<T;k++)
                    m_vary[i][k] = (random.nextDouble()-0.5)/T;
            
            
            for (int ir=0;ir<round;ir++){
                int all=0,right=0;
                if (ir%1==0) System.out.print("ir: "+ir);
                shuffle();
                for (int i=0;i<trainnum-1;i++){
                        
                    Entry x = train[i];
                    Entry y = train[i+1];
                    
                    if (x.rep!=y.rep || Math.abs(x.yield-y.yield)<5) continue;
                    
                    all++;    
                    double real_x = x.yield;
                    double real_y = y.yield;
                    double pred_x = predicte(x.rep,x.loc,x.year,x.var);
                    double pred_y = predicte(y.rep,y.loc,y.year,y.var);
                    if ((real_x-real_y)*(pred_x-pred_y)>=0) right++;
                    
                    double p_xy = 1.0/(1+Math.exp(-1*sigma_real*(real_x-real_y)));
                    double p_xy_p = 1.0/(1+Math.exp(-1*sigma_pred*(pred_x-pred_y)));
                    double delta = (p_xy - p_xy_p) * p_xy_p * (1 - p_xy_p);
                        //sigma_pred*((1-p_xy) - 1.0/(1+Math.exp(-1*sigma_pred*(pred_x-pred_y))));
                    
                    
                    bias_rep[x.rep] += gamma*delta;
                    bias_rep[y.rep] -= gamma*delta;
                    
                    bias_loc[x.loc] += gamma*delta;
                    bias_loc[y.loc] -= gamma*delta;
                    
                    bias_var[x.var] += gamma*delta;
                    bias_var[y.var] -= gamma*delta;
                    
                    bias_vary[x.var*30+x.year] += gamma*delta;
                    bias_vary[y.var*30+y.year] -= gamma*delta;
                    
                    bias_year[x.year] += gamma*delta;
                    bias_year[y.year] -= gamma*delta;
                    
                    for (int k=0;k<T;k++){
                        double p_x = m_rep[x.rep][k]+m_loc[x.loc][k];
                        double q_x = m_var[x.var][k]+m_vary[x.var*30+x.year][k];
                        double p_y = m_rep[y.rep][k]+m_loc[y.loc][k];
                        double q_y = m_var[y.var][k]+m_vary[y.var*30+y.year][k];
                        
                        m_rep[x.rep][k] += gamma*(delta*q_x - lambda_rep*m_rep[x.rep][k]);
                        m_rep[y.rep][k] -= gamma*(delta*q_y + lambda_rep*m_rep[y.rep][k]);
                        
                        m_loc[x.loc][k] += gamma*(delta*q_x - lambda_rep*m_loc[x.loc][k]);
                        m_loc[y.loc][k] -= gamma*(delta*q_y + lambda_rep*m_loc[y.loc][k]);
                        
                        m_var[x.var][k] += gamma*(delta*p_x - lambda_var*m_var[x.var][k]);
                        m_var[y.var][k] -= gamma*(delta*p_y + lambda_var*m_var[y.var][k]);
                        
                        m_vary[x.var*30+x.year][k] += gamma*(delta*p_x - lambda_var*m_vary[x.var*30+x.year][k]);
                        m_vary[y.var*30+y.year][k] -= gamma*(delta*p_y + lambda_var*m_vary[y.var*30+y.year][k]);
                    
                    }
                }
                System.out.print(" right/all on train: "+(right+0.0)/all);
                if (!submit) evaluate();
                else System.out.println();
                
            }
            
            String[] results = new String[quenum];
            for (int i=0;i<quenum;i++){
                 Query t = test[i];
                 int rep = t.rep;
                 int loc = t.loc;
                 int year = t.year;
                 double[] r = new double[36];
                 String s = "";
                 for (int c=0;c<36;c++){
                     int var = t.var[c];
                     r[c] = predicte(rep,loc,year,var);
                 }
                 for (int c=0;c<36;c++){
                     int count=1;
                     for (int cc=0;cc<36;cc++)
                         if (r[cc]<r[c]) count++;
                     s += count;
                     if (c!=35) s +=",";
                 }
                 results[i] = s;
                 if (i==0) System.out.println(s);
                
            }
            
            return results;
        }catch(Exception e){
            e.printStackTrace();
            return null;
        }
    }

    private void evaluate() {
        // TODO Auto-generated method stub
        double score = 0;
        for (int c=0;c<quenum;c++){
            Query t = test[c];
            double q=0;
            for (int i=0;i<36;i++)
                for (int j=i+1;j<36;j++){
                    double c_real = comp(t.real[i],t.real[j]);
                    double c_pred = comp(predicte(t.rep, t.loc, t.year,t.var[i]),predicte(t.rep, t.loc, t.year,t.var[j]));
                    if (c_real==0.5 || c_pred==0.5) q += 0.5;
                    else q += 1.0 - Math.abs(c_real - c_pred);
                }
            q =2*q/(35*36);
            score +=q;
        }
        score /= quenum;
        System.out.println(" SCORE: "+(1000000.0*score));
    }
    
    static double comp(double a,double b){
        if (a<b) return 0;
        if (a>b) return 1;
        return 0.5;
    }

    private double predicte(int rep, int loc, int year, int var) {
        double pred = bias_rep[rep] + bias_loc[loc] + bias_year[year]+ bias_var[var]+bias_vary[var*30+year];
        for (int k=0;k<T;k++)
            pred += (m_rep[rep][k]+m_loc[loc][k])*(m_var[var][k]+m_vary[var*30+year][k]);
         return pred;
    }

    void shuffle(){
        for (int i=0;i<trainnum;i++){
            int x = Math.abs(random.nextInt())%trainnum;
            int y = (x + Math.abs(random.nextInt())%20)%trainnum;
            if (train[x].rep == train[y].rep){
                Entry temp = train[x];
                train[x] = train[y];
                train[y] = temp;
            }
        }
    }

}
