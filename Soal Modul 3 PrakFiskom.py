import numpy as np
import matplotlib.pyplot as plt

g = 9.8       # percepatan gravitasi (m/s^2)
h0 = 42       # ketinggian awal (meter)

# 1. Hitung waktu jatuh
t_fall = (2 * h0 / g) ** 0.5
print("Waktu untuk benda mencapai tanah: {:.2f} detik".format(t_fall))

# 2. Fungsi untuk kecepatan dan posisi
def hitung_kecepatan(g, t):
    return g * t

def hitung_posisi(h0, g, t):
    return h0 - 0.5 * g * t**2

# Buat array waktu mulai dari 0 hingga t_fall
t_values = np.linspace(0, t_fall, 500)

# Hitung kecepatan dan posisi untuk setiap waktu
kecepatan_values = hitung_kecepatan(g, t_values)
posisi_values = hitung_posisi(h0, g, t_values)

# 3. Plot Grafik Kecepatan dan Posisi
plt.figure(figsize=(10, 5))

# Grafik kecepatan
plt.subplot(1, 2, 1)
plt.plot(t_values, kecepatan_values, color="blue")
plt.title("Kecepatan terhadap Waktu")
plt.xlabel("Waktu (detik)")
plt.ylabel("Kecepatan (m/s)")
plt.grid(True)

# Grafik posisi
plt.subplot(1, 2, 2)
plt.plot(t_values, posisi_values, color="red")
plt.title("Posisi terhadap Waktu")
plt.xlabel("Waktu (detik)")
plt.ylabel("Posisi (meter)")
plt.grid(True)

# Tampilkan grafik
plt.tight_layout()
plt.show()
