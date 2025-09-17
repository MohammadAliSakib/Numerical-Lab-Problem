import numpy as np


def newton_backward_interpolation(x_values, y_values, x_to_find):
    """
    Newton Backward Interpolation Formula
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

    # Construct backward difference table
    for j in range(1, n):
        for i in range(j, n):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

    # Display backward difference table
    print("\nBackward Difference Table:")
    for i in range(n):
        print(f"{x_values[i]:.2f}", end="\t")
        for j in range(i + 1):
            print(f"{diff_table[i][j]:.4f}", end="\t")
        print()

    # Newton Backward Interpolation
    u = (x_to_find - x_values[-1]) / h
    result = y_values[-1]
    u_term = 1

    for j in range(1, n):
        u_term *= (u + (j - 1)) / j
        result += u_term * diff_table[n - 1][j]

    return result


# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Input values
    x_values = [0, 10, 20, 30, 40]
    y_values = [0, 0.17365, 0.34202, 0.5, 0.64279]  # Example: sin(x) approx in degrees

    x_to_find = 35  # Value to interpolate (closer to last values → use backward)

    result = newton_backward_interpolation(x_values, y_values, x_to_find)
    print(f"\nInterpolated value at x = {x_to_find} is: {result:.5f}")
