def write_square_matrix(n: int) -> list:
    return [[int(i) for i in input().split()] for _ in range(n)]


def check_numbers_matrix(m: list) -> bool:
    temp = []
    [temp.append(el) for row in m for el in row if el not in temp and el != 0]
    matrix_numbers = [i for row in m for i in row]
    return matrix_numbers == temp


def check_magic_matrix(m: list) -> str:
    n = len(m)
    res = 'YES'
    sum_diag_1 = sum([m[i][i] for i in range(n)])
    sum_diag_2 = sum([m[i][n - i - 1] for i in range(n)])
    for i in range(n):
        if sum(m[i]) == sum([m[j][i] for j in range(n)]) == sum_diag_1 == sum_diag_2:
            continue
        else:
            res = 'NO'
            break
    return res


matrix = write_square_matrix(int(input()))
print(check_magic_matrix(matrix) if check_numbers_matrix(matrix) else 'NO')
