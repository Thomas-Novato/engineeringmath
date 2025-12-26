def la(t_a, t, v, n):
    data = sorted(zip(t, v), key=lambda p: abs(p[0] - t_a))
    selected = sorted(data[:n], key=lambda p: p[0])
    ts = [p[0] for p in selected]
    vs = [p[1] for p in selected]
    v_t = 0
    for i in range(n):
        xi = ts[i]
        yi = vs[i]
        basis = 1.0
        for j in range(n):
            if i != j:
                xj = ts[j]
                term = (t_a - xj) / (xi - xj)
                basis *= term
        con = yi * basis
        v_t += con
    return v_t
time = [0, 10, 15, 20, 22.5, 30]
velocity = [0, 227.04, 362.78, 517.35, 602.97, 901.67]
t_a = 16
try:
    user_n = int(input("请输入插值点数 n : "))

    if user_n < 2:
        print("点数不能少于 2，已自动设为 2。")
        user_n = 2
    if user_n > len(time):
        user_n = len(time)
    result = la(t_a, time, velocity, user_n)
    print(f"\n最终结果: v({t_a}) = {result:.3f} m/s")
except ValueError:
    print("输入错误，请输入整数！")
