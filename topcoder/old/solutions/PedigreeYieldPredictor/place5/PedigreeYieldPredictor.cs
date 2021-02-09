//#define HOME

using System;
using System.Collections.Generic;
using System.Text;
using System.Globalization;
using System.Diagnostics;
using System.Threading;


public class PedigreeYieldPredictor
{
    double compareScores(double p_dA, double p_dB)
    {
        if (p_dA < p_dB ) return 0;
        if (p_dA > p_dB ) return 1;
        return 0.5;
    }

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

    static int CompareIntDouble(KeyValuePair<int, double> a, KeyValuePair<int, double> b)
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

    public class Material
    {
        public int materialID=0;
        public String pedigree = "NULL";
        public String type = "conv";
        public double RM = -1;
        public double avRM = -1;

        public Material(String data)
        {
            String[] temp = data.Split(',');
            int.TryParse(temp[0], out materialID);
            pedigree = temp[1];
            type = temp[2];
            Double.TryParse(temp[3], NumberStyles.Any, g_oCulture, out RM);
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

            Double.TryParse(temp[4], NumberStyles.Any, g_oCulture, out yield);
            Double.TryParse(temp[5], NumberStyles.Any, g_oCulture, out daysToMaturity);
            if (temp[6].Length > 8)
            {
                int.TryParse(temp[6].Substring(8, 2), NumberStyles.Any, g_oCulture, out day);
                int.TryParse(temp[6].Substring(5, 2), NumberStyles.Any, g_oCulture, out month);
                int.TryParse(temp[6].Substring(0, 4), NumberStyles.Any, g_oCulture, out year);
            }
            DateTime.TryParse(temp[6], out plantDate);
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
    String[] g_AsMaterials;
    String[] g_AsQueries;
    String[] g_AsAnswers;

    static Dictionary<int, Location> g_DLocations;
    static Dictionary<int, Material> g_DMaterials;
    static Dictionary<String, double> g_DPedigreesRM;

    Dictionary<String, double> g_DYield;
    Dictionary<String, int> g_DYieldCnt;

    Dictionary<String, double> g_DYieldPos;
    Dictionary<String, int> g_DYieldCntPos;

    static TrainingDataEntry[] g_OTrainingData;

    public void init()
    {
        g_oCulture = new CultureInfo("en-GB");

        // Parse data
        initLocations();
        initMaterials();
        initTrainingData();

    }

    public void initMaterials()
    {
        g_DMaterials = new Dictionary<int, Material>();
        for (int i = 0; i < g_AsMaterials.Length; i++)
        {
            String[] temp = g_AsMaterials[i].Split(',');
            if (g_DMaterials.ContainsKey(int.Parse(temp[0], g_oCulture)) == false)
            {
                g_DMaterials.Add(int.Parse(temp[0], g_oCulture), new Material(g_AsMaterials[i]));
            }
            else
            {
                if (g_AsMaterials[i].Contains("NULL") == false)
                {
                    g_DMaterials[int.Parse(temp[0], g_oCulture)] = new Material(g_AsMaterials[i]);
                }
            }
        }
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
        g_OTrainingData = new TrainingDataEntry[g_AsTrainingData.Length];
        for (int i = 0; i < g_AsTrainingData.Length; i++)
        {
            g_OTrainingData[i] = new TrainingDataEntry(g_AsTrainingData[i]);
        }

    }

    public void initRelativeData()
    {
        g_DYield = new Dictionary<String, double>();
        g_DYieldCnt = new Dictionary<String, int>();

        Dictionary<String, double> l_DExYield = new Dictionary<String, double>();
        Dictionary<String, double> l_DExYieldCnt = new Dictionary<String, double>();
        
        for (int k = 0; k < g_OTrainingData.Length; k++)
        {

            double l_dYield = 0;
            String l_sKey = "";

            if (g_DMaterials.ContainsKey(g_OTrainingData[k].variety) == false)
            {
                continue;
            }

            l_dYield = g_OTrainingData[k].yield;

            // ExID + Rep + Year + locId + Pedigree
            l_sKey = String.Concat("ERYLP;", g_OTrainingData[k].exID, ";", g_OTrainingData[k].repno, ";", g_OTrainingData[k].year.ToString(), ";", g_OTrainingData[k].LOCCD.ToString(), ";", g_DMaterials[g_OTrainingData[k].variety].pedigree);

            if (l_DExYield.ContainsKey(l_sKey) == false)
            {
                l_DExYield.Add(l_sKey, l_dYield);
                l_DExYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                l_DExYield[l_sKey] += l_dYield;
                l_DExYieldCnt[l_sKey] += 1;
            }

            l_sKey = String.Concat("ERYL;", g_OTrainingData[k].exID, ";", g_OTrainingData[k].repno, ";", g_OTrainingData[k].year.ToString(), ";", g_OTrainingData[k].LOCCD.ToString());

            if (l_DExYield.ContainsKey(l_sKey) == false)
            {
                l_DExYield.Add(l_sKey, l_dYield);
                l_DExYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                l_DExYield[l_sKey] += l_dYield;
                l_DExYieldCnt[l_sKey] += 1;
            }
        }

        foreach (String lKey in l_DExYieldCnt.Keys)
        {
            l_DExYield[lKey] /= l_DExYieldCnt[lKey];
        }

        foreach (String lKey in l_DExYieldCnt.Keys)
        {
            if (lKey.StartsWith("ERYLP;") == false)
            {
                continue;
            }
            
            // Insert for all keys
            String[] l_sSplit = lKey.Split(';');

            String l_sExKey = String.Concat("ERYL;", l_sSplit[1], ";", l_sSplit[2], ";", l_sSplit[3], ";", l_sSplit[4]); 
            
            // Year + locId + Pedigree
            String l_sKey = String.Concat("YLP;", l_sSplit[3], ";", l_sSplit[4], ";", l_sSplit[5]);
            
            if (g_DYield.ContainsKey(l_sKey) == false)
            {
                //Console.WriteLine(l_sKey + " " + l_sExKey + " " + l_DExYield[lKey] + " " + l_DExYield[l_sExKey]);
                g_DYield.Add(l_sKey, l_DExYield[lKey] / l_DExYield[l_sExKey]);
                g_DYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                g_DYield[l_sKey] += l_DExYield[lKey] / l_DExYield[l_sExKey];
                g_DYieldCnt[l_sKey]++;
            }

            // locId + Pedigree
            l_sKey = String.Concat("LP;", l_sSplit[4], ";", l_sSplit[5]);

            if (g_DYield.ContainsKey(l_sKey) == false)
            {
                g_DYield.Add(l_sKey, l_DExYield[lKey] / l_DExYield[l_sExKey]);
                g_DYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                g_DYield[l_sKey] += l_DExYield[lKey] / l_DExYield[l_sExKey];
                g_DYieldCnt[l_sKey]++;
            }

            // pedigree
            l_sKey = String.Concat("P;", l_sSplit[5]);

            if (g_DYield.ContainsKey(l_sKey) == false)
            {
                g_DYield.Add(l_sKey, l_DExYield[lKey] / l_DExYield[l_sExKey]);
                g_DYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                g_DYield[l_sKey] += l_DExYield[lKey] / l_DExYield[l_sExKey];
                g_DYieldCnt[l_sKey]++;
            }

            // matBand + Pedigree
            int l_iLocid = 1;
            int.TryParse(l_sSplit[4], out l_iLocid);
            String l_sMatBand = "";
            if (g_DLocations.ContainsKey(l_iLocid) == true)
            {
                l_sMatBand = g_DLocations[l_iLocid].maturityBand.ToString();
            }

            // year + matBand + Pedigree
            l_sKey = String.Concat("YMP;", l_sSplit[3], ";", l_sMatBand, ";", l_sSplit[5]);

            if (g_DYield.ContainsKey(l_sKey) == false)
            {
                g_DYield.Add(l_sKey, l_DExYield[lKey] / l_DExYield[l_sExKey]);
                g_DYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                g_DYield[l_sKey] += l_DExYield[lKey] / l_DExYield[l_sExKey];
                g_DYieldCnt[l_sKey]++;
            }

            // matBand + Pedigree
            l_sKey = String.Concat("MP;", l_sMatBand, ";", l_sSplit[5]);

            if (g_DYield.ContainsKey(l_sKey) == false)
            {
                g_DYield.Add(l_sKey, l_DExYield[lKey] / l_DExYield[l_sExKey]);
                g_DYieldCnt.Add(l_sKey, 1);
            }
            else
            {
                g_DYield[l_sKey] += l_DExYield[lKey] / l_DExYield[l_sExKey];
                g_DYieldCnt[l_sKey]++;
            }

        }

        foreach (String lKey in g_DYieldCnt.Keys)
        {
            g_DYield[lKey] /= g_DYieldCnt[lKey];
        }

    }

    public void initPositionData()
    {
        g_DYieldPos = new Dictionary<String, double>();
        g_DYieldCntPos = new Dictionary<String, int>();

        List<KeyValuePair<String, double>> l_LTempOrder = new List<KeyValuePair<String, double>>();

        for (int k = 0; k < g_OTrainingData.Length; k++)
        {

            String l_sKey = "";
            if (g_DMaterials.ContainsKey(g_OTrainingData[k].variety) == false)
            {
                continue;
            }

            if(k > 0 && ( g_OTrainingData[k].exID != g_OTrainingData[k-1].exID || g_OTrainingData[k].LOCCD != g_OTrainingData[k-1].LOCCD || g_OTrainingData[k].repno != g_OTrainingData[k-1].repno) )
            {
                l_LTempOrder.Sort(CompareDouble);
                for(int j=0;j<l_LTempOrder.Count;j++){

                    String l_sLocid = g_OTrainingData[k - 1].LOCCD.ToString();
                    String l_sYear = g_OTrainingData[k - 1].year.ToString();
                    String l_sPedigree = l_LTempOrder[j].Key;

                    // Year + locId + Pedigree
                    l_sKey = String.Concat("YLP;", l_sYear, ";", l_sLocid, ";", l_sPedigree);

                    if (g_DYieldPos.ContainsKey(l_sKey) == false)
                    {
                        g_DYieldPos.Add(l_sKey, j);
                        g_DYieldCntPos.Add(l_sKey, 1);
                    }
                    else
                    {
                        g_DYieldPos[l_sKey] += j;
                        g_DYieldCntPos[l_sKey] += 1;
                    }
                    
                    // locid + pedigree
                    l_sKey = String.Concat("LP;", l_sLocid, ";", l_sPedigree);

                    if (g_DYieldPos.ContainsKey(l_sKey) == false)
                    {
                        g_DYieldPos.Add(l_sKey, j);
                        g_DYieldCntPos.Add(l_sKey, 1);
                    }
                    else
                    {
                        g_DYieldPos[l_sKey] += j;
                        g_DYieldCntPos[l_sKey] += 1;
                    }

                    // pedigree
                    l_sKey = String.Concat("P;", l_sPedigree);

                    if (g_DYieldPos.ContainsKey(l_sKey) == false)
                    {
                        g_DYieldPos.Add(l_sKey, j);
                        g_DYieldCntPos.Add(l_sKey, 1);
                    }
                    else
                    {
                        g_DYieldPos[l_sKey] += j;
                        g_DYieldCntPos[l_sKey] += 1;
                    }

                }

                // Reset the list
                l_LTempOrder.Clear();
            } else 
            {
                l_LTempOrder.Add(new KeyValuePair<string,double>(g_DMaterials[g_OTrainingData[k].variety].pedigree.ToString(),g_OTrainingData[k].yield));
            }

        }

        foreach (String lKey in g_DYieldCntPos.Keys)
        {
            g_DYieldPos[lKey] /= g_DYieldCntPos[lKey];
        }

    }

    public void initAverageRM()
    {
        Dictionary<String, double> l_dAvRM = new Dictionary<string, double>();
        Dictionary<String, double> l_dAvRMcnt = new Dictionary<string, double>();

        g_DPedigreesRM = new Dictionary<string, double>();

        foreach (int lKey in g_DMaterials.Keys)
        {
            if (g_DMaterials[lKey].pedigree.Equals("NULL") == true || g_DMaterials[lKey].RM < 0)
            {
              
            }
            else
            {
                if (l_dAvRM.ContainsKey(g_DMaterials[lKey].pedigree) == false)
                {
                    l_dAvRM.Add(g_DMaterials[lKey].pedigree, g_DMaterials[lKey].RM);
                    l_dAvRMcnt.Add(g_DMaterials[lKey].pedigree, 1);
                }
                else
                {
                    l_dAvRM[g_DMaterials[lKey].pedigree] += g_DMaterials[lKey].RM;
                    l_dAvRMcnt[g_DMaterials[lKey].pedigree]++;
                }
            }
        }

        foreach (String lKey in l_dAvRMcnt.Keys)
        {
            l_dAvRM[lKey] /= l_dAvRMcnt[lKey];
            if (g_DPedigreesRM.ContainsKey(lKey) == false)
            {
                g_DPedigreesRM[lKey] = l_dAvRM[lKey];
            }
            else
            {
                Console.WriteLine("WHAT ??");
            }
        }

        foreach (int lKey in g_DMaterials.Keys)
        {
            if (l_dAvRM.ContainsKey(g_DMaterials[lKey].pedigree) == true)
            {
                g_DMaterials[lKey].avRM = l_dAvRM[g_DMaterials[lKey].pedigree];
            }
            else
            {
                g_DMaterials[lKey].avRM = -1;
            }
        }

    }

    public double getSimpleEstimation(String p_sLocid, String p_sDate, String p_sPedigree, int p_iDepth)
    {

        int l_iLocid = 1;
        int.TryParse(p_sLocid, out l_iLocid);

        String l_sMatBand = "";
        if (g_DLocations.ContainsKey(l_iLocid) == true)
        {
            l_sMatBand = g_DLocations[l_iLocid].maturityBand.ToString();
        }

        int l_iYear = 2009;
        if (p_sDate.Length > 4)
        {
            int.TryParse(p_sDate.Substring(0, 4), out l_iYear);
        }
        
        double ret1 = 0;
        double ret2 = 0;
        double ret3 = 0;
        String l_sKey = "";

        // year + locid + pedigree
        l_sKey = String.Concat("YLP;", l_iYear.ToString(), ";", l_iLocid.ToString(), ";", p_sPedigree);
        if (g_DYield.ContainsKey(l_sKey) == true)
        {
            ret1 = g_DYield[l_sKey];
        }

        // locid + pedigree
        l_sKey = String.Concat("LP;", l_iLocid.ToString(), ";", p_sPedigree);
        if (g_DYield.ContainsKey(l_sKey) == true)
        {
            ret2 = g_DYield[l_sKey] ;
        }

        // pedigree
        l_sKey = String.Concat("P;", p_sPedigree);
        if (g_DYield.ContainsKey(l_sKey) == true)
        {
            ret3 = g_DYield[l_sKey];
        }

        if (ret1 > 0)
        {
            return (ret1 + ret2 + ret3) / 3;
        }
        else if (ret2 > 0)
        {
            return (ret2 + ret3) / 2;
        } else {
            return ret3;
        }

        //Console.WriteLine(p_sPedigree);
        return 0;
    }

    public double getEstimationYLP(String p_sLocid, String p_sYear, String p_sPedigree)
    {

        double ret = 0;
        String l_sKey = "";

        // year + locid + pedigree
        l_sKey = String.Concat("YLP;", p_sYear, ";", p_sLocid, ";", p_sPedigree);
        if (g_DYield.ContainsKey(l_sKey) == true)
        {
            ret = g_DYield[l_sKey];
            return ret;
        }
        return 0;
    }

    public double getEstimationLP(String p_sLocid, String p_sYear, String p_sPedigree)
    {
        
        double ret = 0;
        String l_sKey = "";

        // locid + pedigree
        l_sKey = String.Concat("LP;", p_sLocid, ";", p_sPedigree);
        if (g_DYield.ContainsKey(l_sKey) == true)
        {
            ret = g_DYield[l_sKey];
            return ret;
        }
        return 0;
    }

    public double getEstimationP(String p_sLocid, String p_sYear, String p_sPedigree)
    {

        double ret = 0;
        String l_sKey = "";

        // pedigree
        l_sKey = String.Concat("P;", p_sPedigree);
        if (g_DYield.ContainsKey(l_sKey) == true)
        {
            ret = g_DYield[l_sKey];
            return ret;
        }
        return 0;
    }
 
#if HOME
    public string[] predictYield(String[] trainingData, String[] droughtMonitor, String[] droughtNOAA, String[] locations, String[] materials, String[] queries, String[] answers)
    {
#else
    public string[] predictYield(String[] trainingData, String[] droughtMonitor, String[] droughtNOAA, String[] locations, String[] materials, String[] queries)
    {
#endif
        Stopwatch stopwatch = Stopwatch.StartNew();
        g_AsTrainingData = trainingData;
        g_AsDroughtMonitor = droughtMonitor;
        g_AsDroughtNOAA = droughtNOAA;
        g_AsLocations = locations;
        g_AsMaterials = materials;
        g_AsQueries = queries;

#if HOME
        g_AsAnswers = answers;
#endif
        init();
        initRelativeData();
        initPositionData();
        initAverageRM();

        String[] ret = new String[queries.Length];

        // Get estimations
        for (int i = 0; i < queries.Length; i++)
        {
            String[] l_AsTempSplit = queries[i].Split(',');
            double[] l_AdEstimations = new double[36];
            double[] l_AdEstimationsBoth = new double[36];

            List<KeyValuePair<int, double>> l_LRelative = new List<KeyValuePair<int, double>>();
            List<KeyValuePair<int, double>> l_LRM = new List<KeyValuePair<int, double>>();

            for (int j = 2; j < 38; j++)
            {
                int l_iLocid = 1;
                String l_sLocid = l_AsTempSplit[0];
                int.TryParse(l_AsTempSplit[0], out l_iLocid);

                String l_sMatBand = "";
                if (g_DLocations.ContainsKey(l_iLocid) == true)
                {
                    l_sMatBand = g_DLocations[l_iLocid].maturityBand.ToString();
                }

                int l_iYear = 2009;
                if (l_AsTempSplit[1].Length > 4)
                {
                    int.TryParse(l_AsTempSplit[1].Substring(0, 4), out l_iYear);
                }
                String l_sYear = l_iYear.ToString();
                String l_sPedigree = l_AsTempSplit[j];

                l_AdEstimations[j - 2] = getSimpleEstimation(l_AsTempSplit[0], l_AsTempSplit[1], l_AsTempSplit[j], 0);
                l_LRelative.Add(new KeyValuePair<int, double>(j - 2, l_AdEstimations[j - 2]));
                
                double avRM = -1;
                if (g_DPedigreesRM.ContainsKey(l_AsTempSplit[j]) == true)
                {
                    avRM = g_DPedigreesRM[l_AsTempSplit[j]];
                }
                l_LRM.Add(new KeyValuePair<int, double>(j - 2, avRM));
                
            }

            l_LRelative.Sort(CompareIntDouble);
            l_LRM.Sort(CompareIntDouble);

            for (int j = 0; j < l_LRelative.Count; j++)
            {
                if (l_LRelative[j].Value > 0)
                {
                    l_AdEstimationsBoth[l_LRelative[j].Key] = Math.Round(l_LRelative[j].Value*35)*100;
                }
            }
            
            for (int j = 0; j < l_LRM.Count; j++)
            {
                l_AdEstimationsBoth[l_LRM[j].Key] += j;
            }

            String lRet = "";
            for (int j = 0; j < 36; j++)
            {
                if (j == 0)
                {
                    lRet = Math.Round(l_AdEstimationsBoth[j]).ToString();
                }
                else
                {
                    lRet = String.Concat(lRet, ",", Math.Round(l_AdEstimationsBoth[j]).ToString());
                }
            }

            ret[i] = lRet;
            
        }

        stopwatch.Stop();
        Console.WriteLine("Time " + stopwatch.Elapsed);

        return ret;
    }
}
