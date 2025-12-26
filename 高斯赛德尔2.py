import numpy as np


class LUDecomposition:
    def __init__(self, matrix, rhs):
        # 强制转换为 float 类型，避免整数运算带来的潜在问题
        self.A = np.array(matrix, dtype=float)
        self.b = np.array(rhs, dtype=float)
        self.n = len(self.b)

        # 初始化 L 和 U
        self.L = np.zeros((self.n, self.n))
        self.U = np.zeros((self.n, self.n))

    def decompose(self):
        """执行 LU 分解"""
        n = self.n

        # 初始化 L 的对角线为 1.0 (Doolittle 算法)
        np.fill_diagonal(self.L, 1.0)

        for k in range(n):
            # 1. 计算 U 的第 k 行: U[k, j]
            # 对应 C++: for (int j = k; j < n; j++)
            for j in range(k, n):
                sum_val = 0.0
                # 对应 C++: for (int p = 0; p < k; p++)
                for p in range(k):
                    sum_val += self.L[k, p] * self.U[p, j]
                self.U[k, j] = self.A[k, j] - sum_val

            # 2. 计算 L 的第 k 列: L[i, k]
            # 对应 C++: for (int i = k + 1; i < n; i++)
            for i in range(k + 1, n):
                sum_val = 0.0
                # 对应 C++: for (int p = 0; p < k; p++)
                for p in range(k):
                    sum_val += self.L[i, p] * self.U[p, k]

                if self.U[k, k] == 0:
                    raise ValueError("除以零错误：主元为 0")
                self.L[i, k] = (self.A[i, k] - sum_val) / self.U[k, k]

    def forward_substitution(self):
        """求解 LZ = b (前向替换)"""
        n = self.n
        Z = np.zeros(n)

        print("=== Solving LZ = b (Forward Substitution) ===")

        for i in range(n):
            sum_val = 0.0
            # 模拟 C++ 的输出格式
            print(f"Z{i + 1} = {self.b[i]:.4f}", end="")

            for j in range(i):
                print(f" - {self.L[i, j]:.4f} * {Z[j]:.4f}", end="")
                sum_val += self.L[i, j] * Z[j]

            Z[i] = (self.b[i] - sum_val) / self.L[i, i]  # L[i,i] 恒为 1
            print(f" = {self.b[i]:.4f} - {sum_val:.4f} = {Z[i]:.4f}")

        print()
        return Z

    def backward_substitution(self, Z):
        """求解 UX = Z (后向替换)"""
        n = self.n
        X = np.zeros(n)

        print("=== Solving UX = Z (Backward Substitution) ===")

        # 从最后一行往回遍历: n-1, n-2, ..., 0
        for i in range(n - 1, -1, -1):
            sum_val = 0.0
            print(f"Equation {n - i}: ", end="")

            # 打印方程部分
            first_term = True
            for j in range(i, n):
                if self.U[i, j] != 0:
                    val = self.U[i, j]
                    if not first_term and val > 0:
                        print(" + ", end="")
                    if val < 0:
                        print(" - ", end="")
                    print(f"{abs(val):.4f} * x{j + 1}", end="")
                    first_term = False
            print(f" = {Z[i]:.4f}")

            # 计算 X[i]
            for j in range(i + 1, n):
                sum_val += self.U[i, j] * X[j]

            X[i] = (Z[i] - sum_val) / self.U[i, i]
            print(f"x{i + 1} = ({Z[i]:.4f} - {sum_val:.4f}) / {self.U[i, i]:.4f} = {X[i]:.4f}")
            print()

        return X

    def solve_photo_equations(self):
        """
        对应 C++ 中的 solvePhotoEquations 函数
        这里是硬编码的数值，用于展示特定的计算步骤
        """
        print("=== Solving Equations from Photo ===")
        X = np.zeros(3)

        # Equation 3
        print("Equation 3: 0.7 * x3 = 0.735")
        X[2] = 0.735 / 0.7
        print(f"x3 = 0.735 / 0.7 = {X[2]:.4f}\n")

        # Equation 2
        print("Equation 2: -4.8 * x2 - 1.56 * x3 = -96.21")
        print(f"-4.8 * x2 - 1.56 * {X[2]:.4f} = -96.21")
        temp = -96.21 + 1.56 * X[2]
        print(f"-4.8 * x2 = -96.21 + {1.56 * X[2]:.4f} = {temp:.4f}")
        X[1] = temp / (-4.8)
        print(f"x2 = {temp:.4f} / (-4.8) = {X[1]:.4f}\n")

        # Equation 1
        print("Equation 1: 25 * x1 + 5 * x2 + x3 = 106.8")
        print(f"25 * x1 + 5 * {X[1]:.4f} + {X[2]:.4f} = 106.8")
        temp = 106.8 - 5 * X[1] - X[2]
        print(f"25 * x1 = 106.8 - {5 * X[1]:.4f} - {X[2]:.4f} = {temp:.4f}")
        X[0] = temp / 25
        print(f"x1 = {temp:.4f} / 25 = {X[0]:.4f}\n")

        print("Final Solution from Photo Equations:")
        print(f"x1 = {X[0]:.4f}")
        print(f"x2 = {X[1]:.4f}")
        print(f"x3 = {X[2]:.4f}\n")

    def print_matrix(self, matrix, name):
        """辅助函数：打印矩阵"""
        print(f"{name}:")
        for row in matrix:
            for val in row:
                print(f"{val:10.4f} ", end="")
            print()
        print()

    def print_vector(self, vec, name):
        """辅助函数：打印向量"""
        print(f"{name}:")
        for val in vec:
            print(f"{val:10.4f} ", end="")
        print("\n")


# --- 主程序入口 ---
if __name__ == "__main__":
    print("=== LU Decomposition Example ===")

    # 定义数据
    A_data = [
        [25, 5, 1],
        [64, 8, 1],
        [144, 12, 1]
    ]
    b_data = [106.8, 177.2, 279.2]

    # 实例化求解器
    lu = LUDecomposition(A_data, b_data)

    # 打印初始状态
    lu.print_matrix(lu.A, "Initial matrix A")
    lu.print_vector(lu.b, "Vector b")

    # 1. 执行分解
    lu.decompose()

    # 打印 L 和 U
    lu.print_matrix(lu.L, "L matrix")
    lu.print_matrix(lu.U, "U matrix")

    # 2. 前向替换
    Z = lu.forward_substitution()
    lu.print_vector(Z, "Z vector (from LZ = b)")

    # 3. 后向替换
    X = lu.backward_substitution(Z)
    lu.print_vector(X, "X vector (solution from UX = Z)")

    # 4. 执行硬编码的示例求解 (对应 C++ 中的 solvePhotoEquations)
    lu.solve_photo_equations()

    # 5. 验证结果
    print("=== Verification (A * X) ===")
    verification = np.dot(lu.A, X)
    for i, val in enumerate(verification):
        print(f"Row {i + 1}: {val:.4f} (expected: {lu.b[i]:.4f})")