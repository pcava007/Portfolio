import java.util.Scanner;

public class BMR_Task_1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("\n"+"This program will calculate the number of 230 calories");
        System.out.println("candy bars to eat to maintain your weight."+"\n\n");

        System.out.print("What is your age in years? ");
        int age = input.nextInt();

        System.out.print("\n\n");
        System.out.print("What is your total height in inches? ");
        double height = input.nextDouble();

        System.out.print("\n\n");
        System.out.print("What is your weight in pounds? ");
        double weight = input.nextDouble();

        // BMR for a man
        double bmrM = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age);

        // BMR for a woman
        System.out.print("\n\n");
        double bmrW = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age);

        double chocolateBarsMan = bmrM / 230;
        double chocolateBarsWoman = bmrW / 230;

        System.out.printf("A male with those measurements should eat %.2f candy bars per day" + "\n" + "to maintain his weight%n", chocolateBarsMan);
        System.out.printf("A female with those measurements should eat %.2f candy bars per day" + "\n" + "to maintain her weight%n", chocolateBarsWoman);
        input.close();
    }
}
