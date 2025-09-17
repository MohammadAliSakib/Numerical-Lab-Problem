import numpy as np


def gauss_seidel(a, b, tolerance=1e-10, max_iterations=100):
    """
    Solves the system of linear equations Ax = b using Gauss-Seidel method.

    Args:
        a: Coefficient matrix (n x n)
        b: Right-hand side vector
        tolerance: Error tolerance for stopping condition
        max_iterations: Maximum number of iterations

    Returns:
        x: Solution vector
    """
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)  # Initial guess (zeros)

    for iteration in range(max_iterations):
        x_new = np.copy(x)

        for i in range(n):
            # Summation of a[i][j] * x[j] for j != i
            s1 = sum(a[i][j] * x_new[j] for j in range(i))  # updated values
            s2 = sum(a[i][j] * x[j] for j in range(i + 1, n))  # old values
            x_new[i] = (b[i] - s1 - s2) / a[i][i]

        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            print(f"\nConverged in {iteration + 1} iterations")
            return x_new

        x = x_new

    raise Exception("Gauss-Seidel method did not converge within the given iterations")


# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Example system:
    # 4x + y + z = 7
    # x + 3y + z = -8
    # x + y + 5z = 6
    a = np.array([[4.0, 1.0, 1.0],
                  [1.0, 3.0, 1.0],
                  [1.0, 1.0, 5.0]])
    b = np.array([7.0, -8.0, 6.0])

    solution = gauss_seidel(a, b)
    print("\nSolution:", solution)
