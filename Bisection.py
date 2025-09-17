def f(x, eq):
    return eval(eq)


def bisection(eq, a, b, tol=1e-6, max_iter=100):
    if f(a, eq) * f(b, eq) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iter':<5}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c, eq)
        print(f"{i + 1:<5}{a:<12.6f}{b:<12.6f}{c:<12.6f}{fc:<12.6f}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        if f(a, eq) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


# -------------------------------
# Main Program
# -------------------------------
equation = input("Enter the equation in terms of x (e.g., x**3 - x - 2): ")
a = float(input("Enter the lower bound (a): "))
b = float(input("Enter the upper bound (b): "))

root = bisection(equation, a, b)
if root is not None:
    print("\nApproximate Root:", root)
