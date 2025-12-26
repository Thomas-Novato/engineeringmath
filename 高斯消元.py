import math
def gauss(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_row][i]):
                max_row = k
        if max_row != i:
            M[i], M[max_row] = M[max_row], M[i]
        if abs(M[i][i]) < 1e-10:
            print("无唯一解")
            return None

        for j in range(i + 1, n):
            if M[j][i] != 0:
                f = M[j][i] / M[i][i]
                for k in range(i, n + 1):
                    M[j][k] -= f * M[i][k]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - s) / M[i][i]
    return x
A = [
    [20,15, 10],
    [-3, -2.249, 7],
    [5, 1, 3]
]
b = [45, 1.751, 9]
answer = gauss(A, b)
if answer:
    for i, val in enumerate(answer):
        print(f"x{i + 1} = {val:.8f}")