import numpy as np


def newton_forward_interpolation(x_values, y_values, x_to_find):
    """
    Newton Forward Interpolation Formula
    Args:
        x_values: list of x data points
        y_values: list of y data points (same length as x_values)
        x_to_find: the value of x for which we need y (interpolated)
    Returns:
        interpolated value at x_to_find
    """
    n = len(x_values)
    h = x_values[1] - x_values[0]  # assume equally spaced
    diff_table = np.zeros((n, n))

    # First column is y_values
    diff_table[:, 0] = y_values

    # Construct forward difference table
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # Display difference table
    print("\nForward Difference Table:")
    for i in range(n):
        print(f"{x_values[i]:.2f}", end="\t")
        for j in range(n - i):
            print(f"{diff_table[i][j]:.4f}", end="\t")
        print()

    # Newton Forward Interpolation Formula
    u = (x_to_find - x_values[0]) / h
    result = y_values[0]
    u_term = 1

    for j in range(1, n):
        u_term *= (u - (j - 1)) / j
        result += u_term * diff_table[0][j]

    return result


# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Input values
    x_values = [0, 10, 20, 30, 40]
    y_values = [0, 0.17365, 0.34202, 0.5, 0.64279]  # Example: sin(x) in degrees approx

    x_to_find = 25  # Value to interpolate

    result = newton_forward_interpolation(x_values, y_values, x_to_find)
    print(f"\nInterpolated value at x = {x_to_find} is: {result:.5f}")
