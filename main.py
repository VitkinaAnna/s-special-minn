import numpy as np

def find_s_special_elements(matrix):
    rows, cols = matrix.shape
    special_elements = []

    for i in range(rows):
        row_sum = np.sum(matrix[i, :])
        for j in range(cols):
            if matrix[i, j] > row_sum - matrix[i, j]:
                special_elements.append((matrix[i, j], i, j))

    return special_elements

def find_min_s_special_element(matrix):
    special_elements = find_s_special_elements(matrix)
    if not special_elements:
        return None, None, None, None

    min_element, min_row, min_col = min(special_elements, key=lambda x: (x[0], x[1]))
    return min_element, min_row, min_col, min_row + 1

# Приклад використання
matrix = np.array([
    [50, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 50],
    [13, 14, 15, 16]
])

min_element, min_row, min_col, row_number = find_min_s_special_element(matrix)

if min_element is not None:
    print(f"Мінімальний S-особливий елемент: {min_element}")
    print(f"Номер рядка: {row_number}")
    print(f"Індекси елемента: ({min_row+1}, {min_col+1})")
else:
    print("таких нема!")
