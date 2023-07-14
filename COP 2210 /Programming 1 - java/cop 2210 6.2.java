import java.util.Scanner;
import java.util.StringTokenizer;

public class WordCounter {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            String[] lines = new String[4];

            System.out.println("Enter any four lines");
            for (int i = 0; i < 4; i++) {
                System.out.print("Line " + (i + 1) + ": ");
                lines[i] = scanner.nextLine();
            }

            int totalWords = 0;
            System.out.println();

            for (String line : lines) {
                StringTokenizer tokenizer = new StringTokenizer(line);
                while (tokenizer.hasMoreTokens()) {
                    String word = tokenizer.nextToken();
                    System.out.println(word);
                    totalWords++;
                }
                System.out.println(); // Line break after each line
            }

            System.out.println("Total number of words: " + totalWords);
        }
    }
}
