matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Матрица 3x3:")
for row in matrix:
    print(row)

print(f"\nЭлемент [0][0]: {matrix[0][0]}")
print(f"Элемент [1][2]: {matrix[1][2]}")
print(f"Элемент [2][1]: {matrix[2][1]}")

print(f"\nКоличество строк: {len(matrix)}")
print(f"Количество столбцов: {len(matrix[0])}")
