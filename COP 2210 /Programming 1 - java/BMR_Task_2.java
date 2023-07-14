import java.util.Scanner;

public class BMR_Task_2 {
    public static void main (String [] args) {
        Scanner input = new Scanner (System.in);

        System.out.println ("\n"+"This program will calculate the number of 230 calories");
        System.out.println ("candy bars to eat to maintain your weight."+"\n\n");

        System.out.print ("What is your age in years? ");
        int age = input.nextInt ();

        System.out.print ("What is your total height in feet? ");
        double heightFeet = input.nextDouble ();

        System.out.print ("What is your weight in kilograms? ");
        double weightKg = input.nextDouble ();

        // Convert units for hieght and weight
        double heightInches = heightFeet * 12;
        double weightLbs = weightKg * 2.20462;

        // Calculate BMR for a man
        double bmrM = 66 + (6.3 * weightLbs) + (12.9 * heightInches) - (6.8 * age);

        // Calculate BMR for a woman
        double bmrW = 655 + (4.3 * weightLbs) + (4.7 * heightInches) - (4.7 * age);

        double chocolateBarsMan = bmrM / 230;
        double chocolateBarsWoman = bmrW / 230;

        System.out.printf ("A male with those measurements should eat %.2f candy bars per day to maintain his weight%n", chocolateBarsMan);
        System.out.printf ("A female with those measurements should eat %.2f candy bars per day to maintain her weight%n", chocolateBarsWoman);

        input.close ();
    }
}