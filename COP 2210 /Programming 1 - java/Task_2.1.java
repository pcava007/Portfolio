import java.util.Scanner;

public class Task_1 {
    public static void main (String [] args){
        Scanner input = new Scanner (System.in);

        while (true) {
            System.out.println ("\n\n" + "Enter the bill amount:");
            double Bill = input.nextDouble ();

            if (Bill < 0) {
                System.out.println ("Invalid input. Bill amount cannot be negative.");
            } else {
                double Pay_Amnt;

                if (Bill < 350) {
                    Pay_Amnt = Bill - (Bill * 0.07);
                    } 
                
                else if (Bill >= 351 && Bill <= 500) {
                    Pay_Amnt = Bill - (Bill * 0.1);
                    } 
                
                else if (Bill >= 501 && Bill <= 750) {
                    Pay_Amnt = Bill - (Bill * 0.12);
                    } 
                
                else {
                    Pay_Amnt = Bill - (Bill * 0.15);
                    }

                System.out.printf ("Your payable amount after discount is $%.2f", Pay_Amnt);
            }
        }
    }
}

