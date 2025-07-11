import java.util.Scanner;  // Import Scanner class to get user input

public class PasswordValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // Create Scanner object to read input

        // Ask the user to enter a password
        System.out.print("Enter a new password: ");
        String password = scanner.nextLine();  // Read the full line of input from the user

        // Initialize variables to count different character types
        int uppercaseCount = 0;    // Counts uppercase letters (A-Z)
        int lowercaseCount = 0;    // Counts lowercase letters (a-z)
        int digitCount = 0;        // Counts digits (0-9)
        int specialCharCount = 0;  // Counts special characters (not a letter or digit)

        // Loop through each character in the password string
        for (int i = 0; i < password.length(); i++) {
            char ch = password.charAt(i);  // Get character at position i

            // Check if the character is uppercase letter
            if (Character.isUpperCase(ch)) {
                uppercaseCount++;  // Increase uppercase count
            }
            // Check if the character is lowercase letter
            else if (Character.isLowerCase(ch)) {
                lowercaseCount++;  // Increase lowercase count
            }
            // Check if the character is a digit
            else if (Character.isDigit(ch)) {
                digitCount++;  // Increase digit count
            }
            // If not letter or digit, treat it as special character
            else {
                specialCharCount++;  // Increase special character count
            }
        }

        // Check if password meets all the requirements:
        // length is 8 or more
        // at least 1 uppercase letter
        // at least 1 lowercase letter
        // at least 1 digit
        // at least 1 special character
        boolean isValid = password.length() >= 8 &&
                          uppercaseCount >= 1 &&
                          lowercaseCount >= 1 &&
                          digitCount >= 1 &&
                          specialCharCount >= 1;

        // Tell the user if the password is valid or not
        if (isValid) {
            System.out.println("Password is valid.");
        } else {
            System.out.println("Password is NOT valid.");
            System.out.println("Your password must:");
            System.out.println("- Be at least 8 characters long");
            System.out.println("- Contain at least 1 uppercase letter");
            System.out.println("- Contain at least 1 lowercase letter");
            System.out.println("- Contain at least 1 digit");
            System.out.println("- Contain at least 1 special character");
        }

        scanner.close();  // Close the scanner to free resources
    }
}
