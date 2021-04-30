import java.util.Scanner;

public class RecursiveRangeSum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter min number in range: ");
        int min = scanner.nextInt();

        System.out.print("Enter max number in range: ");
        int max = scanner.nextInt();


        int result = getSum(min, max, 0);
        System.out.println("The sum of all numbers in that range is " + result);
        
    }

    static int getSum(int currentNum, int max, int sum) {
        sum = sum + currentNum;
        
        if (currentNum == max) return sum;

        return getSum(currentNum + 1, max, sum);
    }
}