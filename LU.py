import numpy as np
class LUDecomposition:
    def __init__(self, matrix, rhs):
        # 将输入转换为 NumPy 数组        self.A = np.array(matrix, dtype=float)
        self.b = np.array(rhs, dtype=float)
        self.n = self.A.shape[0]

        # 初始化 L 和 U 矩阵
        self.L = np.zeros((self.n, self.n))
        self.U = np.zeros((self.n, self.n))

    def decompose(self):
        """执行 LU 分解 (A = L * U)。"""

        # L 的对角线元素初始化为 1 (Doolittle 方法)
        np.fill_diagonal(self.L, 1.0)

        for k in range(self.n):
            # 1. 计算 U 矩阵的第 k 行 U[k, j]
            # U[k, j] = A[k, j] - sum(L[k, p] * U[p, j] for p in 0..k-1)
            for j in range(k, self.n):
                sum_val = np.dot(self.L[k, :k], self.U[:k, j])
                self.U[k, j] = self.A[k, j] - sum_val

            # 2. 计算 L 矩阵的第 k 列 L[i, k]
            # L[i, k] = (A[i, k] - sum(L[i, p] * U[p, k] for p in 0..k-1)) / U[k, k]
            for i in range(k + 1, self.n):
                sum_val = np.dot(self.L[i, :k], self.U[:k, k])

                # 防止除以零
                if self.U[k, k] == 0:
                    raise ValueError(f"在 U[{k},{k}] 处遇到零主元，LU 分解失败或需要进行枢轴选择 (pivoting)。")

                self.L[i, k] = (self.A[i, k] - sum_val) / self.U[k, k]

    def forward_substitution(self):
        """求解 LZ = b (正向替换)。"""
        Z = np.zeros(self.n)

        print("=== 求解 LZ = b (正向替换) ===")
        for i in range(self.n):
            # Z[i] = (b[i] - sum(L[i, j] * Z[j] for j in 0..i-1)) / L[i, i]

            # 由于 L[i, i] 总是 1.0，我们可以简化除法。
            sum_val = np.dot(self.L[i, :i], Z[:i])
            Z[i] = (self.b[i] - sum_val) / self.L[i, i]

            # 打印 C++ 代码中的详细步骤
            print(f"Z{i + 1} = {self.b[i]} - {sum_val:.4f} = {Z[i]:.4f}")

        print()
        return Z

    def backward_substitution(self, Z):
        """求解 UX = Z (反向替换)。"""
        X = np.zeros(self.n)

        print("=== 求解 UX = Z (反向替换) ===")
        # 从最后一行开始向上迭代
        for i in range(self.n - 1, -1, -1):
            # X[i] = (Z[i] - sum(U[i, j] * X[j] for j in i+1..n-1)) / U[i, i]

            sum_val = np.dot(self.U[i, i + 1:], X[i + 1:])

            # 打印 C++ 代码中的方程
            equation_str = f"Equation {self.n - i}: "
            for j in range(i, self.n):
                term = self.U[i, j]
                if term != 0:
                    if j == i:
                        equation_str += f"{term:.4f} * x{j + 1}"
                    else:
                        sign = " + " if term >= 0 else " - "
                        equation_str += f"{sign}{abs(term):.4f} * x{j + 1}"
            print(f"{equation_str} = {Z[i]:.4f}")

            # 求解 X[i]
            if self.U[i, i] == 0:
                raise ValueError("遇到零主元，无法求解。")

            X[i] = (Z[i] - sum_val) / self.U[i, i]

            print(f"x{i + 1} = ({Z[i]:.4f} - {sum_val:.4f}) / {self.U[i, i]:.4f} = {X[i]:.4f}")
            print()

        return X

    def solve_photo_equations(self):

        X = np.zeros(3)

        print("Equation 3: 0.7 * x3 = 0.735")
        X[2] = 0.735 / 0.7
        print(f"x3 = 0.735 / 0.7 = {X[2]:.4f}\n")

        print(f"Equation 2: -4.8 * x2 - 1.56 * x3 = -96.21")
        temp = -96.21 + 1.56 * X[2]
        X[1] = temp / (-4.8)
        print(f"x2 = {temp:.4f} / (-4.8) = {X[1]:.4f}\n")

        print(f"Equation 1: 25 * x1 + 5 * x2 + x3 = 106.8")
        temp = 106.8 - 5 * X[1] - X[2]
        X[0] = temp / 25
        print(f"x1 = {temp:.4f} / 25 = {X[0]:.4f}\n")

        print("最终结果 (来自硬编码中间步骤):")
        print(f"x1 = {X[0]:.4f}, x2 = {X[1]:.4f}, x3 = {X[2]:.4f}")

    def print_matrix(self, matrix, name):
        print(f"\n{name} 矩阵:")
        # 使用 NumPy 打印格式化矩阵
        print(np.array2string(matrix, formatter={'float_kind': lambda x: f"{x:10.4f}"}))

    def print_vector(self, vec, name):
        print(f"\n{name} 向量:")
        print(np.array2string(vec, formatter={'float_kind': lambda x: f"{x:10.4f}"}))


if __name__ == "__main__":

    A = [
        [25, 5, 1],
        [64, 8, 1],
        [144, 12, 1]
    ]

    b = [106.8, 177.2, 279.2]

    lu_solver = LUDecomposition(A, b)

    lu_solver.print_matrix(lu_solver.A, "初始矩阵 A")
    lu_solver.print_vector(lu_solver.b, "向量 b")

    lu_solver.decompose()
    lu_solver.print_matrix(lu_solver.L, "L 矩阵 (下三角)")
    lu_solver.print_matrix(lu_solver.U, "U 矩阵 (上三角)")

    Z = lu_solver.forward_substitution()
    lu_solver.print_vector(Z, "Z 向量 (来自 LZ = b)")

    X = lu_solver.backward_substitution(Z)
    lu_solver.print_vector(X, "X 向量 (最终解)")

    print("=== 验证 (A * X) ===")
    A_np = np.array(A)
    X_np = np.array(X)
    verification = A_np @ X_np

    for i in range(len(b)):
        print(f"第 {i + 1} 行: {verification[i]:.4f} (期望值: {b[i]:.4f})")
