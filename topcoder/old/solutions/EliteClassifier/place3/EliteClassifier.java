/**
 * TopCoder Soybean Oracle Series
 * Soybean Marathon Match 1
 * Wladimir Leite (wleite)
 * 01.06.2012 - 01.20.2012
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class EliteClassifier {
    static Map<Integer, Double> yieldWeightPerArea = new HashMap<Integer, Double>();
    static Map<Integer, Double> maturityWeightPerArea = new HashMap<Integer, Double>();

    static {
        fillMap(yieldWeightPerArea, "0=0.6, 1=1.4, 2=1.3, 3=1.3, 4=1.3, 5=1.4, 6=0.8, 7=0.5, 8=1.2, 9=1.0, 10=1.0");
        fillMap(maturityWeightPerArea, "0=-1.4, 1=-1.3, 2=-1.3, 3=-0.8, 4=-0.8, 5=-0.5, 6=-0.5, 7=-1.3, 8=-0.7, 9=-0.8, 10=-0.8");
    }

    public EliteClassifier() {
        Experiment.purge();
        Variety.purge();
    }

    public int[] classify(String[] expData, String[] locData) {
        Set<Experiment> experiments = getExperiments(expData);
        getLocations(locData);
        for (Experiment experiment : experiments) {
            analyseExperiment(experiment);
        }
        List<Variety> orderedVarieties = sortVarieties(experiments);
        return mountVarietiesIdArray(orderedVarieties);
    }

    private void analyseExperiment(Experiment experiment) {
        Set<Variety> varieties = experiment.getVarieties();
        for (Variety testVariety : varieties) {
            if (testVariety.isCheck()) continue;
            double val = 0;
            Set<Trial> testTrials = testVariety.getTrials();

            List<Double> difYield = new ArrayList<Double>();
            List<Double> difMaturity = new ArrayList<Double>();
            for (Variety checkVariety : varieties) {
                if (!checkVariety.isCheck()) continue;
                Set<Trial> checkTrials = checkVariety.getTrials();
                for (Trial testTrial : testTrials) {
                    for (Trial checkTrial : checkTrials) {
                        if (testTrial.getLoccd() != checkTrial.getLoccd()) continue;
                        if (testTrial.getRepetition() != checkTrial.getRepetition()) continue;
                        if (testTrial.getYield() > 0 && checkTrial.getYield() > 0) {
                            difYield.add(getYieldWeight(testTrial.getLoccd()) * (testTrial.getYield() - checkTrial.getYield()));
                        }
                        if (testTrial.getMaturiryNumber() > 0 && checkTrial.getMaturiryNumber() > 0) {
                            difMaturity.add(getMaturityWeight(testTrial.getLoccd()) * (testTrial.getMaturiryNumber() - checkTrial.getMaturiryNumber()));
                        }
                    }
                }
            }
            Collections.sort(difYield);
            Collections.sort(difMaturity);
            for (int i = 0; i < difYield.size() - 1; i++) {
                val += difYield.get(i);
            }
            if (difYield.size() > 0) val += difYield.get(0) * 4;

            for (int i = difMaturity.size() - 1; i >= 0; i--) {
                val += difMaturity.get(i);
            }

            if (testVariety.getType().equals(VarietyType.RR1)) val += 100;
            if (difMaturity.size() <= 2) val -= 200;
            else if (difMaturity.size() <= 4) val -= 150;
            else if (difMaturity.size() <= 6) val -= 100;
            else if (difMaturity.size() <= 8) val -= 10;

            if (experiment.getYear() == 2002) val *= 4;
            if (experiment.getYear() == 2003) val *= 3;

            testVariety.setEliteScore(val);
        }
    }

    static double getYieldWeight(int loccd) {
        Location location = Location.getLocationByCode(loccd);
        if (location == null) return 1;
        Double val = yieldWeightPerArea.get(location.getAreaCode());
        return val == null ? 1 : val;
    }

    static double getMaturityWeight(int loccd) {
        Location location = Location.getLocationByCode(loccd);
        if (location == null) return 1;
        Double val = maturityWeightPerArea.get(location.getAreaCode());
        return val == null ? -0.8 : val;
    }

    private int[] mountVarietiesIdArray(List<Variety> varieties) {
        int[] ret = new int[varieties.size()];
        for (int i = 0; i < ret.length; i++) {
            ret[i] = varieties.get(i).getId();
        }
        return ret;
    }

    private List<Variety> sortVarieties(Set<Experiment> experiments) {
        List<Variety> allVarieties = new ArrayList<Variety>();
        for (Experiment exp : experiments) {
            List<Variety> expVarieties = new ArrayList<Variety>(exp.getVarieties());
            Collections.sort(expVarieties);
            for (int i = 0; i < expVarieties.size(); i++) {
                Variety v = expVarieties.get(i);
                if (v.isCheck()) break;
                v.setEliteScore(v.getEliteScore() - i * 30);
            }
            allVarieties.addAll(exp.getVarieties());
        }
        Collections.sort(allVarieties);
        return allVarieties;
    }

    public static List<DataRecord> parseData(String[] data) {
        List<DataRecord> dataRecords = new ArrayList<DataRecord>();
        for (int i = 0; i < data.length; i++) {
            dataRecords.add(new DataRecord(data[i]));
        }
        return dataRecords;
    }

    public static Set<Experiment> getExperiments(String[] data) {
        List<DataRecord> dataRecords = parseData(data);
        Set<Experiment> experiments = new HashSet<Experiment>();
        for (DataRecord d : dataRecords) {
            Experiment experiment = Experiment.getExperimentById(d.getExperimentId());
            if (experiment == null) {
                experiment = new Experiment(d.getExperimentId(), d.getYear());
                experiments.add(experiment);
            }
            Set<Variety> varieties = experiment.getVarieties();
            Variety variety = Variety.getVarietyById(d.getVarietyId());
            if (variety == null) {
                variety = new Variety(d.getVarietyId(), d.getIsCheck() == 1, d.getIsElite() == 1, d.getType() == 1 ? VarietyType.CONV
                        : d.getType() == 2 ? VarietyType.RR1 : d.getType() == 3 ? VarietyType.RR2Y : VarietyType.UNKNOWN, d.getRelativeMaturity());
                varieties.add(variety);
            }
            Set<Trial> trials = variety.getTrials();
            Trial trial = new Trial(d.getLoccd(), d.getRep(), d.getYield(), d.getMaturiryNumber());
            trials.add(trial);
        }
        return experiments;
    }

    public static Set<Location> getLocations(String[] data) {
        Set<Location> locations = new HashSet<Location>();
        for (int i = 0; i < data.length; i++) {
            locations.add(new Location(data[i]));
        }
        return locations;
    }

    private static void fillMap(Map<Integer, Double> map, String a) {
        String[] b = a.split(", ");
        for (String c : b) {
            String[] d = c.split("=");
            map.put(Integer.parseInt(d[0]), Double.parseDouble(d[1]));
        }
    }
}

class Experiment {
    private final int id;
    private final int year;
    private final Set<Variety> varieties = new HashSet<Variety>();
    private static final Map<Integer, Experiment> knownExperiments = new HashMap<Integer, Experiment>();

    public Experiment(int id, int year) {
        this.id = id;
        this.year = year;
        knownExperiments.put(id, this);
    }

    public static void purge() {
        knownExperiments.clear();
    }

    public static Experiment getExperimentById(int id) {
        return knownExperiments.get(id);
    }

    public int hashCode() {
        return id;
    }

    public int getId() {
        return id;
    }

    public int getYear() {
        return year;
    }

    public Set<Variety> getVarieties() {
        return varieties;
    }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Experiment other = (Experiment) obj;
        if (id != other.id) return false;
        return true;
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("Experiment [id=");
        builder.append(id);
        builder.append(", year=");
        builder.append(year);
        builder.append(", varieties=");
        builder.append(varieties);
        builder.append("]");
        return builder.toString();
    }
}

class Variety implements Comparable<Variety> {
    private final int id;
    private final boolean check;
    private final boolean elite;
    private final VarietyType type;
    private final double relativeMaturity;
    private double eliteScore;
    private final Set<Trial> trials = new HashSet<Trial>();

    private static final Map<Integer, Variety> knownVarieties = new HashMap<Integer, Variety>();

    public Variety(int id, boolean check, boolean elite, VarietyType type, double relativeMaturity) {
        this.id = id;
        this.check = check;
        this.elite = elite;
        this.type = type;
        this.relativeMaturity = relativeMaturity;
        knownVarieties.put(id, this);
    }

    public static void purge() {
        knownVarieties.clear();
    }

    public static Variety getVarietyById(int id) {
        return knownVarieties.get(id);
    }

    public Set<Trial> getTrials() {
        return trials;
    }

    public int hashCode() {
        return id;
    }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Variety other = (Variety) obj;
        if (id != other.id) return false;
        return true;
    }

    public int getId() {
        return id;
    }

    public boolean isCheck() {
        return check;
    }

    public boolean isElite() {
        return elite;
    }

    public VarietyType getType() {
        return type;
    }

    public double getRelativeMaturity() {
        return relativeMaturity;
    }

    public double getEliteScore() {
        return eliteScore;
    }

    public void setEliteScore(double eliteScore) {
        this.eliteScore = eliteScore;
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("Variety [id=");
        builder.append(id);
        builder.append(", check=");
        builder.append(check);
        builder.append(", elite=");
        builder.append(elite);
        builder.append(", type=");
        builder.append(type);
        builder.append(", relativeMaturity=");
        builder.append(relativeMaturity);
        builder.append(", eliteScore=");
        builder.append(eliteScore);
        builder.append("]");
        return builder.toString();
    }

    public int compareTo(Variety o) {
        if (isCheck() && !o.isCheck()) return 1;
        if (!isCheck() && o.isCheck()) return -1;
        if (getEliteScore() > o.getEliteScore()) return -1;
        if (getEliteScore() < o.getEliteScore()) return 1;
        return 0;
    }
}

class Trial {
    private final int loccd;
    private final int repetition;
    private final double yield;
    private final double maturiryNumber;

    public Trial(int loccd, int repetition, double yield, double maturiryNumber) {
        this.loccd = loccd;
        this.repetition = repetition;
        this.yield = yield;
        this.maturiryNumber = maturiryNumber;
    }

    public int hashCode() {
        return (loccd << 8) | repetition;
    }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Trial other = (Trial) obj;
        if (loccd != other.loccd) return false;
        if (repetition != other.repetition) return false;
        return true;
    }

    public int getLoccd() {
        return loccd;
    }

    public int getRepetition() {
        return repetition;
    }

    public double getYield() {
        return yield;
    }

    public double getMaturiryNumber() {
        return maturiryNumber;
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("Trial [loccd=");
        builder.append(loccd);
        builder.append(", repetition=");
        builder.append(repetition);
        builder.append(", yield=");
        builder.append(yield);
        builder.append(", maturiryNumber=");
        builder.append(maturiryNumber);
        builder.append("]");
        return builder.toString();
    }
}

enum VarietyType {
    CONV, RR1, RR2Y, UNKNOWN;
}

class DataRecord {
    private int experimentId; //Each experiment has a different ID.
    private int year; //Year in which the experiment was ran. 
    private int loccd; //You can refer to Locations.csv to obtain additional information about each location. Please note that such information is not available for all locations.
    private int rep; //Number of the repetition of one trial.  
    private int type; //1-conv (Conventional), 2-RR1 (Roundup Ready) or 3-RR2Y (Roundup Ready to Yield).
    private int varietyId; //ID of the variety within experiment. 
    private double yield; //Yield of a variety given in bushels per acre.
    private double maturiryNumber; //Maturity number of a variety.
    private double relativeMaturity; //Relative maturity of a variety. It's given in case it's available and the variety is a check.
    private int isCheck; //1 if a variety is a check, 0 otherwise
    private int isElite; //1 if a variety is an elite, 0 otherwise. Check/Elite statuses are exclusive - only one can be true.
    private String str; //Original String.

    public DataRecord(String str) {
        String[] s = str.trim().split("\\,");
        init(toInt(s[0]), toInt(s[1]), toInt(s[2]), toInt(s[3]), parseType(s[4]), toInt(s[5]), toDouble(s[6]), toDouble(s[7]), toDouble(s[8]), toInt(s[9]),
                s.length == 10 ? -1 : toInt(s[10]), str);
    }

    private void init(int experimentId, int year, int loccd, int rep, int type, int varietyId, double yield, double mn, double rm, int isCheck, int isElite,
            String str) {
        this.str = str;
        this.experimentId = experimentId;
        this.year = year;
        this.loccd = loccd;
        this.rep = rep;
        this.type = type;
        this.varietyId = varietyId;
        this.yield = yield;
        this.maturiryNumber = mn;
        this.relativeMaturity = rm;
        this.isCheck = isCheck;
        this.isElite = isElite;
    }

    public int getExperimentId() {
        return experimentId;
    }

    public int getYear() {
        return year;
    }

    public int getLoccd() {
        return loccd;
    }

    public int getRep() {
        return rep;
    }

    public int getType() {
        return type;
    }

    public int getVarietyId() {
        return varietyId;
    }

    public double getYield() {
        return yield;
    }

    public double getMaturiryNumber() {
        return maturiryNumber;
    }

    public double getRelativeMaturity() {
        return relativeMaturity;
    }

    public int getIsCheck() {
        return isCheck;
    }

    public int getIsElite() {
        return isElite;
    }

    public String getStr() {
        return str;
    }

    private static final int parseType(String s) {
        if (s.equalsIgnoreCase("conv")) return 1;
        if (s.equalsIgnoreCase("rr1")) return 2;
        if (s.equalsIgnoreCase("rr2y")) return 3;
        return -1;
    }

    private static final int toInt(String s) {
        if (s.equalsIgnoreCase("null")) return -1;
        return Integer.parseInt(s);
    }

    private static final double toDouble(String s) {
        if (s.equalsIgnoreCase("null")) return -1;
        return Double.parseDouble(s);
    }
}

class Location {
    private final int loccd; //Location code.
    private final int maturityBand; //"Row" position on the map.
    private final int maturitySubband; //There are only 3 different values : Early, Mid & Late.
    private final int maturityZone; //"Column" position on the map.
    private String str; //Original String.
    private static final Map<Integer, Location> knownLocations = new HashMap<Integer, Location>();

    public Location(String str) {
        String[] s = str.trim().split("\\,");
        this.loccd = toInt(s[0]);
        this.maturityBand = toInt(s[1]);
        this.maturitySubband = parseSubband(s[2]);
        this.maturityZone = toInt(s[3]);
        this.str = str;
        knownLocations.put(loccd, this);
    }

    public int getLoccd() {
        return loccd;
    }

    public int getMaturityBand() {
        return maturityBand;
    }

    public int getMaturitySubband() {
        return maturitySubband;
    }

    public int getMaturityZone() {
        return maturityZone;
    }

    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }

    public int hashCode() {
        return loccd;
    }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Location other = (Location) obj;
        if (loccd != other.loccd) return false;
        return true;
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("Location [loccd=");
        builder.append(loccd);
        builder.append(", maturityBand=");
        builder.append(maturityBand);
        builder.append(", maturitySubband=");
        builder.append(maturitySubband);
        builder.append(", maturityZone=");
        builder.append(maturityZone);
        builder.append("]");
        return builder.toString();
    }

    private static final int parseSubband(String s) {
        if (s.equalsIgnoreCase("early")) return 1;
        if (s.equalsIgnoreCase("mid")) return 2;
        if (s.equalsIgnoreCase("late")) return 3;
        return -1;
    }

    private static final int toInt(String s) {
        return Integer.parseInt(s);
    }

    public int getAreaCode() {
        return maturityBand;
    }

    public static Location getLocationByCode(int loccd) {
        return knownLocations.get(loccd);
    }

    public static void purge() {
        knownLocations.clear();
    }
}
