import java.text.DecimalFormat;
import java.util.Scanner;

public class TaxCalculator {
    private static double basicRate = 0.04; // 4%
    private static double luxuryRate = 0.10; // 10%
    private static DecimalFormat decimalFormat = new DecimalFormat("#.###");

    public static double computeCostBasic(double price) {
        double cost = price + (price * basicRate);
        return roundToThreeSignificantFigures(cost);
    }

    public static double computeCostLuxury(double price) {
        double cost = price + (price * luxuryRate);
        return roundToThreeSignificantFigures(cost);
    }

    public static void changeBasicRateTo(double newRate) {
        if (newRate >= 4.0) {
            basicRate = newRate / 100.0;
        } else {
            System.out.println("Invalid basic tax rate! Rate cannot be less than 4%.");
        }
    }

    public static void changeLuxuryRateTo(double newRate) {
        if (newRate >= 10.0) {
            luxuryRate = newRate / 100.0;
        } else {
            System.out.println("Invalid luxury tax rate! Rate cannot be less than 10%.");
        }
    }

    public static double roundToThreeSignificantFigures(double value) {
        if (value == 0.0) {
            return 0.0;
        }
        
        final double magnitude = Math.pow(10, Math.floor(Math.log10(Math.abs(value))) + 1 - 3);
        return Double.parseDouble(decimalFormat.format(value / magnitude)) * magnitude;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the item price: ");
        double price = scanner.nextDouble();

        System.out.print("Enter the basic tax rate (%), or enter 'n/a' if not applicable: ");
        String basicTaxRateInput = scanner.next();
        if (basicTaxRateInput.equalsIgnoreCase("n/a")) {
            System.out.println("Basic Tax: Not Applicable");
        } else {
            double basicTaxRate = Double.parseDouble(basicTaxRateInput);
            changeBasicRateTo(basicTaxRate);
            System.out.println("Basic Tax: $" + decimalFormat.format(price * basicRate));
        }

        System.out.print("Enter the luxury tax rate (%), or enter 'n/a' if not applicable: ");
        String luxuryTaxRateInput = scanner.next();
        if (luxuryTaxRateInput.equalsIgnoreCase("n/a")) {
            System.out.println("Luxury Tax: Not Applicable");
        } else {
            double luxuryTaxRate = Double.parseDouble(luxuryTaxRateInput);
            changeLuxuryRateTo(luxuryTaxRate);
            System.out.println("Luxury Tax: $" + decimalFormat.format(price * luxuryRate));
        }

        if (!basicTaxRateInput.equalsIgnoreCase("n/a")) {
            System.out.println("Total Cost with Basic Tax: $" + decimalFormat.format(computeCostBasic(price)));
        }
        if (!luxuryTaxRateInput.equalsIgnoreCase("n/a")) {
            System.out.println("Total Cost with Luxury Tax: $" + decimalFormat.format(computeCostLuxury(price)));
        }

        scanner.close();
    }
}
