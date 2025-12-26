T = [80, 40, -40, -120, -200, -280, -340]
alpha = [6.47e-6, 6.24e-6, 5.72e-6, 5.09e-6, 4.30e-6, 3.33e-6, 2.45e-6]
n = len(T)

sum_x = 0
for i in range(n):
    sum_x = sum_x + T[i]

sum_x2 = 0
for i in range(n):
    sum_x2 = sum_x2 + T[i] * T[i]

sum_x3 = 0
for i in range(n):
    sum_x3 = sum_x3 + T[i] * T[i] * T[i]

sum_x4 = 0
for i in range(n):
    sum_x4 = sum_x4 + T[i] * T[i] * T[i] * T[i]

sum_y = 0
for i in range(n):
    sum_y = sum_y + alpha[i]

sum_xy = 0
for i in range(n):
    sum_xy = sum_xy + T[i] * alpha[i]

sum_x2y = 0
for i in range(n):
    sum_x2y = sum_x2y + T[i] * T[i] * alpha[i]

A = [
    [n,      sum_x,  sum_x2],
    [sum_x,  sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
]

b = [sum_y, sum_xy, sum_x2y]

aug = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j])
    row.append(b[i])
    aug.append(row)

for k in range(3):
    pivot = aug[k][k]
    for i in range(k + 1, 3):
        factor = aug[i][k] / pivot
        for j in range(k, 4):
            aug[i][j] = aug[i][j] - factor * aug[k][j]

a = [0, 0, 0]
a[2] = aug[2][3] / aug[2][2]
a[1] = (aug[1][3] - aug[1][2] * a[2]) / aug[1][1]
a[0] = (aug[0][3] - aug[0][1] * a[1] - aug[0][2] * a[2]) / aug[0][0]


print(f"a0 = {a[0]:.10e}")
print(f"a1 = {a[1]:.10e}")
print(f"a2 = {a[2]:.10e}")
print(f"\n拟合方程: alpha(T) = {a[0]:.6e} + ({a[1]:.6e}) * T + ({a[2]:.6e}) * T^2")

for i in range(n):
    alpha_pred = a[0] + a[1] * T[i] + a[2] * T[i] * T[i]
    error = alpha[i] - alpha_pred
    print(f"T={T[i]:>4}, 实际={alpha[i]:.6e}, 预测={alpha_pred:.6e}, 误差={error:.6e}")
