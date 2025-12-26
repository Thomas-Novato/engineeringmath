import numpy as np
#定义被积函数
def fun(t):
    term1 = 140000
    term2 = 140000 - 2100 * t
    if term2 <= 0: return 0
    return 2000 * np.log(term1 / term2) - 9.8 * t
#实现复合辛普森 1/3 法则
def fun1(func, a, b, n):
    h = (b - a) / n  #h是每个小子段的宽度
    fab = func(a) + func(b)
    sum0 = 0
    for i in range(1, n, 2):
        sum0 += func(a + i * h)
    fab += 4 * sum0
    even_sum = 0
    for i in range(2, n, 2):
        even_sum += func(a + i * h)
    fab += 2 * even_sum
    return fab * h / 3
#主程序逻辑
a = 8
b = 30
er = 1e-6
n = 2
oldre = fun1(fun, a, b, n)
print(f"{'分段数 n (偶数)':<18} | {'当前积分结果':<20} | {'近似误差 (变动量)':<20}")
print("-" * 65)
print(f"{n:<18} | {oldre:.8f}           | {'N/A':<20}")
# 循环迭代
max_iter = 20  # 设置一个最大迭代次数防止死循环
iter_count = 0
while iter_count < max_iter:
    iter_count += 1
    n1 = n+2
    # 计算新结果
    nr = fun1(fun, a, b, n1)
    aper = abs(nr - oldre)
    # 打印进度
    print(f"{n1:<18} | {nr:.8f} | {aper:.9f}")
    # 检查是否满足精度
    if aper < er:
        print("-" * 65)
        print("计算收敛！")
        print(f"最终使用的分段数 n = {n1}")
        print(f"最终计算结果 (距离 x) ≈ {nr:.8f}")
        break
    oldre = nr
    n = n1