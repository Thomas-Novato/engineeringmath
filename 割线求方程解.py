import math
def f(x):
    return x**3-0.165*x**2+3.993e-4
xi=0.05
x=0.065
#迭代开始
for iter in range(1,10):
    fx=f(x)
    fxi=f(xi)
    a=fx-fxi#分母
    if a==0:
        print("分母为零，错误")
        break
    #割线
    xn=x-fx*(x-xi)/a
    #绝对误差
    error=abs((xn-x)/xn)*100
    if error<10e-6:
        break
    print(f"迭代次数{iter}:")
    print(f"x_{iter+1}={xn:.6f}")
    print(f"绝对误差为：{error:.6f}%")
    xi=x
    x=xn
