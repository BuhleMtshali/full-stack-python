# NESTED LOOPS
for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i} x {j} = {i * j}")


# NESTED 2D LISTS
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for first_row in nested_list:
    print(first_row)
    for nested_values in first_row:
        print(nested_values, end=" ")
    print()


# NESTED LIST COMPREHENSION