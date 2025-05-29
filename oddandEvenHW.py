from breezypythongui import EasyFrame

class EvenAndOdd(EasyFrame):
    def __init__(self):
        # Initialize the main application window
        EasyFrame.__init__(self, title="Even or Odd Decider")

        # Label and input for the first number
        self.addLabel(text="First Number:", row=0, column=0, sticky="w")
        self.firstNumField = self.addIntegerField(value=0, row=0, column=1, sticky="w")

        # Label and input for the second number (needed for average)
        self.addLabel(text="Second Number:", row=1, column=0, sticky="w")  # NEW
        self.secondNumField = self.addIntegerField(value=0, row=1, column=1, sticky="w")  # NEW

        # Button to check if the first number is even or odd
        self.addButton(text="Check if Even or Odd", row=2, column=0, columnspan=2, command=self.evenOrOdd)

        # Button to calculate the average of num1 and num2
        self.addButton(text="Calculate Average", row=3, column=0, columnspan=2, command=self.calculateAverage)  # NEW

        # Output area for results — using a Label instead of TextArea to make it non-editable
        self.outputLabel = self.addLabel(text="", row=5, column=0, columnspan=2, sticky="w")  # UPDATED

    def evenOrOdd(self):
        # Get number from first input field
        num = self.firstNumField.getNumber()

        # Determine if even or odd
        if num % 2 == 0:
            result = f"{num} is even"
        else:
            result = f"{num} is odd"

        # Display result in the output label
        self.outputLabel["text"] = result

    def calculateAverage(self):
        # Get numbers from both input fields
        num1 = self.firstNumField.getNumber()
        num2 = self.secondNumField.getNumber()

        # Compute average
        average = (num1 + num2) / 2

        # Display average in the same output label
        self.outputLabel["text"] = f"The average of {num1} and {num2} is {average}"

# Launch the GUI application
if __name__ == "__main__":
    EvenAndOdd().mainloop()

