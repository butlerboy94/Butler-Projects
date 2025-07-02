/*
 * Kaleb Butler
 * Homework 8: Quarts and Miles - Quarts conversion part
 * CIT 1613
 */

import java.util.Scanner;

public class QuartsToGallons{

public static void main(String[]args)
{
    final int Quarts_In_Gallons = 4; // declare a variable to how many quarts equal a gallon
    int quartsNeeded = 18; // declare how many quarts are needed
    int gallons = quartsNeeded / Quarts_In_Gallons; // calculate how many quarts needed equal how many gallons
    int leftover = quartsNeeded % Quarts_In_Gallons; // calculate remained of quarts. 
    System.out.println("A job that needs " + quartsNeeded + 
    " Quarts requires " + gallons + 
    " gallons plus " + leftover + " quart(s)" ); // print output that display how many gallons and how many quarts remain. 
    System.out.println(" ");


    Scanner sc = new Scanner(System.in); //to ask input from users.
    
    System.out.print("How many quarts?: "); //ask input from users.
    quartsNeeded = sc.nextInt(); // assgin a integer value to the input
    sc.close(); // close scanner
    
    gallons = quartsNeeded / Quarts_In_Gallons; // replace "quartsNeeded" with quarts from user input for calculation.
    leftover = quartsNeeded % Quarts_In_Gallons; // calculate remained of quarts
    System.out.println("A job that needs " + quartsNeeded + 
    " Quarts requires " + gallons + 
    " gallons plus " + leftover + " quart(s)" ); // print out that displas how many gallons and how many quarts remain.


    

}

}