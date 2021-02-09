//#define HOME

using System;
using System.Collections.Generic;
using System.Text;
using System.Globalization;
using System.Diagnostics;
using System.Threading;



/*
Current solution:
Equally weights two predictors : 
- kNN vote - (1 vote = neighbour value + mean drift based on other locid / repnos) weighted by power 2 of sum of absolute differences between neighbour and target. Overweight for the same Locid
- relativePerf vote - average perf of the target / (average perf of others on all other locid / repnos) * average perf on target locid / repno
TODO : 
- Overweight for relativePerf vote (for same loccid first)
- For kNN vote - weight by stdev of differences, rather than by differences itself (or a mix of both ?)
- Take into account locid similarity (?)
- Try the matrix of (loccd/repno, matId) decomposition test (as done in previous contests)
*/

public class OmnipotentYieldPredictor
{
    static int CompareDouble(KeyValuePair<string, double> a, KeyValuePair<string, double> b)
    {
        if (a.Value >= b.Value)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }

    public class Location
    {
        public int LOCCD = 1;
        public double latitude = 100;
        public double longitude = 100;
        public String countyName = "Malopolska";
        public int maturityZone = 1;
        public int maturitySubZone = 0;
        public int maturityBand = 0;
        public int stateCode = 1;
        public int climateDivision = 1;
        public int fipsCode = 1;

        public Location(String data)
        {
            String[] temp = data.Split(',');
            int.TryParse(temp[0], out LOCCD);
            Double.TryParse(temp[1], NumberStyles.Any, g_oCulture, out latitude);
            Double.TryParse(temp[2], NumberStyles.Any, g_oCulture, out longitude);
            countyName = temp[3];
            int.TryParse(temp[4], out maturityZone);
            if (temp[5].Equals("Mid"))
            {
                maturitySubZone = 1;
            }
            else if (temp[5].Equals("Late"))
            {
                maturitySubZone = 2;
            }

            int.TryParse(temp[6], out maturityBand);
            int.TryParse(temp[7], out stateCode);
            int.TryParse(temp[8], out climateDivision);
            int.TryParse(temp[9], out fipsCode);
            //Console.WriteLine(data + " " + LOCCD + " " + latitude + " " + longitude + " " + countyName + " " + maturityZone + " " + maturitySubZone + " " + maturityBand + " " + stateCode + " " + stateCode + " " + climateDivision + " " + fipsCode);
        }

    }

    public class TrainingDataEntry
    {

        public int exID = 1;
        public int LOCCD = 1;
        public int repno = 1;
        public int variety = 1;
        public String type = "NULL";
        public double yield = 55;
        public double daysToMaturity = 130;
        public double RM = 50;
        public int day = 10;
        public int month = 5;
        public int year = 2009;
        public DateTime plantDate = DateTime.Parse("2009-05-10");

        public TrainingDataEntry(String data)
        {
            //Console.WriteLine(data);
            String[] temp = data.Split(',');
            int.TryParse(temp[0], NumberStyles.Any, g_oCulture, out exID);
            int.TryParse(temp[1], NumberStyles.Any, g_oCulture, out LOCCD);
            int.TryParse(temp[2], NumberStyles.Any, g_oCulture, out repno);
            int.TryParse(temp[3], NumberStyles.Any, g_oCulture, out variety);
            type = temp[4];

            Double.TryParse(temp[5], NumberStyles.Any, g_oCulture, out yield);
            Double.TryParse(temp[6], NumberStyles.Any, g_oCulture, out daysToMaturity);
            Double.TryParse(temp[7], NumberStyles.Any, g_oCulture, out RM);
            if (temp[8].Length > 8)
            {
                int.TryParse(temp[8].Substring(8, 2), NumberStyles.Any, g_oCulture, out day);
                int.TryParse(temp[8].Substring(5, 2), NumberStyles.Any, g_oCulture, out month);
                int.TryParse(temp[8].Substring(0, 4), NumberStyles.Any, g_oCulture, out year);
            }
            DateTime.TryParse(temp[8], out plantDate);
            //Console.WriteLine(data+" "+LOCCD+" "+repno+" "+variety+" "+type+" "+yield+" "+daysToMaturity+" "+RM+" "+day+" "+month+" "+year+" "+plantDate);

            if (g_DLocations.ContainsKey(LOCCD) == false)
            {
                int l_iTempCnt = 0;
                while (l_iTempCnt < 10000)
                {
                    l_iTempCnt++;
                    if (g_DLocations.ContainsKey(LOCCD + l_iTempCnt) == true)
                    {
                        g_DLocations.Add(LOCCD, g_DLocations[LOCCD + l_iTempCnt]);
                        break;
                    }
                    else if (g_DLocations.ContainsKey(LOCCD - l_iTempCnt) == true)
                    {
                        g_DLocations.Add(LOCCD, g_DLocations[LOCCD - l_iTempCnt]);
                        break;
                    }
                }
            }
        }
    }

