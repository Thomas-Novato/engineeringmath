def print_matrix(matrix):
    for row in matrix:
        print("  ", end="")
        for val in row:
            print(f"{val:10.4f}", end="")

def zhuyuan(A, b):
    n = len(A)
    a = [A[i][:] + [b[i]] for i in range(n)]
    print_matrix(a)

    for i in range(n):
        p = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[p][i]):
                p = j

        if p != i:
            print(f"第 {i + 1} 步: 交换第 {i + 1} 行和第 {p + 1} 行")
            tmp = a[i][:]
            a[i] = a[p][:]
            a[p] = tmp
            print_matrix(a)
            print()

        if abs(a[i][i]) < 1e-10:
            print("无唯一解")
            return None

        print(f"第 {i + 1} 步消元 (主元 = {a[i][i]:.4f}):")
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n + 1):
                a[j][k] -= factor * a[i][k]
        print_matrix(a)

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]
    return x


A = [
    [25, 5, 1],
    [64, 8, 1],
    [144, 12, 1]
]

b = [106.8, 177.2, 279.2]

solution = zhuyuan(A, b)

if solution:
    for i, val in enumerate(solution):
        print()
        print(f"  x{i + 1} = {val:.6f}")



