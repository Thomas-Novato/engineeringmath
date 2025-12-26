import math


def f(t):
    return 2000 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t


def simpson_rule(f, a, b, n):
    """
    多段辛普森1/3法则 (Multiple Segment Simpson's 1/3rd Rule)

    公式: ∫f(x)dx = (b-a)/(3n) * [f(x₀) + 4*Σf(x_i)(i=odd) + 2*Σf(x_i)(i=even) + f(x_n)]

    其中:
    - x₀ = a, x_n = b
    - 奇数索引点(x₁,x₃,x₅...)权重为4
    - 偶数索引点(x₂,x₄,x₆...)权重为2
    - 端点权重为1
    - n必须是偶数
    """
    if n % 2 != 0:
        n += 1  # 确保n是偶数

    h = (b - a) / n

    # f(x₀) + f(x_n)
    result = f(a) + f(b)

    # 4 * Σf(x_i) for i = 1,3,5,...,n-1 (奇数索引)
    for i in range(1, n, 2):
        x_i = a + i * h
        result += 4 * f(x_i)

    # 2 * Σf(x_i) for i = 2,4,6,...,n-2 (偶数索引)
    for i in range(2, n, 2):
        x_i = a + i * h
        result += 2 * f(x_i)

    # 乘以 (b-a)/(3n) = h/3
    return result * (b - a) / (3 * n)


def adaptive_simpson(f, a, b, tolerance=1e-6, max_iterations=100000):
    print(f"积分区间: [{a}, {b}]")
    print(f"误差容忍值: {tolerance}")
    print(f"{'n (分段数)':<12} {'积分值':<20} {'误差估计':<15}")

    n = 2  # 辛普森法则至少需要2段
    I_prev = simpson_rule(f, a, b, n)
    print(f"{n:<12} {I_prev:<20.10f} {'--':<15}")

    for iteration in range(1, max_iterations):
        n += 2  # 每次增加2（保持偶数）
        I_curr = simpson_rule(f, a, b, n)

        error = abs(I_curr - I_prev)
        print(f"{n:<12} {I_curr:<20.10f} {error:<15.2e}")

        if error < tolerance:
            print(f"[OK] 收敛! 误差 {error:.2e} < {tolerance}")
            print(f"最终分段数 n = {n}")
            print(f"积分结果 = {I_curr:.10f}")
            return I_curr, n, error

        I_prev = I_curr

    print(f"警告：达到最大迭代次数 {max_iterations}，未满足误差要求")
    return I_curr, n, error


if __name__ == "__main__":
    a = 8  # 起始时间 t=8秒
    b = 30  # 结束时间 t=30秒

    tolerance = 1e-6

    result, n_final, final_error = adaptive_simpson(f, a, b, tolerance)

    print(f"火箭从 t={a}s 到 t={b}s 的垂直距离：")
    print(f"x = {result:.6f} 米")
    print(f"使用分段数：n = {n_final}")
    print(f"估计误差：{final_error:.2e}")

    # 两段辛普森积分（用于对比）
    I_2 = simpson_rule(f, a, b, 2)
    print(f"两段辛普森积分结果：x = {I_2:.6f} 米")

    # 计算真实误差和相对误差
    true_error = abs(result - I_2)
    relative_error = abs(true_error / result) if result != 0 else 0
    print(f"真实误差 E_t = |准确值 - 近似值| = {true_error:.6f} 米")
    print(f"绝对相对真实误差 |e_a| = {relative_error:.6f} = {relative_error * 100:.4f}%")
