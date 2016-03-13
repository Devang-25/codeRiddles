// Quora 
// http://www.quora.com/Algorithms/What-is-the-most-efficient-algorithm-to-check-if-a-number-is-a-Fibonacci-Number
// John Kurlak's answer

import java.math.BigDecimal;

public class FibonacciTester {
    private static BigDecimal zero = BigDecimal.valueOf(0);
    private static BigDecimal one = BigDecimal.valueOf(1);
    private static BigDecimal two = BigDecimal.valueOf(2);
    
    public static void main(String[] args) {
        BigDecimal num = new BigDecimal(args[0]);
	
        long start = System.currentTimeMillis();
	
        if (isFibonacci(num)) {
            System.out.println(num + " is a Fibonacci number.");
        } else {
            System.out.println(num + " is NOT a Fibonacci number.");
        }

        long end = System.currentTimeMillis();

        System.out.println("Ran in " + (end - start) + " milliseconds.");
    }

    public static boolean isFibonacci(BigDecimal n) {
        BigDecimal[] outputs1 = unFib(one, one, n);
        BigDecimal a = outputs1[1];

        return n.compareTo(a) == 0;
    }

    private static BigDecimal[] unFib(BigDecimal a, BigDecimal b, BigDecimal n) {
        if (n.compareTo(a) < 0) {
            return new BigDecimal[] { zero, zero, one };
        }

        BigDecimal[] inputs1 = fibPlus(a, b, a, b);
        BigDecimal[] outputs1 = unFib(inputs1[0], inputs1[1], n);
        BigDecimal k = outputs1[0];
        BigDecimal c = outputs1[1];
        BigDecimal d = outputs1[2];

        BigDecimal[] outputs2 = fibPlus(a, b, c, d);
        BigDecimal e = outputs2[0];
        BigDecimal f = outputs2[1];

        if (n.compareTo(e) < 0) {
            return new BigDecimal[] { two.multiply(k), c, d };
        }

        return new BigDecimal[] { two.multiply(k).add(one), e, f };
    }

    private static BigDecimal[] fibPlus(BigDecimal a, BigDecimal b, BigDecimal c, BigDecimal d) {
        BigDecimal bd = b.multiply(d);

        return new BigDecimal[] {
            bd.subtract(b.subtract(a).multiply(d.subtract(c))),
            a.multiply(c).add(bd)
        };
    }
}
