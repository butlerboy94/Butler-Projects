/*
 * Kaleb Butler
 * CIT 1613
 * Homework 9A Desks Chairs and Tables
 */
// Import the Scanner class so we can get input from the user
import java.util.Scanner;

// This is the main class of the program
public class FurnitureCalculator {

    // This is the main method where the program starts
    public static void main(String[] args) {

        // Create a Scanner object to read input from the keyboard
        Scanner input = new Scanner(System.in);

        // Set the prices of the items
        int deskPrice = 150;   // Each desk costs $150
        int chairPrice = 50;   // Each chair costs $50
        int tablePrice = 75;   // Each table costs $75
        String runAgain;       // Variable for string answer to run again

        // Use a do-while loop to repeat the program
        do {
            // Ask the user how many desks they want to buy
            System.out.print("How many desks do you wish to buy? ");
            int desks = input.nextInt();  // Read the number of desks

            // Ask the user how many chairs they want to buy
            System.out.print("How many chairs do you wish to buy? ");
            int chairs = input.nextInt();  // Read the number of chairs

            // Ask the user how many tables they want to buy
            System.out.print("How many tables do you wish to buy? ");
            int tables = input.nextInt();  // Read the number of tables

            /*
             * when using numbers with "nextInt()" the newline character remains in the input buffer.
             * when you call input.nextLine() right after nextInt() it reads that leftover newline
             * so runAgain becomes an empty string and wont output correctly. it will output on one line
             * instead of allowing for input. You must consume the leftover newline
             */

            input.nextLine(); // Consume the leftover newline after nextInt()

            // Calculate the total price for each item
            double totalDeskCost = desks * deskPrice;
            double totalChairCost = chairs * chairPrice;
            double totalTableCost = tables * tablePrice;

            // Add up all the totals to get the final bill
            double totalBill = totalDeskCost + totalChairCost + totalTableCost;

            // Show the results to the user and use printf() for formatting to two decimal points.
            System.out.printf("Total price of desks = $%.2f\n", totalDeskCost);
            System.out.printf("Total price of chairs = $%.2f\n", totalChairCost);
            System.out.printf("Total price of tables = $%.2f\n", totalTableCost);
            System.out.printf("Total bill = $%.2f\n", totalBill);

            // Ask user if they want to run again
            System.out.print("Do you want to run again? (Yes/No): ");
            runAgain = input.nextLine().trim().toLowerCase(); //formats input to accept any lower or uppercase input. 

        } while (runAgain.equals("yes")); // while loop to allow the program to run again based on user input.

        System.out.println("Thank you!"); // Message for if they type no.

        // Close the scanner because we are done using it
        input.close();
    }
    
    /* How to format a decimal point
     * % = Signals that formatting instructions follow.
     * .2f = means show 2 digits after the decimal point.
     * f = stands for floating-point number (float or double).
     * \n = moves the cursor to the next line after printing, like pressing "Enter".
     */
}
