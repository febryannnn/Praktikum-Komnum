import numpy as np
from tabulate import tabulate

# Fungsi yang ingin diintegralkan (misalnya sin(x))
def f(x):
    return np.sin(x)

# Metode Trapezoidal
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

# Metode Romberg
def romberg(f, a, b, max_iter):
    R = np.zeros((max_iter, max_iter))
    trapezoid_values = []

    for i in range(max_iter):
        n = 2 ** i
        R[i, 0] = trapezoidal(f, a, b, n)
        trapezoid_values.append([n, R[i, 0]])
        for k in range(1, i + 1):
            R[i, k] = (4**k * R[i, k-1] - R[i-1, k-1]) / (4**k - 1)

    return R, trapezoid_values

# Parameter integrasi
a = 0
b = np.pi
max_iter = 5


romberg_table, trapezoid_table = romberg(f, a, b, max_iter)

# Mencetak Tabel Trapezoidal
print("\nTabel Trapezoidal:")
print(tabulate(trapezoid_table, headers=["n (interval)", "Hasil Trapezoidal"], tablefmt="grid", floatfmt=".10f"))

# Mencetak Tabel Romberg
print("\nTabel Romberg:")
romberg_data = []

for i in range(max_iter):
    row = []
    for j in range(max_iter):
        if j <= i:
            row.append(f"{romberg_table[i, j]:.10f}")
        else:
            row.append("")
    romberg_data.append(row)

header = [f"k={j}" for j in range(max_iter)]
print(tabulate(romberg_data, headers=header, tablefmt="grid"))
