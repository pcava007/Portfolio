import java.util.InputMismatchException;
import java.util.Scanner;

public class ArrayAnalyzer {
    private static final int MAX_ARRAY_SIZE = 1000; // Max size of array

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int size = getSizeFromUser(scanner);
        int[] numbers = readNumbersFromUser(scanner, size);

        int positiveCount = countPositiveNumbers(numbers);
        int negativeCount = countNegativeNumbers(numbers);
        int oddCount = countOddNumbers(numbers);
        int evenCount = countEvenNumbers(numbers);
        int zeroCount = countZeroNumbers(numbers);

        printResults(positiveCount, negativeCount, oddCount, evenCount, zeroCount);

        scanner.close();
    }

    private static int getSizeFromUser(Scanner scanner) {
        int size;
        do {
            System.out.print("Enter the size of the array: ");
            try {
                size = scanner.nextInt();
                if (size < 1 || size > MAX_ARRAY_SIZE) {
                    System.out.println("ERROR: Size must be between 1 and " + MAX_ARRAY_SIZE + ".");
                }
            } catch (InputMismatchException e) {
                System.out.println("ERROR: Invalid input. Size must be a positive integer.");
                size = 0; 
                scanner.nextLine(); 
            }
        } while (size < 1 || size > MAX_ARRAY_SIZE);

        return size;
    }

    private static int[] readNumbersFromUser(Scanner scanner, int size) {
        int[] numbers = new int[size];

        System.out.println("Enter " + size + " integers:");
        for (int i = 0; i < size; i++) {
            try {
                numbers[i] = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("ERROR: Invalid input. Only integers are allowed.");
                i--; // loop to decrease size of array until number of open spots = 0
                scanner.nextLine(); 
            }
        }

        return numbers;
    }
    
// for numbers greater than 0
    private static int countPositiveNumbers(int[] numbers) {
        int count = 0;
        for (int num : numbers) {
            if (num > 0) {
                count++;
            }
        }
        return count;
    }

// for numbers less than 0
    private static int countNegativeNumbers(int[] numbers) {
        int count = 0;
        for (int num : numbers) {
            if (num < 0) {
                count++;
            }
        }
        return count;
    }
    
// for all odd numbers
    private static int countOddNumbers(int[] numbers) {
        int count = 0;
        for (int num : numbers) {
            if (num % 2 != 0) {
                count++;
            }
        }
        return count;
    }
    
// for all even numbers
    private static int countEvenNumbers(int[] numbers) {
        int count = 0;
        for (int num : numbers) {
            if (num % 2 == 0) {
                count++;
            }
        }
        return count;
    }
// for numbers equal to 0
    private static int countZeroNumbers(int[] numbers) {
        int count = 0;
        for (int num : numbers) {
            if (num == 0) {
                count++;
            }
        }
        return count;
    }

    private static void printResults(int positiveCount, int negativeCount, int oddCount, int evenCount, int zeroCount) {
        System.out.println("Number of positive numbers: " + positiveCount);
        System.out.println("Number of negative numbers: " + negativeCount);
        System.out.println("Number of odd numbers: " + oddCount);
        System.out.println("Number of even numbers: " + evenCount);
        System.out.println("Number of zeros: " + zeroCount);
    }
}