    static CultureInfo g_oCulture;
    String[] g_AsTrainingData;
    String[] g_AsDroughtMonitor;
    String[] g_AsDroughtNOAA;
    String[] g_AsLocations;
    String[] g_AsQueries;
    String[] g_AsExperimentData;
    Double[] g_AdAnswers;

    double g_RPerf = 1;

    static Dictionary<int, Location> g_DLocations;

    static TrainingDataEntry[] g_OTrainingData;

    public void init()
    {
        g_oCulture = new CultureInfo("en-GB");

        // Parse data
        initLocations();
        initTrainingData();

    }

    public void initLocations()
    {
        g_DLocations = new Dictionary<int, Location>();
        for (int i = 0; i < g_AsLocations.Length; i++)
        {
            String[] temp = g_AsLocations[i].Split(',');
            if (g_DLocations.ContainsKey(int.Parse(temp[0], g_oCulture)) == false)
            {
                g_DLocations.Add(int.Parse(temp[0], g_oCulture), new Location(g_AsLocations[i]));
            }
        }
    }

    public void initTrainingData()
    {
        g_OTrainingData = new TrainingDataEntry[g_AsExperimentData.Length];
        for (int i = 0; i < g_AsExperimentData.Length; i++)
        {
            g_OTrainingData[i] = new TrainingDataEntry(g_AsExperimentData[i]);
        }

    }

    double getBestRelativePerfEstimation(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {

        // First put all perfs in Map - for this particular Ex
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();

        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        double l_dRelativePerf = 0;
        int l_iRelativePerfCnt = 0;

        // Get averages perfs
        foreach (String lConfig in l_DConfigurations.Keys)
        {
            String l_sTempKey = String.Concat(lConfig, ";", p_iVariety.ToString());
            if (l_DYields.ContainsKey(l_sTempKey) == false) continue;


            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lMat in l_DVarieties.Keys)
            {
                //if (p_iVariety.ToString().Equals(lMat)) continue;
                l_sTempKey = String.Concat(lConfig, ";", lMat);
                if (l_DYields.ContainsKey(l_sTempKey) == true)
                {
                    l_dSum += l_DYields[l_sTempKey];
                    l_iCnt++;
                }
            }

            if (l_iCnt > 0)
            {
                int nbR = 1;
                string[] tmp = lConfig.Split(';');
                if (tmp[0].Equals(p_iLOCCD.ToString()) == true)
                {
                    nbR = 9;
                }

                for (int rr = 0; rr < nbR; rr++)
                {
                    l_sTempKey = String.Concat(lConfig, ";", p_iVariety.ToString());
                    double l_dDSum = l_dSum / (double)l_iCnt;
                    l_dRelativePerf += l_DYields[l_sTempKey] / l_dDSum;
                    l_iRelativePerfCnt++;
                }
            }
        }

        if (l_iRelativePerfCnt > 0)
        {
            l_dRelativePerf /= (double)l_iRelativePerfCnt;

        }
        else
        {
            l_dRelativePerf = 1;
            Console.WriteLine("BUG ??");
        }

        g_RPerf = l_dRelativePerf;

        double l_dAvPerf = 0;
        int l_iAvPerfCnt = 0;
        // Get the average on the current problem and multiply
        foreach (String lMat in l_DVarieties.Keys)
        {
            String l_sTempKey = String.Concat(p_iLOCCD, ";", p_iRepNo, ";", lMat);
            if (l_DYields.ContainsKey(l_sTempKey) == false) continue;
            l_dAvPerf += l_DYields[l_sTempKey];
            l_iAvPerfCnt++;
        }

        l_dRelativePerf = Math.Pow(l_dRelativePerf, 0.85);

        if (l_iAvPerfCnt > 0)
        {
            l_dAvPerf /= (double)l_iAvPerfCnt;
            // TODO : Still have to explain this bias...
            return l_dRelativePerf * l_dAvPerf;

        }
        else
        {
            Console.WriteLine("BUG ???");
            return 50;
        }


    }

