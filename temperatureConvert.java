/* Kaleb Butler
 * CIT 1613
 * Homework 5: Temperature Conversion
 */
import javax.swing.*;
public class temperatureConvert
{
    public static void main(String[] args)
    {
        // this code coverts from fahrenheit using a dialog box as shown in Lecture D notes and with help from google.
        // to celcius
        //
        // f -> c is 
        // c = (f-32) * 5/9;
        // f = (c*9/5) + 32;
        // Ask the user which conversion they want

        //Shows a dialog box using a JOption pane as in lecture D
        //Gives the user two options to choose from for conversion
        String[] options = {"Celsius to Fahrenheit", "Fahrenheit to Celsius"}; // customizes button choices.
        int choice = JOptionPane.showOptionDialog(
                null, // null centers it on screen
                "Select Conversion Type:", // asks user to choose
                "Temperature Conversion", // title of dialog box
                JOptionPane.DEFAULT_OPTION, // These are the defaul button settings
                JOptionPane.INFORMATION_MESSAGE,
                null, // No custom icon
                options,
                options[0]
        );

        if (choice == JOptionPane.CLOSED_OPTION) {
            return; // User closed the dialog
        }

        // Ask the user to input the temperature as STRING
        String input = JOptionPane.showInputDialog("Enter the temperature:");
        if (input == null) {
            return; // User cancelled and will close dialog box
        }

        try {
            double temp = Double.parseDouble(input); // converts string input into a decimal number
            double result;
            String message;
                // allows for decimal point numbers to be entered and decimal point numbers to be produced.
            if (choice == 0) { // "0" means the first button on the dialog box.
                // Celsius to Fahrenheit
                result = (temp * 9/5) + 32; // takes temp entered and convers to fahrenheit if chose that option
                message = temp + " degrees celsius converts too " + result + " degrees fahrenheit";
            } else {
                // Fahrenheit to Celsius
                result = (temp - 32) * 5/9; // takes temp entered and convers to celsius if chose that option
                message = temp + " degrees fahrenheit converts too " + result + " degrees celsius";
            }
                // show converted temperature in a message dialog box
            JOptionPane.showMessageDialog(null, message);


            // if a non-numeric value is entered this message will show.
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Invalid temperature input. Please enter a valid number.");
            
        }
    }
    }