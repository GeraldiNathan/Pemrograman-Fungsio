import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 8, 10])
# ypoints = np.array([3, 10, 5])

# plt.figure(figsize=(5,5))
# plt.plot(xpoints, ypoints, color="red")

# plt.xlim([0, 16])
# plt.ylim([0, 16])
# plt.show()

#modifikasi
xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, marker="D", color="blue", ls="dotted", linewidth="3")

plt.xlim([0, 16])
plt.ylim([0, 16])
plt.show()
