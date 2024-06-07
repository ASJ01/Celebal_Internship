def lower_triangular(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def upper_triangular(rows):
    for i in range(rows, 0, -1):
        print('  ' * (rows - i) + '* ' * i)

def pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

def main():
    while True:
        print("\nSelect the pattern you want to generate:")
        print("1. Lower Triangular")
        print("2. Upper Triangular")
        print("3. Pyramid")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            rows = int(input("Enter the number of rows for Lower Triangular pattern: "))
            lower_triangular(rows)
        elif choice == '2':
            rows = int(input("Enter the number of rows for Upper Triangular pattern: "))
            upper_triangular(rows)
        elif choice == '3':
            rows = int(input("Enter the number of rows for Pyramid pattern: "))
            pyramid(rows)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
