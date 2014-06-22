import java.io.*; 

class ExampleClass
{
    public ExampleClass()
    {
        // constructor
    }

    public void methodOne()
    {
        System.out.println("In method 1");
    }

    public void methodTwo()
    {
        System.out.println("In method 2");
    }

    public void methodThree()
    {
        System.out.println("In method 3");
    }
}

public class Driver
{
    public static void main(String[] args)
    {
        ExampleClass ex = new ExampleClass();
        ex.methodOne();
        ex.methodTwo();
        ex.methodThree();
    }
}

