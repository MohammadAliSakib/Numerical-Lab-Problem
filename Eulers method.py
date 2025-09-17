def euler_method(f, x0, y0, h, xn):
    """
    Solve ODE dy/dx = f(x, y) using Euler's Method.

    Args:
        f  : function f(x, y) defining dy/dx
        x0 : initial x value
        y0 : initial y value (y(x0))
        h  : step size
        xn : value of x at which we want y

    Returns:
        (x_values, y_values): lists of x and y values
    """
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    while x < xn:
        y = y + h * f(x, y)  # Euler formula
        x = x + h
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


# ================================
# Example usage
# ================================
if __name__ == "__main__":
    # Example: dy/dx = x + y, with y(0) = 1
    f = lambda x, y: x + y
    x0, y0 = 0, 1  # initial conditions
    h = 0.1  # step size
    xn = 1  # compute up to x = 1

    x_vals, y_vals = euler_method(f, x0, y0, h, xn)

    print("x values:", x_vals)
    print("y values (approx):", y_vals)
