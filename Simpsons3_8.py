import numpy as np

def simpsons_three_eighth(f, a, b, n):
    """
    Approximate integral of f(x) from a to b using Simpson's 3/8 rule.

    Args:
        f: Function to integrate
        a: Lower limit
        b: Upper limit
        n: Number of sub-intervals (must be a multiple of 3)

    Returns:
        Approximate value of the integral
    """
    if n % 3 != 0:
        raise ValueError("Number of sub-intervals (n) must be a multiple of 3 for Simpson's 3/8 rule")

    h = (b - a) / n
    result = f(a) + f(b)

    # Terms where index is not multiple of 3 (multiplied by 3)
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            result += 2 * f(x)
        else:
            result += 3 * f(x)

    result *= (3 * h) / 8
    return result

# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Example: integrate f(x) = x^3 from 0 to 1
    f = lambda x: x**3
    a, b = 0, 1
    n = 6  # must be multiple of 3

    integral = simpsons_three_eighth(f, a, b, n)
    print(f"Approximate integral of f(x) from {a} to {b} is: {integral:.6f}")
