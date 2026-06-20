# Program to print a full pyramid pattern
# changing the file and run for 

# Get the number of rows from the user
rows = int(input("Enter number of rows: "))

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop 1: Prints the leading spaces for alignment
    for j in range(rows - i):
        print(" ", end="")
        
    # Inner loop 2: Prints the stars for the pyramid
    for k in range(2 * i - 1):
        print("*", end="")
        
    # Move to the next line after completing each row
    print()
