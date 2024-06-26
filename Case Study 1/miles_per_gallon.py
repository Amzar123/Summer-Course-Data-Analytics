def calculate_miles_per_gallon():
    while True:
        # Take integer input from the user
        gallons = int(input("Enter the gallons used (-1 to end): "))

        # Check if the user wants to end the program
        if gallons == -1:
            break

        # Take integer input from the user
        miles = int(input("Enter the miles driven: "))

        # Print the input
        print("The miles/gallon for this tank was: ", miles/gallons)

if __name__ == "__main__":
    # Call the function to start the program
    calculate_miles_per_gallon()
