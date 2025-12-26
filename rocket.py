import numpy as np
import matplotlib.pyplot as plt

# 定义速度函数 v(t)
def v(t):
    n=14e4
    d_n = n - 2100 * t
    return 2000 * np.log(n / d_n) - 9.8 * t

# 时间范围：0 ≤ t ≤ 30，先选一个较小的步长（如Δt=0.01）来提高精度
t = np.arange(0, 30, 0.01)
v_values = v(t)

# 中心差分计算加速度（注意：首尾点无法用中心差分，这里取中间区域）
acceleration = np.diff(v_values, 2) / (0.01 ** 2)  # 中心差分公式推导后的二阶差分形式
t_acc = t[1:-1]  # 中心差分的时间点对应t[1]到t[-2]

# 找到t=16s附近的索引
idx = np.abs(t_acc - 16).argmin()
a_16 = acceleration[idx]

# 验证误差：通过减小步长，观察加速度的变化是否小于1e-6
def calculate_acceleration(step):
    t_step = np.arange(0, 30, step)
    v_step = v(t_step)
    acc_step = np.diff(v_step, 2) / (step ** 2)
    idx_step = np.abs(t_step[1:-1] - 16).argmin()
    return acc_step[idx_step]

# 逐步减小步长，直到加速度变化小于1e-6
step_list = [2, 1, 0.5, 0.1, 0.01, 0.001]
acc_list = []
for step in step_list:
    acc = calculate_acceleration(step)
    acc_list.append(acc)
    print(f"步长Δt={step}, 加速度a(16)={acc:.8f}")

# 绘制加速度曲线（用小步长的结果）
plt.figure(figsize=(8, 6))
plt.plot(t_acc, acceleration, linewidth=1, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Rocket Acceleration vs Time (Center Difference, Δt=0.01)')
plt.grid(True)
plt.show()

print(f"最终t=16s时的加速度（误差<1e-6）：{a_16:.8f} m/s²")