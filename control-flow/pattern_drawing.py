# A Python script that draws text-based patterns using nested loops

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Draw the pattern using nested loops
    row = 1  # Initialize row counter for while loop
    
    # While loop to iterate through each row
    while row <= size:
        # For loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        
        # Print newline to move to next row
        print()
        
        # Increment row counter
        row += 1

# Run the program
if __name__ == "__main__":
    main()