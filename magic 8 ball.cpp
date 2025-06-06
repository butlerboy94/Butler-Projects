#include <iostream>     // For input and output (cin, cout)
#include <cstdlib>      // For rand() and srand() functions
#include <ctime>        // For time() to seed the random number generator

using namespace std;    // Allows use of standard library names without std::

int main() {
    // Array of possible 8-Ball responses
    string responses[] = {
        "It is certain.",
        "Ask again later.",
        "Better not tell you now.",
        "Don't count on it.",
        "Yes, definitely!",
        "My reply is no.",
        "Outlook good.",
        "Very doubtful.",
        "You may rely on it.",
        "Signs point to yes."
    };

    // Seed the random number generator with the current time
    srand(time(0));

    string question;  // Variable to store the user's question

    // Display a welcome message
    cout << "🎱 Welcome to the Magic 8-Ball 🎱" << endl;

    // Prompt the user to ask a yes/no question
    cout << "Ask your yes/no question: ";

    // Get the full line of user input (in case they type more than one word)
    getline(cin, question);

    // Generate a random number between 0 and 9
    int index = rand() % 10;

    // Display the randomly selected response
    cout << "The Magic 8-Ball says: " << responses[index] << endl;

    return 0;  // End of the program
}
