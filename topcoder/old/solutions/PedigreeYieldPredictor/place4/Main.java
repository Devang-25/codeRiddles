package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Random;

public class Main {
	public static void main(String[] args) throws Exception {
		boolean usevalid = true;
		String dir="D:/TC/marathon/PedigreeYieldPredictor/";
		String tempString = null;
		
		File file = null;
		BufferedReader reader = null;
		LinkedList<String> buffer = new LinkedList<String>();
		int line = 0;
		
		
		System.out.println("read 0!");
		line = 0;
		if (usevalid) file =new File(dir + "valid_trainingData.csv");
		else file =new File(dir + "DataTraining.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] trainingData = new String[line];
		if (usevalid) file =new File(dir + "valid_trainingData.csv");
		else file =new File(dir + "DataTraining.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			trainingData[i] = tempString;
		}
		
		System.out.println("read 1!");
		line = 0;
		file =new File(dir + "DroughtMonitor.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] droughtMonitor = new String[line];
		file =new File(dir + "DroughtMonitor.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			droughtMonitor[i] = tempString;
		}
		
		System.out.println("read 2!");
		line = 0;
		file =new File(dir + "DroughtNOAA.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] droughtNOAA = new String[line];
		file =new File(dir + "DroughtNOAA.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			droughtNOAA[i] = tempString;
		}
		
		System.out.println("read 3!");
		line = 0;
		file =new File(dir + "Locations.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] locations = new String[line];
		file =new File(dir + "Locations.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			locations[i] = tempString;
		}
		
		System.out.println("read 4!");
		line = 0;
		file =new File(dir + "Material.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] Material = new String[line];
		file =new File(dir + "Material.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			Material[i] = tempString;
		}
		
		System.out.println("read 5!");
		line = 0;
		if (usevalid) file =new File(dir + "valid_queries.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] queries = new String[line];
		if (usevalid) file =new File(dir + "valid_queries.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			queries[i] = tempString;
		}
		
		System.out.println("read 6!");
		line = 0;
		file =new File(dir + "ValidReps.csv");
		reader = new BufferedReader(new FileReader(file));
		while ((tempString = reader.readLine())!=null && !tempString.equals("")){
			line++;
		}
		String[] ValidReps = new String[line];
		file =new File(dir + "ValidReps.csv");
		reader = new BufferedReader(new FileReader(file));
		for (int i=0;i<line;i++){
			tempString = reader.readLine();
			ValidReps[i] = tempString;
		}
		
		System.out.println("read OK!");
		
		if (!usevalid){
			///*
			java.io.FileOutputStream outf = new java.io.FileOutputStream(dir+"valid_trainingData.csv", false);
			java.io.PrintStream outp = new java.io.PrintStream(outf);
			
			java.io.FileOutputStream outf2 = new java.io.FileOutputStream(dir+"valid_queries.csv", false);
			java.io.PrintStream outp2 = new java.io.PrintStream(outf2);
			
			HashMap<Integer,String> pedigree = new HashMap<Integer,String>();
	        
	        for (int i=0;i<Material.length;i++){
	        	String[] label =Material[i].split(",");
	        	pedigree.put(Integer.parseInt(label[0]),label[1]);
	        	
	        }
						
			Random random = new Random();
			
			LinkedList<String> testData = new LinkedList<String>();
			HashSet<Integer> testExp = new HashSet<Integer>();
			for (int i=0;i<500;i++){
				int index = Math.abs(random.nextInt())% ValidReps.length;
				testData.add(ValidReps[index]);
				String[] labels = ValidReps[index].split(",");
				testExp.add(Integer.parseInt(labels[0]));
			}
			
			String[] real = null;
			int last=0;
			int count = 0;
			String lasts ="";
			for (int i=0;i<trainingData.length;i++){
				String[] labels = trainingData[i].split(",");
				String now = labels[0]+","+labels[1]+","+labels[2];
				
				if (testData.contains(now)){
					if (last==0 || !lasts.equals(now)) {
						if (last==1) {
							for (int a=0;a<count;a++) outp2.print(","+real[a]);
							outp2.println();
						}
						System.out.println(now);
						outp2.print(labels[1]+","+labels[6]);
						real = new String[36];
						count=0;
					}
					last = 1;
					outp2.print(","+pedigree.get(Integer.parseInt(labels[3])));
					real[count] = labels[4];
					count++;
				}else{
					if (last==1){
						for (int a=0;a<count;a++) outp2.print(","+real[a]);
						outp2.println();
					}
					last = 0;
					String[] labels2 = trainingData[i].split(",");
					if (!testExp.contains(Integer.parseInt(labels2[0])))
						outp.println(trainingData[i]);
				}
				lasts = now;
			}
			if (last==1){
				for (int a=0;a<count;a++) outp2.print(","+real[a]);
				outp2.println();
			}
			
			outp.close();
			outp2.close();
			//*/
		}else{
			///*
			PedigreeYieldPredictor Model = new PedigreeYieldPredictor();
			String[] results =  Model.predictYield(trainingData, droughtMonitor, droughtNOAA, locations, Material, queries);
			
			System.out.println("Evaluate Begin!");
	
			if (results.length!=queries.length) System.out.println("error");
			
			//evaluate
			double score = 0;
			for (int c=0;c<queries.length;c++){
				String[] labels = results[c].split(",");
				if (labels.length!=36) System.err.println("error! result not 36!");
				double[] pred = new double[36]; 
				for (int t=0;t<36;t++) pred[t] = Double.parseDouble(labels[t]);
				
				labels = queries[c].split(",");
				double[] real = new double[36]; 
				for (int t=0;t<36;t++) real[t] = Double.parseDouble(labels[t+38]);
				
				double q=0;
				for (int i=0;i<36;i++)
					for (int j=i+1;j<36;j++){
						double c_real = comp(real[i],real[j]);
						double c_pred = comp(pred[i],pred[j]);
						if (c_real==0.5 || c_pred==0.5) q += 0.5;
						else q += 1.0 - Math.abs(c_real - c_pred);
					}
				q =2*q/(35*36);
				System.out.println("test case "+(c+1)+" score: "+q);
				score +=q;
				
			}
			score /= queries.length;
			System.out.println("avg_result: "+score + " SCORE: "+(1000000.0*score));
			
		}
	}
	
	static double comp(double a,double b){
		if (a<b) return 0;
		if (a>b) return 1;
		return 0.5;
	}
}
