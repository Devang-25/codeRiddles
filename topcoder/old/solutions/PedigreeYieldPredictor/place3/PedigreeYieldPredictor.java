import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.util.*;

public class PedigreeYieldPredictor {

    public static final int f = 20;
    public double garm = 0.03;
    public static final double lambda = 0.01;
    public static final double fuck = 100;
    public static final int part_tms = 60;
    public static final int tms = 70;
    public static final int Lozy = 54325432;
    static Random rand = new Random(Lozy);
    public static final int neg_sample = 4;
    private static final boolean submit = true;
    private static final double GAP = sigmoid(5) - 0.5;

    long sTime;

    class Train {
        int t1p, t2p, kk, ty, tl;
        double real;

        public Train(DataRecord t1, DataRecord t2) {
            t1p = t1.pedigree;
            t2p = t2.pedigree;
            kk = t1.loccd * 30 + t1.year;
            ty = t1.year;
            tl = t1.loccd;
            real = sigmoid(t2.yield - t1.yield);
        }

        public void train() {
            if (abs(real - 0.5) < GAP)
                return;
            double tmp = ped_bias[t2p] - ped_bias[t1p];
            double[] a = p[kk], b = q[t2p], c = q[t1p], d = p_year[ty], pl = p_loc[tl];
            for (int k = 0; k < f; ++k)
                tmp += (a[k] + d[k] + pl[k]) * (b[k] - c[k]);
            tmp = sigmoid(tmp);
            // double real = sigmoid((t2.yield - t1.yield) * fuck
            // / (t2.yield + t1.yield));
            double e = (tmp - real);
            double gg = e * tmp * (1 - tmp);
            ped_bias[t2p] -= garm * gg;
            ped_bias[t1p] += garm * gg;
            for (int k = 0; k < f; ++k) {
                double x = b[k] - c[k], y = a[k] + d[k] + pl[k];
                double x1 = a[k] - garm * (gg * x + lambda * a[k]), x2 = d[k]
                        - garm * (gg * x + lambda * d[k]), x3 = pl[k] - garm
                        * (gg * x + lambda * pl[k]), x4 = b[k] - garm
                        * (gg * y + lambda * b[k]), x5 = c[k] + garm
                        * (gg * y - lambda * c[k]);
                a[k] = x1;
                d[k] = x2;
                pl[k] = x3;
                b[k] = x4;
                c[k] = x5;
            }
        }
    }

    class DataRecord {
        int eid, loccd, year;
        double yield;
        int pedigree;

        public DataRecord(String str) {
            String[] res = str.trim().split(",");
            // eid = toInt(res[0]);
            loccd = 0;
            pedigree = 0;
            if (locId.containsKey(toInt(res[1])))
                loccd = locId.get(toInt(res[1]));
            // rep = toInt(res[2]);
            // mid = toInt(res[3]);
            if (mm_ped.containsKey(toInt(res[3])))
                pedigree = mm_ped.get(toInt(res[3]));
            yield = toDouble(res[4]);
            // mr = toInt(res[5]);
            year = getYear(res[6]);
        }
    }

    class ASK {
        int loccd, year;
        int rnk[] = new int[36];
        String pedigree[] = new String[36];
        double rights[] = new double[36];

        public ASK(String s) {
            String res[] = s.trim().split(",");
            loccd = Integer.parseInt(res[0]);
            year = getYear(res[1]);
            System.arraycopy(res, 2, pedigree, 0, 36);
            if (!submit) {
                for (int i = 0; i < 36; ++i) {
                    rights[i] = Double.valueOf(res[38 + i]);
                }
            }
        }

        public double[] local_ans() {
            double[] res = new double[36];
            for (int i = 0; i < 36; ++i) {
                res[i] = prid(loccd, year, pedigree[i]);
            }
            return res;
        }

