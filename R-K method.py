def runge_kutta(f, x0, y0, h, xn):
    """
    Solve ODE dy/dx = f(x, y) using 4th Order Runge-Kutta method (RK4).

    Args:
        f  : function f(x, y) defining dy/dx
        x0 : initial x value
        y0 : initial y value (y(x0))
        h  : step size
        xn : value of x up to which we want solution

    Returns:
        (x_values, y_values): lists of x and y values
    """
    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0

    while x < xn:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
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
    x0, y0 = 0, 1  # initial condition
    h = 0.1  # step size
    xn = 1  # compute up to x = 1

    x_vals, y_vals = runge_kutta(f, x0, y0, h, xn)

    print("x values:", x_vals)
    print("y values (approx):", y_vals)
