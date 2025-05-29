def get_data():
    data = []  # Initialize an empty list to store the user inputs
    while True:
        value = float(input("Enter a value (or -1 to stop): "))  # Prompt the user for input
        if value == -1:
            break  # Stop input collection when -1 is entered
        data.append(value)  # Add the entered value to the list
    return data  # Return the list of entered values

def get_average(L):
    if len(L) == 0:
        return 0  # Prevent division by zero if the list is empty
    return sum(L) / len(L)  # Calculate and return the average

# Main code
data_list = get_data()  # Call get_data to create the list
average = get_average(data_list)  # Call get_average to calculate the average

# Print the list and the average
print("The entered values are:", data_list)
print("The average is:", average)
