# Create an empty dictionary to store English-Spanish word pairs
translations = {}

while True:
    # Ask the user for the English word
    english_word = input("Enter an English word (or Q to quit): ")

    # Check if the user wants to quit
    if english_word.lower() == 'q':
        break

    # Ask for the Spanish translation of the word
    spanish_word = input(f"Enter the Spanish translation for '{english_word}': ")

    # Add the word pair to the dictionary
    translations[english_word] = spanish_word

    # Display the updated dictionary, sorted alphabetically by the English words
    print("\nUpdated Dictionary (sorted alphabetically):")
    for eng, span in sorted(translations.items()):
        print(f"{eng}: {span}")

print("OK, done! The final dictionary is:")
# Display the final dictionary, sorted alphabetically by the English words
for eng, span in sorted(translations.items()):
    print(f"{eng}: {span}")
