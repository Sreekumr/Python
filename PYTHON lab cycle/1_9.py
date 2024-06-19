def set_union(set1, set2):
    return set1.union(set2)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_difference(set1, set2):
    return set1.difference(set2)

def main():
    while True:
        print("\nMenu:")
        print("1. Set Union")
        print("2. Set Intersection")
        print("3. Set Difference")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 4:
            print("Exiting the program.")
            break

        set1 = set(map(int, input("Enter the elements of the first set separated by space: ").split()))
        set2 = set(map(int, input("Enter the elements of the second set separated by space: ").split()))

        if choice == 1:
            result = set_union(set1, set2)
            print(f"Union of {set1} and {set2} is {result}")

        elif choice == 2:
            result = set_intersection(set1, set2)
            print(f"Intersection of {set1} and {set2} is {result}")

        elif choice == 3:
            result = set_difference(set1, set2)
            print(f"Difference of {set1} and {set2} is {result}")

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
