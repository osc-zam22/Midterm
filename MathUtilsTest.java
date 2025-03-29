// imports necessary packages

import static org.junit.Assert.*;
import org.junit.Test;

public class MathUtilsTest {

    @Test
    public void testAdd()
    {
        //instantiates MathUtils object
        MathUtils test = new MathUtils();

        // first test case adds two positive numbers
        int sum1 = test.add(17, 38);
        assertEquals(55, sum1);
        //second test case, adds two zeroes
        int sum2 = test.add(0, 0);
        assertEquals(0, sum2);
        //third test case, adds to negative numbers
        int sum3 = test.add(-17, -38);
        assertEquals(-55, sum3);
        // fourth test case, adds a positive number and negative number
        // of equal magnitude, should result in 0 
        int sum4 = test.add(-15, +15);
        assertEquals(0, sum4);
        // fifth test case, adds a positive number larger then the negative
        // number.
        int sum5 = test.add(20, -10);
        assertEquals(10, sum5);
        // final test case, adds a negative number larger then the positve
        // number.
        int sum6 = test.add(-20, 10);
        assertEquals(-10, sum6);

    }


    @Test
    public void testSubtract()
    {
        MathUtils test = new MathUtils();
        // first test case, test subtraction between two positives
        int difference1 = test.subtract(20 , 10);
        assertEquals(10 , difference1);
        //second test case, test subtraction of two zeroes
        int difference2 = test.subtract(0, 0);
        assertEquals(0, difference2);
        // third test case, tests subtraction between a positive numbner and
        // a zero
        int difference3 = test.subtract(50, 0);
        assertEquals(50, difference3);
        // fourth test case, subtractoin between 0 and a positive number
        int difference4 = test.subtract(0, 50);
        assertEquals(-50, difference4);
        // fifth test case, subtractoin between 0 and a negative number
        int difference5 = test.subtract(0, -50);
        assertEquals(50, difference5);
        // sixth test case, subtraction between 2 negative numbers
        int difference6 = test.subtract(-50, -25);
        assertEquals(-25, difference6);
    }
    

    @Test
    public void testMultply()
    {
        MathUtils test = new MathUtils();
        // first test case, two positive numbers
        int solution1 = test.multiply(5, 5);
        assertEquals(25, solution1);
        // second test case, two negative numbers
        int solution2 = test.multiply(-5, -5);
        assertEquals(25, solution2);
        // third test, one positive and one negative
        int solution3 = test.multiply(5, -5);
        assertEquals(-25, solution3);
        // fourth test case, multiplication with zero
        int solution4 = test.multiply(25, 0);
        assertEquals(0, solution4);
        // final test case, two zeroes
        int solution5 = test.multiply(0, 0);
        assertEquals(0, solution5);
    }

    @Test
    public void testDivide() {
        MathUtils test = new MathUtils();
        
        // Test case 1: Divide two positive numbers
        double result1 = test.divide(10, 2);
        assertEquals(5.0, result1, 0.0001);
        
        // Test case 2: Divide a positive number by a negative number
        double result2 = test.divide(10, -2);
        assertEquals(-5.0, result2, 0.0001);
        
        // Test case 3: Divide two negative numbers
        double result3 = test.divide(-10, -2);
        assertEquals(5.0, result3, 0.0001);
        
        // Test case 4: Division resulting in a decimal
        double result4 = test.divide(7, 2);
        assertEquals(3.5, result4, 0.0001);
        
        // Test case 5: Division by zero
        double result5 = test.divide(10, 0);
        assertEquals(-1.0, result5, 0.0001);
        
        // Test case 6: Zero divided by any number
        double result6 = test.divide(0, 5);
        assertEquals(0.0, result6, 0.0001);
        
        // Test case 7: Zero divided by zero (should return -1.0 as per your implementation)
        double result7 = test.divide(0, 0);
        assertEquals(-1.0, result7, 0.0001);
    }

// test commit from laptop


}
