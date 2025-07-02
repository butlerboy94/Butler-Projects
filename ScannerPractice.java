import java.util.Scanner;

public class ScannerPractice {
    public static void main(String[]args) {
        Scanner input = new Scanner(System.in); // creates Scanner object "input"
        
        String continueCalc = "yes"; // A string variable used to control wether the loop should continue running

        while (continueCalc.equalsIgnoreCase("yes")){
            // start a while loop that will run as long as the user types "yes"
            //continueCalc is the yes variable created and equalsignorecase means to ignore capitalization from input.

        
        System.out.print("Enter your name: "); // asks for input for name
        String name = input.nextLine(); // Use "string" for string inputs

        System.out.print("Enter your age: "); // asks for input for age
        int age = input.nextInt(); // use "int" for integer inputs
        int f_age = (age * 2); // multiply user input by 2, variable has to be assigned after age variable. 

       

        System.out.println("  "); // adds a space between lines of code

        System.out.print("Give me a number: "); // ask for number 1
        double number1 = input.nextDouble(); // convers number into a float.
            /*  must assgin variable to first input in ordered for it to ask for a secon on the next line. otherwise
                will run into each other on the same line and wont ask for input correclty. */
        System.out.print("Give me another number: ");// ask for number 2
        double number2 = input.nextDouble(); //converts number 2 into a float and assigns it to a variable

        System.out.print("Enter an operator (+, -, *, /): ");
        char operator = input.next().charAt(0); // this reads the first charachter of the input
        double result = 0; // this stores the variable

        switch (operator) { // SWITCH checks the value of 'operator' and matches it agaisnt different possible cases.
            case '+': // if the operator is '+'
                result = (number1 + number2); //adds number1 and number 2 together
                break; // exit the switch block
            case '-':
                result = (number1 - number2);
                break;
            case '*':
                result = (number1 * number2);
                break;
            case '/':
                if (number2 != 0){ // checks to avoid dividing by zero
                    result = (number1 / number2); // divides number if it is divisable
                } else { // prints error if number cannot divide by zero
                    System.out.println("Error: Cannot divde by zero.");
                    continue; //Skip to the next loop iteration
                }
                break;
                
            default: // this block runs if the user entered an invlid operator
                System.out.println("invalid operator");
                continue; // Skip to the next loop iteration


        }
        System.out.println(" ");
        System.out.println("Your name is " + name + " and your age twice from now will be " + f_age + " and you asked whats " + 
        number1 + " " + operator + " " + number2 + " is and this is your result --->: " + result);

        System.out.println(" ");

        System.out.print("Do you want to do this again? (yes/no): ");
        continueCalc = input.next(); // read user input (yes or no)

        input.nextLine(); // This helps restart the code and erases all previous data
                        //Important: clear the leftover newline so nextLine() works correctly next loop
          }
        

        input.close(); // this closes the scanner

        System.out.println("Thank you!");

    /* in order for a code to run repeatedly it needs to be stuck inside a while loop 
    and the nextLine() must be entered at the bottom */

    }
}
