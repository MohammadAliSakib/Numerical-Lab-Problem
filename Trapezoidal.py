import numpy as np


def trapezoidal_rule(f, a, b, n):
    """
    Approximate integral of f(x) from a to b using the trapezoidal rule.

    Args:
        f: Function to integrate
        a: Lower limit
        b: Upper limit
        n: Number of sub-intervals

    Returns:
        Approximate value of the integral
    """
    h = (b - a) / n  # Step size
    result = 0.5 * (f(a) + f(b))  # First and last terms

    for i in range(1, n):
        result += f(a + i * h)

    result *= h
    return result


# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Example: integrate f(x) = x^2 from 0 to 2
    f = lambda x: 1/ (1+x ** 2)
    a, b = 0, 2
    n = 6  # number of sub-intervals

    integral = trapezoidal_rule(f, a, b, n)
    print(f"Approximate integral of f(x) from {a} to {b} is: {integral:.6f}")
