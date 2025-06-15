import numpy as np
import matplotlib.pyplot as plt

# Fungsi x^3 - 4x - 9
def f(x):
    return x**3 - 4*x - 9 

# Implementasi Regula Falsi
def regula_falsi(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Fungsi tidak berubah tanda di [a, b].")
        return None, []

    iterasi = []
    for i in range(max_iter):
        c = b - (f(b)*(a - b)) / (f(a) - f(b))
        iterasi.append((i+1, a, b, c, f(c)))

        if abs(f(c)) < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c, iterasi

# Parameter awal
a = 2
b = 3
akar, data_iterasi = regula_falsi(f, a, b)

print("\nProses Iterasi Regula Falsi:")
print(f"{'Iter':<5}{'a':<10}{'b':<10}{'c':<12}{'f(c)':<12}")
for i, a_i, b_i, c_i, fc in data_iterasi:
    print(f"{i:<5}{a_i:<10.6f}{b_i:<10.6f}{c_i:<12.6f}{fc:<12.6f}")


x_vals = np.linspace(a - 1, b + 1, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)

for i, _, _, c_i, _ in data_iterasi:
    plt.plot(c_i, f(c_i), 'ro')
    plt.text(c_i, f(c_i), f"iter {i}", fontsize=8, ha='right')

plt.title("Grafik Fungsi dan Titik Akar (Regula Falsi)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
