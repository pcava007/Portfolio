import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Characteristic {
    private String description;
    private int rating;

    public Characteristic() {
        this.description = "No description yet";
        this.rating = 0;
    }

    public Characteristic(String description, int rating) {
        this.description = description;
        this.rating = rating;
    }

    public void setRating(int rating) {
        if (isValid(rating)) {
            this.rating = rating;
        } else {
            System.out.println("Invalid rating! Rating remains unchanged.");
        }
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getRating() {
        return rating;
    }

    public String getDescription() {
        return description;
    }

    private boolean isValid(int rating) {
        return rating >= 0 && rating <= 10;
    }

    @Override
    public String toString() {
        return "Description: " + description + ", Rating: " + rating;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean restart = true;
        List<Characteristic> characteristicsList = new ArrayList<>();

        while (restart) {
            Characteristic user1Characteristic = new Characteristic();
            Characteristic user2Characteristic = new Characteristic();

            // User 1 input
            System.out.println("User 1:");
            System.out.print("Enter description: ");
            String user1Description = scanner.nextLine();
            user1Characteristic.setDescription(user1Description);

            int user1Rating;
            do {
                System.out.print("Enter rating (0-10): ");
                user1Rating = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character
                if (!user1Characteristic.isValid(user1Rating)) {
                    System.out.println("Invalid rating! Please enter a rating between 0 and 10.");
                }
            } while (!user1Characteristic.isValid(user1Rating));
            user1Characteristic.setRating(user1Rating);

            // User 2 input
            System.out.println("\nUser 2:");
            System.out.print("Enter description: ");
            String user2Description = scanner.nextLine();
            user2Characteristic.setDescription(user2Description);

            int user2Rating;
            do {
                System.out.print("Enter rating (0-10): ");
                user2Rating = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character
                if (!user2Characteristic.isValid(user2Rating)) {
                    System.out.println("Invalid rating! Please enter a rating between 0 and 10.");
                }
            } while (!user2Characteristic.isValid(user2Rating));
            user2Characteristic.setRating(user2Rating);

            // User 1 rates User 2's description
            System.out.println("\nUser 1, rate User 2's description:");
            int user1RatingForUser2;
            do {
                System.out.print("Enter rating (0-10): ");
                user1RatingForUser2 = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character
                if (!user1Characteristic.isValid(user1RatingForUser2)) {
                    System.out.println("Invalid rating! Please enter a rating between 0 and 10.");
                }
            } while (!user1Characteristic.isValid(user1RatingForUser2));
            user2Characteristic.setRating(user1RatingForUser2);

            // User 2 rates User 1's description
            System.out.println("\nUser 2, rate User 1's description:");
            int user2RatingForUser1;
            do {
                System.out.print("Enter rating (0-10): ");
                user2RatingForUser1 = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character
                if (!user2Characteristic.isValid(user2RatingForUser1)) {
                    System.out.println("Invalid rating! Please enter a rating between 0 and 10.");
                }
            } while (!user2Characteristic.isValid(user2RatingForUser1));
            user1Characteristic.setRating(user2RatingForUser1);

            // Add characteristics to the list
            characteristicsList.add(user1Characteristic);
            characteristicsList.add(user2Characteristic);

            // Display table
            System.out.println("\nDescription\t\tUser 1 Rating\tUser 2 Rating");
            System.out.println("----------------------------------------------------");
            for (Characteristic characteristic : characteristicsList) {
                System.out.printf("%-16s\t%d\t\t%d%n", characteristic.getDescription(), characteristic.getRating(), characteristicsList.get(characteristicsList.indexOf(characteristic) ^ 1).getRating());
            }

            // Ask the user if they want to restart
            System.out.print("\nDo you want to restart the program? (yes/no): ");
            String restartChoice = scanner.next();
            scanner.nextLine(); // Consume the newline character

            if (!restartChoice.equalsIgnoreCase("yes")) {
                restart = false;
            }

            System.out.println();
        }
    }
}
