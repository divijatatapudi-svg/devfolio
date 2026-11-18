
# Matrix Cell Swap
# Exchange the values of two cells in a 3 x 3 matrix.

matrix = []

# Read the 3 x 3 matrix
print("Enter 9 numbers for the 3 x 3 matrix:")

for i in range(3):
    row = list(map(int, input().split()))

    if len(row) != 3:
        print("Please enter exactly 3 numbers in each row.")
        exit()

    matrix.append(row)

# Display the original matrix
print("\nOriginal Matrix:")

for row in matrix:
    print(*row)

# Get the positions of the two cells (1-based)
r1, c1 = map(int, input("\nEnter first cell position (row column): ").split())
r2, c2 = map(int, input("Enter second cell position (row column): ").split())

# Validate positions
if not (1 <= r1 <= 3 and 1 <= c1 <= 3 and
        1 <= r2 <= 3 and 1 <= c2 <= 3):

    print("Invalid cell position.")

else:
    # Swap the two cell values
    matrix[r1 - 1][c1 - 1], matrix[r2 - 1][c2 - 1] = (
        matrix[r2 - 1][c2 - 1],
        matrix[r1 - 1][c1 - 1]
    )

    # Display the updated matrix
    print("\nMatrix after swapping:")

    for row in matrix:
        print(*row)
