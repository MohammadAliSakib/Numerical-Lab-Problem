import numpy as np

def simpsons_one_third(f, a, b, n):
    """
    Approximate integral of f(x) from a to b using Simpson's 1/3 rule.

    Args:
        f: Function to integrate
        a: Lower limit
        b: Upper limit
        n: Number of sub-intervals (must be even)

    Returns:
        Approximate value of the integral
    """
    if n % 2 != 0:
        raise ValueError("Number of sub-intervals (n) must be even for Simpson's 1/3 rule")

    h = (b - a) / n
    result = f(a) + f(b)

    # Odd terms (multiplied by 4)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)

    # Even terms (multiplied by 2)
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)

    result *= h / 3
    return result

# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Example: integrate f(x) = x^2 from 0 to 2
    f = lambda x: x**2
    a, b = 0, 2
    n = 6  # must be even

    integral = simpsons_one_third(f, a, b, n)
    print(f"Approximate integral of f(x) from {a} to {b} is: {integral:.6f}")
