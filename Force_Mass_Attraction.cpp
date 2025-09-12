#include <iostream> //Allows for input/output tools like cin, cout, etc.
#include <string> //Allows use of strings.
#include <iomanip> // Allows for input/out control. Allows you to control decimal places in input and output for example.
#include <cmath> //Allows for math functions like sqrt
using namespace std; //Uses standard name space so you don't have to put "std" every time.

int main()
{
double M1, M2, d; //Declared variables to be assigned to later
double G = 6.67e-11; //Formula to calculate gravitational constant

cout << "What is the 1st mass in kg?: > ";
cin >> M1; //First declared variable assigned to the input for mass 1
cout << "What is the 2nd mass in kg?: > ";
cin >> M2; //Second declared variable assigned to the input for mass 2
cout << "What is the distance in meters?: > ";
cin >> d; //third declared variable assigned to the input for distance

double F = G*M1*M2/pow(d,2); //formula to calculate force of attraction

cout << "The force of attraction is: " << scientific << setprecision(3) << F << " N" << endl; //scientific and setprecision to format output in scientific form and stop at 3 spots after decimal.




return 0;
}