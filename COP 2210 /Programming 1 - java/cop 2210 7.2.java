import java.util.Scanner;

public class OrderingSystem {
    private int totalQuantityOrdered;
    private Order[] orders;

    public void computeTotalQuantity(Order[] orders) {
        int total = 0;
        for (Order order : orders) {
            total += order.getQuantity();
        }
        totalQuantityOrdered = total;
    }

    public void getData() {
        Scanner scanner = new Scanner(System.in);

        boolean validInput = false;
        while (!validInput) {
            System.out.print("Enter the number of products you want to order: ");
            String input = scanner.nextLine();
            try {
                int numProducts = Integer.parseInt(input);
                if (numProducts > 0) {
                    orders = new Order[numProducts];
                    for (int i = 0; i < numProducts; i++) {
                        Order order = new Order();
                        order.readInput(scanner);
                        orders[i] = order;
                    }
                    validInput = true;
                } else {
                    System.out.println("Invalid input. Number of products must be a positive whole number.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Number of products must be a positive whole number.");
            }
        }

        System.out.println(); // Add a blank line for spacing

        scanner.close();
    }

    public void writeOutput() {
        System.out.println("Order Details:");
        for (Order order : orders) {
            System.out.println(order.toString());
        }

        System.out.println(); // Add a blank line for spacing

        System.out.println("Total Quantity Ordered: " + totalQuantityOrdered);
    }

    public static void main(String[] args) {
        OrderingSystem orderingSystem = new OrderingSystem();
        orderingSystem.getData();
        orderingSystem.computeTotalQuantity(orderingSystem.orders);
        orderingSystem.writeOutput();
    }
}

class Order {
    private String productName;
    private int quantity;

    public Order() {
        this("", 0);
    }

    public Order(String productName, int quantity) {
        set(productName, quantity);
    }

    public void set(String productName, int quantity) {
        setProductName(productName);
        setQuantity(quantity);
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public String getProductName() {
        return productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void readInput(Scanner scanner) {
        System.out.print("Enter the product name: ");
        String productName = scanner.nextLine();
        setProductName(productName);

        boolean validInput = false;
        while (!validInput) {
            System.out.print("Enter the quantity: ");
            String input = scanner.nextLine();
            try {
                int quantity = Integer.parseInt(input);
                if (quantity > 0) {
                    setQuantity(quantity);
                    validInput = true;
                } else {
                    System.out.println("Invalid input. Quantity must be a positive whole number.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Quantity must be a positive whole number.");
            }
        }
    }

    @Override
    public String toString() {
        return "Product: " + productName + ", Quantity: " + quantity;
    }
}
