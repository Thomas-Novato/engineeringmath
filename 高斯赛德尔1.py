import numpy as np
def gauss(A, b, ini, max_iter=100, tolerance=1e-5):
    n = len(b)
    x = ini.copy()
    print(f"k=0: {x}")
    for k in range(1, max_iter + 1):
        x_prev = x.copy()
        x[0] = (b[0] - A[0, 1] * x[1] - A[0, 2] * x[2]) / A[0, 0]
        x[1] = (b[1] - A[1, 0] * x[0] - A[1, 2] * x[2]) / A[1, 1]
        x[2] = (b[2] - A[2, 0] * x[0] - A[2, 1] * x[1]) / A[2, 2]
        print(f"k={k}: {x}")
    print("\n发散。")
    return x
A = np.array([
    [25.0, 5.0, 1.0],
    [64.0, 8.0, 1.0],
    [144.0, 12.0, 1.0]
])
b = np.array([106.8, 177.2, 279.2])
initial_guess = np.array([0.0, 0.0, 0.0])
s = gauss(A, b, initial_guess, max_iter=5)
print(f"a1 ≈ {s[0]:.6f}")
print(f"a2 ≈ {s[1]:.6f}")
print(f"a3 ≈ {s[2]:.6f}")