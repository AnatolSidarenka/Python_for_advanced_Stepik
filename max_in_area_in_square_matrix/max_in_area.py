def max_in_area(m: list) -> int:
    max_in_matrix = matrix[0][0]
    for i in range(len(m)):
        if i <= n // 2:
            max_in_row = max(matrix[i][:i + 1] + matrix[i][n - i - 1:])
        else:
            max_in_row = max(matrix[i][:n - i] + matrix[i][i:])
        max_in_matrix = max(max_in_row, max_in_matrix)
    return max_in_matrix


def write_square_matrix(size: int) -> list:
    mat = []
    for _ in range(size):
        string = [int(num) for num in input().split()]
        mat.append(string)
    return mat


n = int(input())
matrix = write_square_matrix(n)
print(max_in_area(matrix))
