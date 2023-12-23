import numpy as np #Import modul NumPy untuk manipulasi matriks dan vektor secara efisien.
import sympy as sp #Import modul SymPy untuk manipulasi ekspresi matematika simbolis.
import matplotlib.pyplot as plt # Import modul matplotlib untuk membuat plot.

def my_bisection(f, a, b, e, max, iterasi):
    # Fungsi rekursif untuk metode bisection
    # Input: fungsi f, interval [a, b], toleransi galat e, iterasi maksimum max, dan iterasi saat ini iterasi.
    # Output: akar fungsi (hasil), jumlah iterasi yang dilakukan (iterasi)
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

# Menginput persamaan 
function = input("Masukkan fungsi: ")
a = float(input("Masukkan nilai batas awal: "))
b = float(input("Masukkan nilai batas akhir: "))
epsilon = float(input("Masukkan nilai toleransi galat: "))
max = int(input("Masukkan iterasi maksimum: "))

# Mengubah string menjadi fungsi yang dapat dievaluasi
x = sp.symbols('x')
f = sp.sympify(function)
f = sp.lambdify(x, f)

# Memanggil fungsi my_bisection
r1, i = my_bisection(f, a, b, epsilon, max, 1)

print("r1 =", r1)
print("f(r1) =", f(r1))
print("Iterasi ke-", i)

# Membuat grafik fungsi
x_values = np.linspace(a, b, 1000)
y_values = f(x_values)

plt.figure(figsize=(10, 6)) # Membuat objek gambar dengan ukuran 10x6 inci
plt.plot(x_values, y_values, label='Fungsi') # Menampilkan plot garis fungsi berdasarkan x_values dan y_values

# Menampilkan titik akar pada grafik dengan warna merah
# dan menambahkan label yang mencakup nilai x dan y akar dengan format tertentu
plt.scatter(r1, f(r1), color='red', label=f'Akar (x={r1:.4f}, y={f(r1):.4f})')

# Menyertakan label sumbu x dan y pada grafik:
plt.xlabel('x')
plt.ylabel('f(x)')

plt.axhline(0, color='black', linestyle='--', linewidth=0.7) #Menambahkan garis horizontal pada nilai y=0 sebagai referensi
plt.title('Grafik Fungsi') # Menambahkan judul pada grafik
plt.legend() # Menampilkan legenda yang berisi label-label yang ditetapkan sebelumnya
plt.grid(True) # Menampilkan grid pada grafik
plt.show() # Menampilkan grafik
