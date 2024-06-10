def print_pyramid(height):
    for i in range(height):
        # Print leading spaces
        for j in range(height - i - 1):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        
                   # Move to the next line
        print()


height = 20
print_pyramid(height)
