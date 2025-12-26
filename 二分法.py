import math

def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

a, b = 0.0623, 0.0624          # 初始区间
iterations = []           # 保存每次结果
c_old = None              # 用于误差计算

for k in range(1, 20):     # 只跑 19次迭代
    c = (a + b)/2
    fc = f(c)
    if k == 1:
        eps_a, sig = None, None
    else:
        eps_a = abs((c - c_old)/c)*100
        sig = max(0, int(-math.log10(eps_a/0.5)))  # 有效位公式
    iterations.append((k, c, fc, eps_a, sig))
    # 缩小区间
    if f(a)*fc < 0:
        b = c
    else:
        a = c
    c_old = c

# 打印
print("iter    c (m)        f(c)        |ε_a|%  sig_dig")
for k, c, fc, eps, sig in iterations:
    if eps is None:
        print(f"{k:4d}  {c:.8f}  {fc:+.2e}    N/A    N/A")
    else:
        print(f"{k:4d}  {c:.8f}  {fc:+.2e}  {eps:6.2f}    {sig}")