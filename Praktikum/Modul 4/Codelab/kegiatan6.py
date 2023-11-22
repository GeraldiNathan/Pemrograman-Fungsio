# Nim Ganjil
# NIM 351

def point(x,y):
    return x,y

def line_equation_of(x1, y1, M):
    #TODO 1: tulis rumus untuk mendapatkan nilai C disini
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

# Ubah nilai input dengan 3 digit NIM akhir 351
print("Persamaan garis yang melalui titik (3,5) dan bergradien 1:")
print(line_equation_of(3, 5, 1))