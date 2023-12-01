import matplotlib.pyplot as plt
import numpy as np

grafik1 = np.array([3, 8, 1, 10])
grafik2 = np.array([6, 2, 7, 11])
grafik3 = np.array([10, 2, 4, 7]) #penambahan array

plt.plot(grafik1, label='Grafik 1', marker='X', color="red", ls="dotted")
plt.plot(grafik2, label='Grafik 2', color="blue")
plt.plot(grafik3, label='Grafik 3', marker='*', ls="dashed", color="green")

# plt.title("Plot Tiga Garis")
# plt.xlabel("Nilai x")
# plt.ylabel("Nilai y")

plt.legend()
plt.show()