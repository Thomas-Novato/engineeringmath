import math
def A(theta):
    return 4 * math.sin(theta) * (1 + math.cos(theta))
def gold(f, a, b, eps=1e-2):
    phi = (math.sqrt(5) - 1) / 2
    count = 0
    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)
    f1, f2 = f(x1), f(x2)

    while (b - a) > eps:
        count += 1
        if f1 > f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - phi * (b - a)
            f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + phi * (b - a)
            f2 = f(x2)

    return (a + b) / 2, f((a + b) / 2), count
theta_best, A_max, iterations = gold(A, 0, math.pi/2, eps=1e-2)
print(f"最优角度 θ = {theta_best:.4f}  rad")
print(f"最大截面积 A = {A_max:.4f}")
print(f"迭代次数     = {iterations}")