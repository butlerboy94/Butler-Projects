#define _USE_MATH_DEFINES

#include <iostream>                             // getline allows us to get the entire string or line for data
#include <string>
#include <iomanip>
#include <cmath>
#include <fstream> // You need this to write and read files.
#include <cassert>
#include <cctype>
using namespace std;

string get_letter_as_digit(char letter)
{
    string value = "";
    letter = toupper(letter);
    switch(letter)
{    
    case 'A':
    case 'B':
    case 'C':
        value = "2";
        break;
    case 'D':
    case 'E':
    case 'F':
        value = "3";
        break;
    case 'G':
    case 'H':
    case 'I':
        value = "4";
        break;
    case 'J':
    case 'K':
    case 'L':
        value = "5";
        break;
    case 'M':
    case 'N':
    case 'O':
        value = "6";
        break;
    case 'P':
    case 'Q':
    case 'R':
    case 'S':
        value = "7";
        break;
    case 'T':
    case 'U':
    case 'V':
        value = "8";
        break;
    case 'W':
    case 'X':
    case 'Y':
    case 'Z':
        value = "9";
        break;
    default:
        value = string(1, letter);
}
    return value;
}

int main()
{
    string PhoneNumber;
    cout << "Enter a number such as '1800HOTJAVA': ";
    cin >> PhoneNumber;
    string output ="";
    string digitsOnly = "";
    
// Convert everything to numbers and strip out dashes
    for (char ch : PhoneNumber) {
        if (isalnum(ch)) { // only letters or numbers
            digitsOnly += get_letter_as_digit(ch);
        }
    }

    // Format the number properly: 1-800-XXX-XXXX
    for (int i = 0; i < digitsOnly.length(); i++) {
        output += digitsOnly[i];

        if (i == 0) output += '-';         // after '1'
        else if (i == 3) output += '-';    // after '800'
        else if (i == 6) output += '-';    // after next 3 digits
    }

    cout << output << endl;
    cout << "Booyah!";
    return 0;
}