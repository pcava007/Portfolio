import java.util.Scanner;

public class Assingment_3_Task_1
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while (true) {
            System.out.println("Enter data values for which to compute the geometric mean.");
            System.out.println("Enter a negative number after you have entered all the data values.");
            
            int count = 0;
            double ans = 1, value = 1;
            
            while (value > 0) {
                value = sc.nextDouble();
                if (value > 0) {
                    ans *= value;
                    count++;
                }
            }
            
            if (count > 0) {
                System.out.println("The geometric mean is " + Math.pow(ans, 1.0 / count));
            } else {
                System.out.println("No valid data values entered. Exiting the program.");
                break;
            }
            
            System.out.println("\n\n" + "Press Enter to continue or 'q' to quit.");
            sc.nextLine(); // Clear the newline character
            String input = sc.nextLine();
            if (input.equalsIgnoreCase("q")) {
                System.out.println("End of program.");
                break;
            }
        }
        
        sc.close();
    }
}
