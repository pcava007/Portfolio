import java.util.Scanner;

class Assingment_3_Task_2{

    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.println("How much money can you spend on chocolate bars: ");
        int N = obj.nextInt();
        int chocolates = N;
        int coupons = N;
        while(coupons>=6){
            //Find extra chocolates from coupons
            int extra_chocolates = coupons/6;
            chocolates = chocolates + extra_chocolates;
            coupons = coupons%6;
            //New coupons because of extra chocolates
            coupons = coupons + extra_chocolates;
        }
        System.out.println("\n" + "After redeeming coupons, you will have " + chocolates + " chocolate bars and " + coupons + " leftover coupon(s)");
    }
}