    double getBestEstimationKNN(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {
        String l_sConfigCheckKey = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString());

        // First put all perfs in Map - for this particular Ex
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurationsDist = new Dictionary<String, double>();

        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        double l_dVoteSum = 0;
        double l_dVoteCnt = 0;

        // Get Locid relative distances first
        foreach (String lKey in l_DConfigurations.Keys)
        {
            if (lKey.Equals(l_sConfigCheckKey)) continue;

            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += Math.Abs(l_DYields[l_tKey] - l_DYields[l_sKey]);
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;

            if (l_DConfigurationsDist.ContainsKey(lKey) == false)
            {
                //Console.WriteLine(l_dSum + " " + l_iCnt + " " + (l_dSum / l_iCnt));
                l_DConfigurationsDist.Add(lKey, (double)Math.Sqrt(l_dSum / l_iCnt));
            }
            else
            {
                Console.WriteLine("PB ??");
            }

        }

        foreach (String lKey in l_DVarieties.Keys)
        {
            if (lKey.Equals(p_iVariety.ToString()) == true) continue;
            String l_sCheckKey = String.Concat(p_iLOCCD, ";", p_iRepNo, ";", lKey);
            if (l_DYields.ContainsKey(l_sCheckKey) == false)
            {
                //Console.WriteLine("Skip " + l_sCheckKey);
                continue;
            }

            double l_dSum = 0;
            double l_dS = 0;
            int l_iCnt = 0;
            double l_dSumLoc = 0;

            // Weight by locid distances
            foreach (String lKeyC in l_DConfigurations.Keys)
            {
                String l_sTempKey = String.Concat(lKeyC, ";", lKey);
                String l_sTempKeyCur = String.Concat(lKeyC, ";", p_iVariety.ToString());

                if (l_DYields.ContainsKey(l_sTempKey) == false || l_DYields.ContainsKey(l_sTempKeyCur) == false)
                {
                    //Console.WriteLine("Can't compare " + l_sTempKey + " " + l_sTempKeyCur);
                    continue;
                }

                double l_dLDist = 1;

                if (l_DConfigurationsDist.ContainsKey(lKeyC) == true)
                {
                    l_dLDist = l_DConfigurationsDist[lKeyC];
                }

                l_dSum += Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                l_dS += (l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                l_iCnt++;
                l_dSumLoc += 1 / l_dLDist;

                String[] tete = lKeyC.Split(';');
                if (tete[0].Equals(p_iLOCCD.ToString()))
                {
                    for (int d = 0; d < 1; d++)
                    {
                        l_dSum += Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                        l_dS += (l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                        l_iCnt++;
                        l_dSumLoc += 1 / l_dLDist;
                    }
                }
            }

            if (l_iCnt == 0) continue;

            if (l_dSum < 0.001) l_dSum = 0.001;
            if (l_dSumLoc < 0.01) l_dSumLoc = 0.01;
            l_dS /= l_iCnt;
            l_dVoteSum += (l_DYields[l_sCheckKey] - l_dS) / ((l_dSum * l_dSum) / (l_dSumLoc));
            l_dVoteCnt += 1 / ((l_dSum * l_dSum) / (l_dSumLoc));

        }

        double res = (l_dVoteSum / l_dVoteCnt);
        if (double.IsNaN(res) || double.IsInfinity(res))
        {
            Console.WriteLine(l_dVoteSum + " " + l_dVoteCnt);
            return 50;
        }

        return (l_dVoteSum / l_dVoteCnt);

    }

    double getRelativePerfEstimation(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {
        String l_sConfigCheckKey = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString());
        // First put all perfs in Map - for this particular Ex
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurationsDist = new Dictionary<String, double>();

        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        double l_dRelativePerf = 0;
        double l_iRelativePerfCnt = 0;

        // Get Locid relative distances first
        foreach (String lKey in l_DConfigurations.Keys)
        {
            if (lKey.Equals(l_sConfigCheckKey)) continue;

            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += (l_DYields[l_tKey] - l_DYields[l_sKey]);
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;

            double lDiff = (l_dSum / l_iCnt);

            l_dSum = 0;
            l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += Math.Abs(l_DYields[l_tKey] - l_DYields[l_sKey] - lDiff);
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;

            if (l_DConfigurationsDist.ContainsKey(lKey) == false)
            {
                //Console.WriteLine(l_dSum + " " + l_iCnt + " " + (l_dSum / l_iCnt));
                l_DConfigurationsDist.Add(lKey, (double)Math.Sqrt(l_dSum / l_iCnt));
            }
            else
            {
                Console.WriteLine("PB ??");
            }

        }

        // Get averages perfs
        foreach (String lConfig in l_DConfigurations.Keys)
        {
            String l_sTempKey = String.Concat(lConfig, ";", p_iVariety.ToString());
            if (l_DYields.ContainsKey(l_sTempKey) == false) continue;

            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lMat in l_DVarieties.Keys)
            {
                //if (p_iVariety.ToString().Equals(lMat)) continue;
                l_sTempKey = String.Concat(lConfig, ";", lMat);
                if (l_DYields.ContainsKey(l_sTempKey) == true)
                {
                    l_dSum += l_DYields[l_sTempKey];
                    l_iCnt++;
                }
            }

            if (l_iCnt > 0)
            {
                int nbR = 1;
                string[] tmp = lConfig.Split(';');
                if (tmp[0].Equals(p_iLOCCD.ToString()) == true)
                {
                    nbR = 10;
                }

                double l_dLDist = 2;

                if (l_DConfigurationsDist.ContainsKey(lConfig) == true)
                {
                    l_dLDist = l_DConfigurationsDist[lConfig];
                }
                
                for (int rr = 0; rr < nbR; rr++)
                {
                    l_sTempKey = String.Concat(lConfig, ";", p_iVariety.ToString());
                    double l_dDSum = l_dSum / (double)l_iCnt;

                    l_dRelativePerf += (l_DYields[l_sTempKey] / l_dDSum) / l_dLDist;
                    l_iRelativePerfCnt+= (1/l_dLDist);
                }
            }
        }

        if (l_iRelativePerfCnt > 0)
        {
            l_dRelativePerf /= (double)l_iRelativePerfCnt;

        }
        else
        {
            l_dRelativePerf = 1;
            Console.WriteLine("BUG ??");
        }

        g_RPerf = l_dRelativePerf;

        double l_dAvPerf = 0;
        int l_iAvPerfCnt = 0;
        // Get the average on the current problem and multiply
        foreach (String lMat in l_DVarieties.Keys)
        {
            String l_sTempKey = String.Concat(p_iLOCCD, ";", p_iRepNo, ";", lMat);
            if (l_DYields.ContainsKey(l_sTempKey) == false) continue;
            l_dAvPerf += l_DYields[l_sTempKey];
            l_iAvPerfCnt++;
        }

        if (l_iAvPerfCnt > 0)
        {
            l_dAvPerf /= (double)l_iAvPerfCnt;
            // TODO : Still have to explain this bias...
            //Console.Write(" " + l_dAvPerf + " " + l_dRelativePerf);
            return l_dRelativePerf * l_dAvPerf ;


        }
        else
        {
            Console.WriteLine("BUG ???");
            return 50;
        }

    }

    double getEstimationKNN(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {
        String l_sConfigCheckKey = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString());

        // First put all perfs in Map - for this particular Ex
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurationsDist = new Dictionary<String, double>();

        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        double l_dVoteSum = 0;
        double l_dVoteCnt = 0;

        // Get Locid relative distances first
        foreach (String lKey in l_DConfigurations.Keys)
        {
            if (lKey.Equals(l_sConfigCheckKey)) continue;

            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += Math.Abs(l_DYields[l_tKey] - l_DYields[l_sKey]);
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;
            
            if (l_DConfigurationsDist.ContainsKey(lKey) == false)
            {
                //Console.WriteLine(l_dSum + " " + l_iCnt + " " + (l_dSum / l_iCnt));
                l_DConfigurationsDist.Add(lKey, (double)Math.Sqrt(l_dSum / l_iCnt));
            }
            else
            {
                Console.WriteLine("PB ??");
            }

        }

        foreach (String lKey in l_DVarieties.Keys)
        {
            if (lKey.Equals(p_iVariety.ToString()) == true) continue;
            String l_sCheckKey = String.Concat(p_iLOCCD, ";", p_iRepNo, ";", lKey);
            if (l_DYields.ContainsKey(l_sCheckKey) == false)
            {
                //Console.WriteLine("Skip " + l_sCheckKey);
                continue;
            }

            double l_dSum = 0;
            double l_dS = 0;
            int l_iCnt = 0;
            double l_dSumLoc = 0;

            // Weight by locid distances
            foreach (String lKeyC in l_DConfigurations.Keys)
            {
                String l_sTempKey = String.Concat(lKeyC, ";", lKey);
                String l_sTempKeyCur = String.Concat(lKeyC, ";", p_iVariety.ToString());

                if (l_DYields.ContainsKey(l_sTempKey) == false || l_DYields.ContainsKey(l_sTempKeyCur) == false)
                {
                    //Console.WriteLine("Can't compare " + l_sTempKey + " " + l_sTempKeyCur);
                    continue;
                }
                
                double l_dLDist = 1;

                if (l_DConfigurationsDist.ContainsKey(lKeyC) == true)
                {
                    l_dLDist = l_DConfigurationsDist[lKeyC];
                }

                l_dSum += Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                l_dS += (l_DYields[l_sTempKeyCur] - l_DYields[l_sTempKey]) / l_dLDist;
                l_iCnt++;
                l_dSumLoc += 1 / l_dLDist;

                String[] tete = lKeyC.Split(';');
                if (tete[0].Equals(p_iLOCCD.ToString()))
                {
                    for (int d = 0; d < 1; d++)
                    {
                        l_dSum += Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                        l_dS += (l_DYields[l_sTempKeyCur] - l_DYields[l_sTempKey]) / l_dLDist;
                        l_iCnt++;
                        l_dSumLoc += 1 / l_dLDist;
                    }
                }
            }

            if (l_iCnt == 0) continue;

            if (l_dSum < 0.001) l_dSum = 0.001;
            if (l_dSumLoc < 0.01) l_dSumLoc = 0.01;
            l_dS /= l_iCnt;
            l_dVoteSum += (l_DYields[l_sCheckKey] + l_dS) / ((l_dSum * l_dSum / l_dSumLoc));
            l_dVoteCnt += 1 / ((l_dSum * l_dSum / l_dSumLoc));

        }

        double res = (l_dVoteSum / l_dVoteCnt);
        if (double.IsNaN(res) || double.IsInfinity(res))
        {
            Console.WriteLine(l_dVoteSum + " " + l_dVoteCnt);
            return 50;
        }

        return (l_dVoteSum / l_dVoteCnt);

    }
    
    double getEstimationKNNWithStdDevOnDiff(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {
        String l_sConfigCheckKey = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString());
        Random toto = new Random();
        // First put all perfs in Map - for this particular Ex
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurationsDist = new Dictionary<String, double>();

        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        double l_dVoteSum = 0;
        double l_dVoteCnt = 0;

        // Get Locid relative distances first
        foreach (String lKey in l_DConfigurations.Keys)
        {
            if (lKey.Equals(l_sConfigCheckKey)) continue;

            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += (l_DYields[l_tKey] - l_DYields[l_sKey]);
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;

            double lDiff = (l_dSum / l_iCnt);

            l_dSum = 0;
            l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += Math.Abs(l_DYields[l_tKey] - l_DYields[l_sKey] - lDiff) ;
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;

            if (l_DConfigurationsDist.ContainsKey(lKey) == false)
            {
                //Console.WriteLine(l_dSum + " " + l_iCnt + " " + (l_dSum / l_iCnt));
                l_DConfigurationsDist.Add(lKey, (double)Math.Sqrt(l_dSum / l_iCnt));
            }
            else
            {
                Console.WriteLine("PB ??");
            }

        }

        foreach (String lKey in l_DVarieties.Keys)
        {
            if (lKey.Equals(p_iVariety.ToString()) == true) continue;
            String l_sCheckKey = String.Concat(p_iLOCCD, ";", p_iRepNo, ";", lKey);
            if (l_DYields.ContainsKey(l_sCheckKey) == false)
            {
                //Console.WriteLine("Skip " + l_sCheckKey);
                continue;
            }

            double l_dSum = 0;
            double l_dS = 0;
            int l_iCnt = 0;
            double l_tSum = 0;

            // Get average difference first
            foreach (String lKeyC in l_DConfigurations.Keys)
            {
                String l_sTempKey = String.Concat(lKeyC, ";", lKey);
                String l_sTempKeyCur = String.Concat(lKeyC, ";", p_iVariety.ToString());

                if (l_DYields.ContainsKey(l_sTempKey) == false || l_DYields.ContainsKey(l_sTempKeyCur) == false)
                {
                    //Console.WriteLine("Can't compare " + l_sTempKey + " " + l_sTempKeyCur);
                    continue;
                }

                double l_dLDist = 1;

                if (l_DConfigurationsDist.ContainsKey(lKeyC) == true)
                {
                    l_dLDist = l_DConfigurationsDist[lKeyC];
                }

                l_dSum += (l_DYields[l_sTempKeyCur] - l_DYields[l_sTempKey]) / l_dLDist;
                l_tSum += (1 / l_dLDist);
                l_iCnt++;
            }

            double l_dAvDiff = 0;
            //Console.WriteLine(l_iCnt);
            if (l_tSum > 0) // TODO: Check that one...
            {
                l_dAvDiff = l_dSum / l_tSum;
                //Console.WriteLine(l_dAvDiff);
            }
            
            l_dSum = 0;
            l_dS = 0;
            l_iCnt = 0;
            double lTT = 0;

            // Weight by locid distances
            foreach (String lKeyC in l_DConfigurations.Keys)
            {
                String l_sTempKey = String.Concat(lKeyC, ";", lKey);
                String l_sTempKeyCur = String.Concat(lKeyC, ";", p_iVariety.ToString());

                if (l_DYields.ContainsKey(l_sTempKey) == false || l_DYields.ContainsKey(l_sTempKeyCur) == false)
                {
                    //Console.WriteLine("Can't compare " + l_sTempKey + " " + l_sTempKeyCur);
                    continue;
                }

                double l_dLDist = 1;

                if (l_DConfigurationsDist.ContainsKey(lKeyC) == true)
                {
                    l_dLDist = l_DConfigurationsDist[lKeyC] ;
                }

                //Console.WriteLine(p_iExID + " " + lKeyC + " " + lKey + " " + l_dLDist + " " + Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur] - l_dAvDiff));

                l_dSum += (Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur] - l_dAvDiff) * Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur] - l_dAvDiff));
                double tt = Math.Pow(Math.Abs(l_DYields[l_sTempKeyCur] - l_DYields[l_sTempKey]), 0.9);
                if (l_DYields[l_sTempKeyCur] - l_DYields[l_sTempKey] < 0) tt = 0 - tt;
                l_dS += tt;
                l_iCnt++;
                lTT += (1/l_dLDist);

