#include <iostream> // For input/output
#include <string>   // For using string data type
#include <iomanip>  // For formatting output (like decimal places)
#include <algorithm> // For using transform() to covert strings to lowercase

using namespace std;

int main(){
    // Declare variables to store income and expenses values.
    double income;
    string choice;
    double food = 0.0;
    double housing = 0.0;
    double transportation = 0.0;
    double fun = 0.0;
    double leftover;
    
cout << "What is your monthly net income?: ";   // ask for users monthly net income.
cin >> income;  // attach income variable to income input.
cout << "would you like to deduct expenses like food, housing, transportation, and fun? (yes/no): ";    //ask for yes or no input for calculations
cin >> choice;  // attach choice variable to user input choice.
transform(choice.begin(), choice.end(), choice.begin(), ::tolower); // converts using input to all lowercase.

if (choice == "yes"){   //if user puts yes then asks for following input.
    cout << "what is your food expense?: ";     //ask for food expense
    cin >> food;    // attach food variable to food input.
    cout << "What is your housing expense?: ";  // ask for housing expense.
    cin >> housing; // attach housing variable to housing input.
    cout << "What is your transportation expense?: ";   // ask for transportation expense.
    cin >> transportation;  // attach transportation variable to housing input.
    cout << "How much do you spend on fun?: ";  // ask for fun expense.
    cin >> fun; // attach fun variable to fun expense.

    double leftover = income - food - housing - transportation - fun;   // calculation for left over money.
    cout << fixed << setprecision(2);   // limits output to 2 decimal points.
    cout << "You will have: $" << leftover << " at the end of the month!";  // output
    
    




}
else if (choice == "no"){   // if user decides no.
    cout << fixed << setprecision(2);   // limits the output to 2 decimal points.
    cout << "Okay your net income is: $" << income; // output
}
else{ // if user inputs invalid input.
    cout << "Invalid choice. Please enter 'yes' or 'no'. \n";
}
return 0; // ends main function.
}