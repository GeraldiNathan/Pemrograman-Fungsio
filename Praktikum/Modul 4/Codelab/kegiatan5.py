# Nim Ganjil
# NIM 351

# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GANJIL

def point(x,y):
  return x,y

def line_equation_of(p1, p2):
    #TODO 1: gunakan inner function dan closure untuk menghitung nilai M
    def calculate_m():
        delta_y = p2[1] - p1[1]
        delta_x = p2[0] - p1[0]
        return delta_y / delta_x
    #TODO 2: panggil fungsi inner untuk mendapatkan nilai M
    M = calculate_m()
    #TODO 3: tulis rumus untuk mendapatkan nilai C disini
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A(1,3) dan B(5,1):")
print(line_equation_of(point(1,3),point(5,1))) 
#ubah nilai input dengan 4 digit nim akhir kalian
#dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
#untuk membuktikan bahwa output sudah benar

# # manual
x1, y1 = (1, 3)
x2, y2 = (5, 1)
m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1
print (f"y = {m:.2f}x + {c:.2f}")