class Job
{
    private String jobTitle;
    Job (String jobTitle)
    {
	this.jobTitle = jobTitle;
    }
    public String toString ()
    {
	return jobTitle;
    }
}
class Employee
{
    private String name;
    private Job [] jobs;
    private int jobIndex = 0;
    Employee (String name, Job [] jobs)
    {
	this.name = name;
	this.jobs = jobs;
    }
    String getName ()
    {
	return name;
    }
    boolean hasMoreJobs ()
    {
	return jobIndex < jobs.length;
    }
    Job nextJob ()
    {
	return !hasMoreJobs () ? null : jobs [jobIndex++];
    }
}
class JobIterator1
{
    public static void main (String [] args)
    {
	Job [] jobs = { new Job ("Janitor"), new Job ("Delivery Person") };
	Employee e = new Employee ("John Doe", jobs);
	System.out.println (e.getName () + " works the following jobs:\n");
	while (e.hasMoreJobs ())
	    System.out.println (e.nextJob ());
    }
}
