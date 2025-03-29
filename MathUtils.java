public class MathUtils {

    public int add(int a , int b)
    {
        // returns the sum of the values
        return a + b;
    }

    public int subtract(int a , int b)
    {
        // returns the the difference
        return a - b;
    }

    public int multiply(int a , int b)
    {
        // returns the solution
        return a * b;
    }

    public double divide(int a , int b)
    {
        //branch checking if the divisor is 0
        // if divisor is 0, -1 is returned
        if(b == 0 )
            return -1.0;
        // casts the quotient as double and returns it
        return (double) a / b;
    }

    // test commit
    
}