                String[] tete = lKeyC.Split(';');
                if (tete[0].Equals(p_iLOCCD.ToString()))
                {
                    for (int d = 0; d < 1; d++)
                    {
                        l_dSum += (Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur] - l_dAvDiff) * Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur] - l_dAvDiff));
                        l_dS += tt ;
                        l_iCnt++;
                        lTT += (1/l_dLDist);
                    }
                }
            }

            if (l_iCnt == 0) continue;

            if (l_dSum < 0.001) l_dSum = 0.001;

            l_dS /= l_iCnt ;
            
            //Console.WriteLine(lKey + " " + l_DYields[l_sCheckKey] + " " + l_dS + " = " + (l_DYields[l_sCheckKey] + l_dS));
            l_dVoteSum += (l_DYields[l_sCheckKey] + l_dS) / ((l_dSum) );
            l_dVoteCnt += 1 / ((l_dSum) );
            
        }
        
        double res = (l_dVoteSum / l_dVoteCnt);
        if (double.IsNaN(res) || double.IsInfinity(res))
        {
            Console.WriteLine(l_dVoteSum + " " + l_dVoteCnt);
            return 50;
        }

        return (l_dVoteSum / l_dVoteCnt);

    }
    
    double getEstimationKNNRelative(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {
        String l_sConfigCheckKey = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString());

        // First put all perfs in Map - for this particular Ex
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurationsDist = new Dictionary<String, double>();

        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        double l_dVoteSum = 0;
        double l_dVoteCnt = 0;

        // Get Locid relative distances first
        foreach (String lKey in l_DConfigurations.Keys)
        {
            if (lKey.Equals(l_sConfigCheckKey)) continue;

            double l_dSum = 0;
            int l_iCnt = 0;

            foreach (String lVar in l_DVarieties.Keys)
            {
                String l_tKey = String.Concat(l_sConfigCheckKey, ";", lVar.ToString());
                String l_sKey = String.Concat(lKey, ";", lVar.ToString());

                if (l_DYields.ContainsKey(l_tKey) == false || l_DYields.ContainsKey(l_sKey) == false) continue;
                l_dSum += Math.Abs(l_DYields[l_tKey] - l_DYields[l_sKey]);
                l_iCnt++;
            }

            if (l_iCnt == 0) continue;
            if (l_dSum < 0.01) l_dSum = 0.01;

            if (l_DConfigurationsDist.ContainsKey(lKey) == false)
            {
                //Console.WriteLine(l_dSum + " " + l_iCnt + " " + (l_dSum / l_iCnt));
                l_DConfigurationsDist.Add(lKey, (double)Math.Sqrt(l_dSum / l_iCnt));
            }
            else
            {
                Console.WriteLine("PB ??");
            }

        }

        foreach (String lKey in l_DVarieties.Keys)
        {
            if (lKey.Equals(p_iVariety.ToString()) == true) continue;
            String l_sCheckKey = String.Concat(p_iLOCCD, ";", p_iRepNo, ";", lKey);
            if (l_DYields.ContainsKey(l_sCheckKey) == false)
            {
                //Console.WriteLine("Skip " + l_sCheckKey);
                continue;
            }

            double l_dSum = 0;
            double l_dS = 0;
            int l_iCnt = 0;
            double l_dSumLoc = 0;

            // Weight by locid distances
            foreach (String lKeyC in l_DConfigurations.Keys)
            {
                String l_sTempKey = String.Concat(lKeyC, ";", lKey);
                String l_sTempKeyCur = String.Concat(lKeyC, ";", p_iVariety.ToString());

                if (l_DYields.ContainsKey(l_sTempKey) == false || l_DYields.ContainsKey(l_sTempKeyCur) == false)
                {
                    //Console.WriteLine("Can't compare " + l_sTempKey + " " + l_sTempKeyCur);
                    continue;
                }

                double l_dLDist = 1;

                if (l_DConfigurationsDist.ContainsKey(lKeyC) == true)
                {
                    //l_dLDist = l_DConfigurationsDist[lKeyC];
                }

                l_dSum += Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                l_dS += (l_DYields[l_sTempKeyCur] / l_DYields[l_sTempKey]);
                l_iCnt++;
                l_dSumLoc += 1 / l_dLDist;

                String[] tete = lKeyC.Split(';');
                if (tete[0].Equals(p_iLOCCD.ToString()))
                {
                    for (int d = 0; d < 1; d++)
                    {
                        l_dSum += Math.Abs(l_DYields[l_sTempKey] - l_DYields[l_sTempKeyCur]) / l_dLDist;
                        l_dS += (l_DYields[l_sTempKeyCur] / l_DYields[l_sTempKey]);
                        l_iCnt++;
                        l_dSumLoc += 1 / l_dLDist;
                    }
                }
            }

            if (l_iCnt == 0) continue;

            if (l_dSum < 0.01) l_dSum = 0.01;
            if (l_dSumLoc < 0.01) l_dSumLoc = 0.01;
            l_dS /= l_iCnt;
            l_dVoteSum += (l_DYields[l_sCheckKey] * l_dS) / (l_dSum * l_dSum);
            l_dVoteCnt += 1 / (l_dSum * l_dSum);

        }

        double res = (l_dVoteSum / l_dVoteCnt);
        if (double.IsNaN(res) || double.IsInfinity(res))
        {
            Console.WriteLine(l_dVoteSum + " " + l_dVoteCnt);
            return 50;
        }

        return (l_dVoteSum / l_dVoteCnt);

    }

    double getEstimationKNNPosition(int p_iExID, int p_iLOCCD, int p_iVariety, int p_iRepNo)
    {
        String l_sConfigCheckKey = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString());
        // Based on position only
        Dictionary<String, double> l_DVarieties = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurations = new Dictionary<String, double>();
        Dictionary<String, double> l_DConfigurationsD = new Dictionary<String, double>();
        Dictionary<String, double> l_DYields = new Dictionary<String, double>();
        Dictionary<String, double> l_DPositions = new Dictionary<String, double>();
        Dictionary<String, double> l_DPositionsCnt = new Dictionary<String, double>();
        Dictionary<String, double> l_DAvPositions = new Dictionary<String, double>();
        Dictionary<String, double> l_DTargetOrder = new Dictionary<String, double>();
        
        for (int i = 0; i < g_OTrainingData.Length; i++)
        {
            if (g_OTrainingData[i].exID != p_iExID) continue;

            String l_sTempKey = g_OTrainingData[i].variety.ToString();
            if (l_DVarieties.ContainsKey(l_sTempKey) == false) l_DVarieties.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno);
            if (l_DConfigurations.ContainsKey(l_sTempKey) == false) l_DConfigurations.Add(l_sTempKey, 1);

            l_sTempKey = String.Concat(g_OTrainingData[i].LOCCD, ";", g_OTrainingData[i].repno, ";", g_OTrainingData[i].variety);
            if (l_DYields.ContainsKey(l_sTempKey) == false) l_DYields.Add(l_sTempKey, g_OTrainingData[i].yield);
        }

        //Console.WriteLine("----------------------------");
        List<KeyValuePair<String, double>> l_DTempC = new List<KeyValuePair<String, double>>();
        foreach (String lKeyV in l_DVarieties.Keys)
        {
            String l_sTemp = String.Concat(String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString(), ";", lKeyV));
            if (l_DYields.ContainsKey(l_sTemp))
            {
                l_DTempC.Add(new KeyValuePair<String, double>(lKeyV, l_DYields[l_sTemp]));
            }

        }

        l_DTempC.Sort(CompareDouble);

        for(int i=0;i<l_DTempC.Count;i++){
            l_DTargetOrder.Add(l_DTempC[i].Key, i);
        }

        // Get the positions for each configuration
        foreach (String lKeyC in l_DConfigurations.Keys)
        {
            if(lKeyC.Equals(l_sConfigCheckKey))continue;
            List<KeyValuePair<String, double>> l_DTemp = new List<KeyValuePair<String, double>>();
            foreach (String lKeyV in l_DVarieties.Keys)
            {
                String l_sTemp = String.Concat(lKeyC, ";", lKeyV);
                if (l_DYields.ContainsKey(l_sTemp))
                {
                    l_DTemp.Add(new KeyValuePair<String, double>(lKeyV, l_DYields[l_sTemp]));
                }

            }

            l_DTemp.Sort(CompareDouble);
            
            double dist = 0;
            // Get the average distance
            for (int i = 0; i < l_DTemp.Count; i++)
            {
                double tPos = 5;
                if (l_DTargetOrder.ContainsKey(l_DTemp[i].Key) == true)
                {
                    tPos = l_DTargetOrder[l_DTemp[i].Key];
                }
                
                dist += Math.Abs(tPos - i) * Math.Abs(tPos - i);
            }

            dist *= dist;
            l_DConfigurationsD.Add(lKeyC, dist);
            //Console.WriteLine(lKeyC + " " + dist);
            
            for (int i = 0; i < l_DTemp.Count; i++)
            {
                //if(l_DTemp[i].Key.Equals(p_iVariety.ToString())) Console.WriteLine(lKeyC + " " + l_DTemp[i].Key + " " + l_DTemp[i].Value + " " + i + " " + dist);
                if (l_DPositions.ContainsKey(l_DTemp[i].Key) == true)
                {
                    l_DPositions[l_DTemp[i].Key] += i / dist;
                    l_DPositionsCnt[l_DTemp[i].Key] += (1/dist);
                }
                else
                {
                    l_DPositions.Add(l_DTemp[i].Key, i / dist);
                    l_DPositionsCnt.Add(l_DTemp[i].Key, (1 / dist));
                }
            }
        }

        List<KeyValuePair<String, double>> l_DScores = new List<KeyValuePair<String, double>>();
        foreach (String lKeyV in l_DPositions.Keys)
        {
            l_DAvPositions.Add(lKeyV, l_DPositions[lKeyV] / l_DPositionsCnt[lKeyV]);
            l_DScores.Add(new KeyValuePair<String, double>(lKeyV, l_DAvPositions[lKeyV]));
        }

        l_DScores.Sort(CompareDouble);

        int pos = 0;
        for (int i = 0; i < l_DScores.Count; i++)
        {
            //Console.WriteLine(l_DScores[i].Key + " " + i + " " + l_DScores[i].Value);
            if (l_DScores[i].Key.Equals(p_iVariety.ToString()) == true)
            {
                pos = (int) ( Math.Round(l_DScores[i].Value) );
                //Console.WriteLine("--> " + pos);
            }
        }

        // Get the estimation
        List<KeyValuePair<String, double>> l_DTemp2 = new List<KeyValuePair<String, double>>();
        foreach (String lKeyV in l_DVarieties.Keys)
        {
            String l_sTemp = String.Concat(p_iLOCCD.ToString(), ";", p_iRepNo.ToString(), ";", lKeyV);
            if (l_DYields.ContainsKey(l_sTemp))
            {
                l_DTemp2.Add(new KeyValuePair<String, double>(lKeyV, l_DYields[l_sTemp]));
            }
        }

        l_DTemp2.Sort(CompareDouble);
        if (pos < 0) pos = 0;
        if (pos >= l_DTemp2.Count) pos = l_DTemp2.Count - 1;
        if (pos >= 0 && pos < l_DTemp2.Count)
        {
            //Console.WriteLine("Pos "  + pos + " Score " + l_DTemp2[pos].Value);
            return l_DTemp2[pos].Value;
        }
        //Console.WriteLine("Can't predict " + pos);

        return l_DTemp2[l_DTemp2.Count - 1].Value;

    }


