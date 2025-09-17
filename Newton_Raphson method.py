import sympy as sp


def newton_raphson(eq_str, x0, tol=1e-6, max_iter=100):
    # Define symbol and function
    x = sp.Symbol('x')
    f = sp.sympify(eq_str)  # Convert input string to symbolic expression
    f_prime = sp.diff(f, x)  # Derivative

    # Convert symbolic to numerical functions
    f_func = sp.lambdify(x, f, 'math')
    f_prime_func = sp.lambdify(x, f_prime, 'math')

    print(f"{'Iter':<5}{'x':<15}{'f(x)':<15}")

    for i in range(max_iter):
        fx = f_func(x0)
        fpx = f_prime_func(x0)

        if fpx == 0:
            print("Error: Derivative is zero. Method fails.")
            return None

        x1 = x0 - fx / fpx
        print(f"{i + 1:<5}{x0:<15.8f}{fx:<15.8f}")

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1

    return x0


# -------------------------------
# Main Program
# -------------------------------
equation = input("Enter the equation in terms of x (e.g., x**3 - x - 2): ")
x0 = float(input("Enter the initial guess: "))

root = newton_raphson(equation, x0)
if root is not None:
    print("\nApproximate Root:", root)
