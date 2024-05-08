import random

def generate_matrix(rows, columns):
    matrix = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]
    return matrix

def matrix_to_string(matrix):
    return ''.join(str(cell) for row in matrix for cell in row)

def write_to_file(filename, matrices):
    with open(filename, 'w') as file:
        for rows, columns, matrix in matrices:
            matrix_str = matrix_to_string(matrix)
            file.write(f"{rows}x{columns}:{matrix_str}\n")

def main():
    # Specify the number of matrices you want to generate
    num_matrices = 10
    matrices = []

    for _ in range(num_matrices):
        rows = random.randint(5, 10)  # Adjust the range as needed
        columns = random.randint(5, 10)  # Adjust the range as needed
        matrix = generate_matrix(rows, columns)
        matrices.append((rows, columns, matrix))

    write_to_file('mat.in', matrices)

if __name__ == "__main__":
    main()