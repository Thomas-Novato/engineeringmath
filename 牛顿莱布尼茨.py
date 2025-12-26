import math
def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4
def df(x):
    return 3*x**2 - 0.33*x
def nt(x0, tol=1e-8, max_iter=50):
#    tol: 相对误差阈值（默认 1e-8，约 0.000 01 %）
#   max_iter: 最大迭代次数
#    返回: (根, 迭代次数, 误差%, 有效位)
    x = x0
    for k in range(1, max_iter+1):
        fx  = f(x)
        dfx = df(x)
        if dfx == 0:                       # 导数为 0 无法继续
            raise ZeroDivisionError("导数为 0，不能再使用牛莱")
        x_new = x - fx / dfx               # 核心迭代公式
        eps_a = abs((x_new - x) / x_new)*100
        sig   = max(0, int(-math.log10(eps_a / 0.5)))
        if eps_a < tol*100:                # 相对误差 < 阈值
            return x_new, k, eps_a, sig
        x = x_new

# ----------------- 运行 -----------------
if __name__ == "__main__":
    x0 = 0.062                # 初值：物理上根在 4 cm 左右，0.06 m 足够近
    root, n_iter, eps_a, sig = nt(x0)
    print(f"牛顿法结果：")
    print(f"  根 x = {root:.8f} m  ({root*100:.4f} cm)")
    print(f"  迭代次数：{n_iter}")
    print(f"  相对误差：{eps_a:.4e} %")
    print(f"  至少正确有效位：{sig}")
    print(f"  验证 f(x) = {f(root):.4e}")