        public String answer() {
            double[] res = new double[36];
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < 36; ++i) {
                res[i] = prid(loccd, year, pedigree[i]);
            }
            for (int i = 0; i < 36; ++i) {
                double a = res[i];
                for (int j = 0; j < 36; ++j) {
                    if (a >= res[j]) {
                        ++rnk[i];
                    }
                }
            }
            for (int i = 0; i < 36; ++i) {
                sb.append(String.valueOf(rnk[i]));
                if (i != 35)
                    sb.append(",");
            }
            return sb.toString();
        }
    }

    HashMap<String, int[]> ped_mm; // ped -> mid, herb
    HashMap<Integer, Integer> mm_ped; // mid -> ped
    HashMap<String, Integer> pedigreeId;
    HashMap<Integer, Integer> locId;

    int[] order = null;

    String[] trainingData, droughtMonitor, droughtNOAA, locations, material,
            reps;
    int numTrain, numMat, numReps, numLoc;

    double[] ped_bias, loc_bias, year_bias;
    double[][] p, q;// p: loc * year, q: ped
    double[][] p_year, p_loc;

    DataRecord[] trainData = null;

    public String[] predictYield(String[] trainingData,
            String[] droughtMonitor, String[] droughtNOAA, String[] locations,
            String[] material, String[] reps) {
        sTime = System.currentTimeMillis();
        this.trainingData = trainingData;
        this.droughtMonitor = droughtMonitor;
        this.droughtNOAA = droughtNOAA;
        this.locations = locations;
        this.material = material;
        this.reps = reps;

        numTrain = trainingData.length;
        numMat = material.length;
        numReps = reps.length;
        numLoc = locations.length;

        trainData = new DataRecord[numTrain];
        print("begin init");
        init();
        print("finish init");
        debug(numTrain, numMat, numReps, numLoc);
        // train
        make();
        for (int i = 0; i < tms; ++i) {
            if (i == 20)
                garm = 0.01;
            if (i >= part_tms)
                garm /= 1.05;
            Collections.shuffle(model_key, rand);
            train();
            if (!submit)
                System.out.printf("round %d:\t%.2f\t%.2fs\n", i, evaluate(),
                        getTime());
            else
                debug(i, getTime());
        }
        print("\n");

        // get answer
        String[] res = new String[numReps];
        for (int i = 0; i < numReps; ++i) {
            ASK ask = new ASK(reps[i]);
            res[i] = ask.answer();
            // debug(res[i]);
        }
        return res;
    }

    private double cmp(double a, double b) {
        if (a < b)
            return 0;
        if (a > b)
            return 1;
        return 0.5;
    }

    private double evaluate() {
        double res = 0;
        for (int k = 0; k < numReps; ++k) {
            ASK ask = new ASK(reps[k]);
            double[] tmp = ask.local_ans();
            double q = 0;
            for (int i = 0; i < 36; ++i) {
                for (int j = i + 1; j < 36; ++j) {
                    double real_i = ask.rights[i], real_j = ask.rights[j], pr_i = tmp[i], pr_j = tmp[j];
                    double cmp_real = cmp(real_i, real_j), cmp_pr = cmp(pr_i,
                            pr_j);
                    if (cmp_real == 0.5 || cmp_pr == 0.5)
                        q += 0.5;
                    else
                        q += 1 - abs(cmp_real - cmp_pr);
                }
            }
            q = q / (35 * 36);
            res += q;
        }
        res /= numReps;
        return res * 2000000;
    }

    private void train() {
        for (int i = 0; i < model_key.size(); ++i) {
            // if (trainData[i].loccd != trainData[i + 1].loccd)
            // continue;
            model_key.get(i).train();
        }
    }

    List<Train> model_key = new ArrayList<Train>();

    private void make() {
        int i = 0;
        while (i < numTrain) {
            int old = i;
            int tmp = trainData[i].loccd, yr = trainData[i].year;
            while (i < numTrain && tmp == trainData[i].loccd
                    && yr == trainData[i].year) {
                ++i;
            }
            model_key.addAll(give(old, i));
            // debug(old, i);
        }
    }

    private ArrayList<Train> give(int begin, int end) {
        int gap = end - begin;
        ArrayList<Train> res = new ArrayList<Train>();
        for (int i = begin; i < end; ++i) {
            for (int j = 0; j < neg_sample; ++j) {
                res.add(new Train(trainData[i], trainData[rand.nextInt(gap)
                        + begin]));
            }
        }
        return res;
    }

    public double prid(int loccd, int year, String ped) {
        int loc = 0, pedi = 0;
        Integer tmp = locId.get(loccd);
        if (tmp != null)
            loc = tmp;
        tmp = pedigreeId.get(ped);
        if (tmp != null)
            pedi = tmp;
        double res = ped_bias[pedi];
        double[] a = p[loc * 30 + year], b = q[pedi], c = p_year[year], d = p_loc[loc];
        for (int i = 0; i < f; ++i)
            res += (a[i] + c[i] + d[i]) * b[i];
        return res;
    }

    private void init() {
        // loccd
        locId = new HashMap<Integer, Integer>();
        int loc_id = 0;
        for (int i = 0; i < numLoc; ++i) {
            Integer tmp = Integer.valueOf(locations[i].split(",")[0]);
            if (!locId.containsKey(tmp)) {
                locId.put(tmp, ++loc_id);
            }
        }
        numLoc = locId.size() + 1;
        // material TODO just use the pedigree
        pedigreeId = new HashMap<String, Integer>();
        mm_ped = new HashMap<Integer, Integer>();
        int ped_id = 0;
        for (int i = 0; i < numMat; ++i) {
            String[] res = material[i].trim().split(",");
            String tmp = res[1];
            if (!pedigreeId.containsKey(tmp)) {
                pedigreeId.put(tmp, ++ped_id);
            }
            mm_ped.put(Integer.valueOf(res[0]), pedigreeId.get(tmp));
        }
        numMat = pedigreeId.size() + 1;

        ped_bias = new double[numMat];
        for (int i = 0; i < numMat; ++i)
            ped_bias[i] = uniform();
        loc_bias = new double[numLoc];
        for (int i = 0; i < numLoc; ++i)
            loc_bias[i] = uniform();
        year_bias = new double[30];
        for (int i = 0; i < 30; ++i)
            year_bias[i] = uniform();
        p = new double[numLoc * 30][f];
        q = new double[numMat][f];
        p_year = new double[30][f];
        p_loc = new double[numLoc][f];
        for (int i = 0; i < numLoc; ++i) {
            for (int j = 0; j < f; ++j) {
                p_loc[i][j] = uniform();
            }
        }
        for (int i = 0; i < 30; ++i) {
            for (int j = 0; j < f; ++j) {
                p_year[i][j] = uniform();
            }
        }
        for (int i = 0; i < p.length; ++i) {
            for (int j = 0; j < f; ++j) {
                p[i][j] = uniform();
            }
        }
        for (int i = 0; i < q.length; ++i) {
            for (int j = 0; j < f; ++j) {
                q[i][j] = uniform();
            }
        }
        for (int i = 0; i < numTrain; ++i) {
            trainData[i] = new DataRecord(trainingData[i]);
        }
    }

    static final double uniform() {
        return rand.nextDouble() - 0.5;
    }

    static final int toInt(String s) {
        if (s.equalsIgnoreCase("null"))
            return -1;
        return Integer.parseInt(s);
    }

    static final double toDouble(String s) {
        if (s.equalsIgnoreCase("null"))
            return -1;
        return Double.parseDouble(s);
    }

    static final int parseHerbType(String s) {
        if (s.equalsIgnoreCase("conv"))
            return 1;
        if (s.equalsIgnoreCase("rr1"))
            return 2;
        if (s.equalsIgnoreCase("rr2y"))
            return 3;
        return 0;
    }

    static final int getYear(String str) {
        if (str.equalsIgnoreCase("null"))
            return 0;
        String[] s = str.trim().split("-");
        return Integer.parseInt(s[0]) - 1990;
    }

    static final double sigmoid(double x) {
        return 1 / (1 + exp(-x));
    }

    static final void debug(Object... os) {
        System.err.println(deepToString(os));
    }

    static final void print(String s) {
        System.out.println(s);
    }

    double getTime() {
        return (System.currentTimeMillis() - sTime) * 1e-3;
    }
}
