// Import the Scanner class so we can get input from the user
import java.util.Scanner;

public class CoastGuardEnlistment {

    public static void main(String[] args) {
        
        // Create a Scanner object to read input from the user
        Scanner input = new Scanner(System.in);

        // Ask the user to enter their age
        System.out.println("What is your age?");

        // Read the age input as an integer
        int age = input.nextInt();

        // Check the user's age and determine enlistment status
        if (age < 17) {
            // If under 17, too young to enlist
            System.out.println("Sorry, too young to enlist.");
        } else if (age == 17) {
            // If exactly 17, can enlist with parental permission
            System.out.println("You can enlist with parental permission.");
        } else if (age >= 18 && age <= 35) {
            // If age is between 18 and 35, can enlist
            System.out.println("You can enlist!");
        } else if (age >= 36 && age <= 42) {
            // If age is between 36 and 42, can enlist only in the reserves
            System.out.println("You can enlist if you're in the reserves.");
        } else {
            // If older than 42, too old to enlist
            System.out.println("Sorry, too old.");
        }

        // Close the Scanner
        input.close();
    }
}
