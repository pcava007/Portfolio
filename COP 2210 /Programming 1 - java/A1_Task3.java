import java.util.Scanner;

public class A1_Task3 {
    public static void main (String [] args) {
        Scanner input = new Scanner (System.in);

        System.out.println ("\n\n" + "Enter a line of text - no punctuation, please.");
        String line = input.nextLine ();

        int firstSpaceIndex = line.indexOf (' ');
        if (firstSpaceIndex != -1) {
            String firstWord = line.substring (0, firstSpaceIndex);
            String remainingWords = line.substring (firstSpaceIndex + 1);

            String modifiedLine = remainingWords + " " + firstWord;
            System.out.println ("\n\n" +"I have rephrased that line to read: " + modifiedLine);
        } else {
            System.out.println ("Invalid input. The line must contain at least two words separated by a space.");
        }

        input.close ();
    }
}
