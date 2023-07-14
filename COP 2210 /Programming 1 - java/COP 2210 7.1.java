import java.util.Scanner;

public class SalaryCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Number of employees
        System.out.print("Enter the number of employees: ");
        int numEmployees = scanner.nextInt();

        // Array for salaries
        double[] salaries = new double[numEmployees];

        for (int i = 0; i < numEmployees; i++) {
            System.out.print("Enter the salary for employee " + (i + 1) + ": ");
            salaries[i] = scanner.nextDouble();
        }

        System.out.print("Enter the bonus amount (in percentage): ");
        double bonusPercentage = scanner.nextDouble();

        // New salary with bonus
        double[] newSalaries = addBonus(salaries, bonusPercentage);

        for (int i = 0; i < numEmployees; i++) {
            System.out.println("Employee " + (i + 1) + ":");
            System.out.println("Old Salary: $" + salaries[i]);
            System.out.println("New Salary: $" + newSalaries[i]);
            System.out.println();
        }

        scanner.close();
    }

    public static double[] copyArray(double[] source, double[] dest) {
        for (int i = 0; i < source.length; i++) {
            dest[i] = source[i];
        }
        return dest;
    }

    public static double[] addBonus(double[] salary, double bonus) {
        double[] copy = new double[salary.length];
        copyArray(salary, copy);

        for (int i = 0; i < copy.length; i++) {
            copy[i] += (copy[i] * bonus) / 100.0;
        }

        return copy;
    }
}
