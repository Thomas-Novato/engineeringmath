import math
def f(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993e-4
def df(x):
    return 3 * x ** 2 - 0.33 * x
# ---------- 主程序 ----------
x = float(input("给一个初值（米，建议 0~0.11）："))
max_step = 20  # 最多跑 20 次
tol = 0.0001  # 0.0001 % 就认为是够了
print("步数\tx (米)\t误差%\t有效位")
for k in range(1, max_step + 1):
    fx = f(x)
    dfx = df(x)

    x_new = x - fx / dfx
    error = abs(x_new - x) / x_new * 100

    print(f"{k}\t{x_new:.7f}\t{error:.2e}")

    # 保护 2：误差足够小就退出
    if error < tol:
        print("------ 收敛！ ------")
        print(f"根 ≈ {x_new:.6f} 米 = {x_new * 100:.4f} 厘米")
        break
    x = x_new
else:
    print("达到最大迭代次数，还没收敛，请检查初值或函数。")