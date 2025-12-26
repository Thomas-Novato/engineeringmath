t_data = [0, 10, 15, 20, 22.5, 30]
v_data = [0, 227.04, 362.78, 517.35, 602.97, 901.67]
t_target = 16
for i in range(len(t_data)):
    print(f"  [{i}] t={t_data[i]}s, v={v_data[i]}m/s")
n = int(input("\n输入阶数n (1, 2, 3...): "))
start_idx = int(input(f"请输入起始点的序号 (需要连续{n+1}个点): "))
t = t_data[start_idx : start_idx + n + 1]
v = v_data[start_idx : start_idx + n + 1]
num_points = n + 1
table = [[0.0] * num_points for _ in range(num_points)]
for i in range(num_points):
    table[i][0] = v[i]
for j in range(1, num_points):
    for i in range(num_points - j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (t[i+j] - t[i])
coeffs = [table[0][j] for j in range(num_points)]
result = coeffs[0]
term = 1.0
for i in range(1, num_points):
    term = term * (t_target - t[i-1])
    result += coeffs[i] * term

print(f"\n在 t = {t_target} s 时，火箭速度 v = {result:.2f} m/s")


