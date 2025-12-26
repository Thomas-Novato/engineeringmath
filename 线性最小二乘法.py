theta = [0.698132, 0.959931, 1.134464, 1.570796, 1.919862]
T = [0.188224, 0.209138, 0.230052, 0.250965, 0.313707]
n = len(theta)
sum_x = 0
for i in range(n):
    sum_x = sum_x + theta[i]
sum_y = 0
for i in range(n):
    sum_y = sum_y + T[i]
sum_x2 = 0
for i in range(n):
    sum_x2 = sum_x2 + theta[i] * theta[i]
sum_xy = 0
for i in range(n):
    sum_xy = sum_xy + theta[i] * T[i]
fenmu = n * sum_x2 - sum_x * sum_x
a1_fenzi = n * sum_xy - sum_x * sum_y
a1 = a1_fenzi / fenmu
a0_fenzi = sum_x2 * sum_y - sum_x * sum_xy
a0 = a0_fenzi / fenmu
print(f"k1 (截距) = {a0:.6f}")
print(f"k2 (斜率) = {a1:.6f}")
print(f"拟合直线方程: T = {a0:.6f} + {a1:.6f} * theta")
