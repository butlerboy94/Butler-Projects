#include <iostream>
#include <cstdlib>   // for rand() and srand()
#include <ctime>     // for time()

using namespace std;

int main()
{
    bool done = false;
    int secret;
    int guess;
    int guessCount = 0;

    // Generate a random number between 1 and 100
    srand(time(0));          // seed random number generator
    secret = rand() % 100 + 1;

    cout << "I'm thinking of a number between 1 and 100.\n";

    while (!done)
    {
        cout << "\nGuess the number 1-100! > ";
        cin >> guess;

        guessCount++;

        if (guess == secret)
        {
            cout << "Congrats! You win!\n";
            cout << "You guessed it in " << guessCount << " tries.\n";
            done = true;
        }
        else if (guess < secret)
        {
            cout << "Sorry, your guess is too low.\n";
            cout << "Guesses made: " << guessCount << " / 10\n";
        }
        else
        {
            cout << "Sorry, your guess is too high.\n";
            cout << "Guesses made: " << guessCount << " / 10\n";
        }

        // Check if player exceeded 10 guesses
        if (guessCount >= 10 && !done)
        {
            cout << "\nGame over! You’ve used all 10 guesses.\n";
            cout << "The secret number was: " << secret << endl;
            done = true;
        }
    }

    return 0;
}
