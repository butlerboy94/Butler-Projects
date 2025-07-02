/*
 * Kaleb Butler
 * Homework 8: Quarts and Miles - Miles conversion part
 * CIT 1613
 */
import java.util.Scanner;
import java.utili.scanner;

public class MilesConversion{

    public static void main(String[]args)
    {
        final int Inches_In_Mile = 12 * 5280;  // calucaltion for inchest in a mile which is 63,360
        final int Feet_In_Mile = 5280;         // calculation for feet in a mile which 5,280
        final int Yards_In_Mile = 1760;        // calculation for yards in a mile which 1,760

        double miles = 5.0;  // Assigned 5 to miles and as a float

        // Calucate conversions as a float
        double inches = miles * Inches_In_Mile;
        double feet   = miles * Feet_In_Mile;
        double yards  = miles * Yards_In_Mile;
      

       
        System.out.println("There are " + inches + " inches in " + miles + " miles"); // display the output for inches
        System.out.println("There are " + feet + " feet in " + miles + " miles"); // display the output for feet
        System.out.println("There are " + yards + " yards in " + miles + " miles"); // display the output for yards
        System.out.println(" ");

        Scanner sc = new Scanner(System.in); //open utility scanner to get input
        System.out.print("How many miles?: "); // ask for user input
        miles = sc.nextDouble(); // allow miles to entered as a float
        sc.close();//close scanner
        
        inches = miles * Inches_In_Mile;
        feet = miles * Feet_In_Mile;
        yards = miles * Yards_In_Mile;

        System.out.println("There are " + inches + " inches in " + miles + " miles"); // display the output for inches
        System.out.println("There are " + feet + " feet in " + miles + " miles"); // display the output for feet
        System.out.println("There are " + yards + " yards in " + miles + " miles"); //display the output for miles

            
            
         

    }
}