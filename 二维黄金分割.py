import math

def f(l, theta):
    return l * math.sin(theta) * (6 - 2 * l + l * math.cos(theta))
def gold(func, a, b, tol=0.0001, direction=""):
    phi = ( math.sqrt(5)-1) / 2  # 黄金
    iter= 1
    while abs(b - a) > tol:
        x1 = a + phi * (b - a)
        x2 = a + (1 - phi) * (b - a)
        f1 = func(x1)
        f2 = func(x2)
        epsilon = abs(b - a)
        print(f"{direction} 迭代次数 {iter}: a={a:.4f}, b={b:.4f}, x1={x1:.4f}, x2={x2:.4f}, f(x1)={f1:.4f}, f(x2)={f2:.4f}, ε={epsilon:.4f}")
        if f1 > f2:
            a = x2
        else:
            b = x1
        iter += 1
    opt_x = (a + b) / 2
    print(f"{direction} Converged at x={opt_x:.4f}, f={func(opt_x):.4f}")
    return opt_x
theta = math.pi / 4
l_min = 0.0
l_max = 3.0
theta_min = 0.01
theta_max = math.pi / 2 - 0.01
tol = 0.0001
max_iter = 10
prev_f = -1
print("开始二维黄金分割优化")
print(f"初始角度: theta = {theta:.4f} rad ({theta * 180 / math.pi:.2f}°)")
print(f"目标容差: {tol}")
for iter in range(1, max_iter + 1):
    print(f"\n--- 二维迭代 {iter}: 沿 l 方向优化 (固定 theta={theta:.4f} rad) ---")
    func_l = lambda l_val: f(l_val, theta)
    l_opt = gold(func_l, l_min, l_max, tol, direction="l-direction")
    print(f"\n--- 二维迭代 {iter}: 沿 theta 方向优化 (固定 l={l_opt:.4f}) ---")
    func_theta = lambda th_val: f(l_opt, th_val)
    theta_opt = gold(func_theta, theta_min, theta_max, tol, direction="theta-direction")
    l = l_opt
    theta = theta_opt
    current_f = f(l, theta)
    print(
            f"\n二维迭代 {iter} 结果: "
            f"l={l:.4f}, "
            f"theta={theta:.4f} rad ({theta * 180 / math.pi:.2f}°), "
            f"f={current_f:.4f}, "
        )
    if abs(current_f - prev_f) < tol:
        print("优化收敛 (函数值变化小于容差)。")
        break
    prev_f = current_f  # 记录当前函数值，用于下一次比较
    print(f"\n--- 优化完成 ---")
    print(f"最终最大值: {current_f:.4f}")
    print(f"在点 (l, theta): ({l:.4f}, {theta * 180 / math.pi:.2f}°)")
