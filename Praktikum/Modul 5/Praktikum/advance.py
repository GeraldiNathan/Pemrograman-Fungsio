# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import norm

# # Data tinggi badan individu dalam sentimeter
# tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
# interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# # TODO 1: Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
# def group_into_intervals(data, interval_size):
#     intervals = []
#     for i in range(min(data), max(data) + interval_size, interval_size):
#         intervals.append((i, i + interval_size))
#     return intervals

# # TODO 2: Menghitung frekuensi tinggi badan dalam interval
# def calculate_frequencies(data, intervals):
#     frequencies = [0] * len(intervals)
#     for height in data:
#         for i, interval in enumerate(intervals):
#             if interval[0] <= height < interval[1]:
#                 frequencies[i] += 1
#                 break
#     return frequencies

# # Menentukan interval dan menghitung frekuensi
# intervals = group_into_intervals(tinggi_badan, interval_size)
# frequencies = calculate_frequencies(tinggi_badan, intervals)

# # TODO 3: Visualisasi data dalam bentuk histogram
# plt.bar([f'{i[0]}-{i[1]}' for i in intervals], frequencies, color='blue', alpha=0.7, label='Data Asli')

# # TODO 4: Menambahkan kurva PDF pada hasil visualisasi data
# mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mu, std) * len(tinggi_badan) * interval_size  # Normalisasi berdasarkan jumlah data dan lebar interval
# plt.plot(x, p, 'k', linewidth=2, label='PDF')

# # Menambahkan label dan legend
# plt.xlabel('Interval Tinggi Badan (cm)')
# plt.ylabel('Frekuensi')
# plt.title('Histogram dan Kurva PDF Tinggi Badan')
# plt.legend()

# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def group_heights(heights, interval_size):
    grouped_heights = {}
    
    for height in heights:
        group_key = (height // interval_size) * interval_size
        if group_key not in grouped_heights:
            grouped_heights[group_key] = {'interval': f"{group_key}-{group_key + interval_size - 1}", 'frequencies': 0}
        grouped_heights[group_key]['frequencies'] += 1
    
    return grouped_heights

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

grouped_heights = group_heights(tinggi_badan, interval_size)

for group_key, data in grouped_heights.items():
    print(f"Interval {data['interval']} : {data['frequencies']} orang")

plt.hist(tinggi_badan, bins=range(150, 199, interval_size), density=True)

mean_tinggi = np.mean(tinggi_badan)
std_tinggi = np.std(tinggi_badan)

x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
plt.plot(x, norm.pdf(x, mean_tinggi, std_tinggi), label='PDF', linewidth=2,  color="orange")

plt.xlabel('Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Tinggi Badan')

plt.legend()
plt.show()