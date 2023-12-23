import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt 

def my_bisection(f, a, b, e, max, iterasi):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    m = (a + b) / 2
    if np.abs(f(m)) < e or iterasi >= max:
        return m, iterasi
    elif np.sign(f(a)) == np.sign(f(m)):
        hasil, iterasi = my_bisection(f, m, b, e, max, iterasi + 1)
        return hasil, iterasi
    elif np.sign(f(b)) == np.sign(f(m)):
        hasil, iterasi = my_bisection(f, a, m, e, max, iterasi + 1)
        return hasil, iterasi

function = input("Masukkan fungsi: ")
a = float(input("Masukkan nilai batas awal: "))
b = float(input("Masukkan nilai batas akhir: "))
epsilon = float(input("Masukkan nilai toleransi galat: "))
max = int(input("Masukkan iterasi maksimum: "))

x = sp.symbols('x')
f = sp.sympify(function)
f = sp.lambdify(x, f)

r1, i = my_bisection(f, a, b, epsilon, max, 1)

print("r1 =", r1)
print("f(r1) =", f(r1))
print("Iterasi ke-", i)

x_values = np.linspace(a, b, 1000)
y_values = f(x_values)

plt.figure(figsize=(10, 6)) 
plt.plot(x_values, y_values, label='Fungsi') 

plt.scatter(r1, f(r1), color='red', label=f'Akar (x={r1:.4f}, y={f(r1):.4f})')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.axhline(0, color='black', linestyle='--', linewidth=0.7) 
plt.title('Grafik Fungsi') 
plt.legend() 
plt.grid(True) 
plt.show() 