#if HOME
    public double[] predictYield(String[] trainingData, String[] droughtMonitor, String[] droughtNOAA, String[] locations, String[] queries, String[] experimentData, double[] answers)
    {
#else
    public double[] predictYield(String[] trainingData, String[] droughtMonitor, String[] droughtNOAA, String[] locations, String[] queries, String[] experimentData)
    {
#endif
        Stopwatch stopwatch = Stopwatch.StartNew();
        g_AsTrainingData = trainingData;
        g_AsDroughtMonitor = droughtMonitor;
        g_AsDroughtNOAA = droughtNOAA;
        g_AsLocations = locations;
        g_AsQueries = queries;
        g_AsExperimentData = experimentData;
#if HOME
        g_AdAnswers = answers;
#endif
        init();

        double[] ret = new double[queries.Length];

        // Get estimations
        for (int i = 0; i < queries.Length; i++)
        {
            String[] temp = queries[i].Split(',');
            //Console.WriteLine(" -----> " + answers[i]);
            int l_iExID = 1;
            int.TryParse(temp[0], out l_iExID);
            int l_iLOCCD = 0;
            int.TryParse(temp[1], out l_iLOCCD);
            int l_iRepNo = 0;
            int.TryParse(temp[2], out l_iRepNo);
            int l_iVariety = 0;
            int.TryParse(temp[3], out l_iVariety);


            //double relativePerfScore = getRelativePerfEstimation(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);
            //double KNNBase = getEstimationKNN(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);
            //double KNNRelative = getEstimationKNNRelative(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);
            //double KNNWithStdDevOnDiff = getEstimationKNNWithStdDevOnDiff(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);
            //double KNNPosition = getEstimationKNNPosition(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);
            double bestRelative = getBestRelativePerfEstimation(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);
            double KNNBest = getBestEstimationKNN(l_iExID, l_iLOCCD, l_iVariety, l_iRepNo);

            //Console.WriteLine(g_RPerf + " " + KNNBase + " " + KNNRelative + " " + KNNWithStdDevOnDiff + " " + KNNPosition + " " + bestRelative + " " + KNNBest + " " + answers[i]);
            ret[i] = (KNNBest+bestRelative) /2;
            
            //Console.WriteLine(g_RPerf+ " " + KNNWithStdDevOnDiff + " " + relativePerfScore + " " + KNNWithStdDevOnDiffRelative + " " + ret[i] + " " + answers[i]);
            
        } 

        stopwatch.Stop();
        //Console.WriteLine("Time " + stopwatch.Elapsed);

        return ret;
    }
}
