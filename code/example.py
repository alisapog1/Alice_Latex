import numpy as np

def euler_method(f, y0, t0, t_end, h):
    """
    Реализация явного метода Эйлера.

    Параметры:
    f: функция правой части dy/dt = f(t, y)
    y0: начальное значение y(t0)
    t0: начальное время
    t_end: конечное время
    h: шаг интегрирования

    Возвращает:
    t_values: массив моментов времени
    y_values: массив приближенных значений решения
    """
    n_steps = int((t_end - t0) / h) + 1
    t_values = np.linspace(t0, t_end, n_steps)
    y_values = np.zeros(n_steps)
    y_values[0] = y0

    for i in range(1, n_steps):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])

    return t_values, y_values
