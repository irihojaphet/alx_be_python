# A Python script that generates multiplication tables using for loops

def main():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print the multiplication table using a for loop
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the program
if __name__ == "__main__":
    main()