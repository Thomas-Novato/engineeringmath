import math
def f(x, y):
    return x ** 2 + y ** 2 + 2 * x + 4

def gradi(x, y):
    grad_x = 2 * x + 2
    grad_y = 2 * y
    return [grad_x, grad_y]

def G(x0, y0, dx, dy):
    A = dx ** 2 + dy ** 2
    B = 2 * x0 * dx + 2 * y0 * dy + 2 * dx
    h = -B / (2 * A)
    return h

ini = [100, 2]
iter = 0
err = 1e-6

while True:
    iter += 1
    x0 = ini[0]
    y0 = ini[1]
    c = f(x0, y0)
    print(f"\n第 {iter} 次迭代")
    print(f"当前: ({x0:.6f}, {y0:.6f})")
    print(f"函数值: {c:.6f}")
    grad = gradi(x0, y0)
    maxgrad= math.sqrt(grad[0] ** 2 + grad[1] ** 2)
    if maxgrad < err:
        print("\n梯度0")
        break

    d = [-grad[0], -grad[1]]
    dx, dy = d
    new_h = G(x0, y0, dx, dy)
    print(f"计算梯度: {grad}")
    print(f"步长 h: {new_h:.6f} ")

    x_new = x0 + new_h * dx
    y_new = y0 + new_h * dy
    ini = [x_new, y_new]

fx = ini[0]
fy = ini[1]
min_value = f(fx, fy)
print(f"步长 h: {new_h:.6f} ")
print(f"坐标 (x, y): ({fx:.1f}, {fy:.1f})")
print(f"最小值 : {min_value:.1f}")