/*
 * Kaleb Butler
 * Homework 8 Force/Mass calculation
 * CIT 1613
 */
import java.util.Scanner;

public class MassCalculation {

    // Gravitational constant G
    final static double G = 6.67E-11;

    public static void main(String[] args) {
        // Create a Scanner object for reading input from the user
        Scanner sc = new Scanner(System.in);

        // ask the user to enter the mass of the first body in kilograms
        System.out.print("Enter the mass of the first object in (kg): ");
        double mass1 = sc.nextDouble();  // Read first mass

        // ask the user to enter the mass of the second body in kilograms
        System.out.print("Enter the mass of the second object in (kg): ");
        double mass2 = sc.nextDouble();  // Read second mass

        // ask the user to enter the distance between the objects in meters
        System.out.print("Enter the distance between the objects in (m): ");
        double distance = sc.nextDouble();  // Read distance

        // Calculate the gravitational force using Newton's law of universal gravitation
        double force = G * mass1 * mass2 / Math.pow(distance, 2);

        // Display the result to the user
        System.out.printf("\nThe gravitational force of attraction between the objects is: %.2e Newtowns\n", force);
        // use the "%.2e" formatting for scientific notation.
        // Close the scanner
        sc.close();
    }
}
