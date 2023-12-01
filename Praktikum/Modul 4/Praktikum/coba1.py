import math

def translasi(tx, ty):
    def translasi_poin(x, y):
        return x + tx, y + ty
    return translasi_poin

def rotasi(angle):
    def rotate_poin(x, y):
        radian_angle = math.radians(angle)
        new_x = x * math.cos(radian_angle) - y * math.sin(radian_angle)
        new_y = x * math.sin(radian_angle) + y * math.cos(radian_angle)
        return new_x, new_y
    return rotate_poin

def dilatasi(sx, sy):
    def dilatasi_poin(x, y):
        return x * sx, y * sy
    return dilatasi_poin

x_input = float(input("Masukkan nilai x titik awal: "))
y_input = float(input("Masukkan nilai y titik awal: "))
point = (x_input, y_input)

tx_input = float(input("Masukkan nilai translasi tx: "))
ty_input = float(input("Masukkan nilai translasi ty: "))
DoTranslasi = translasi(tx=tx_input, ty=ty_input)
point = DoTranslasi(*point)

angle_input = float(input("Masukkan nilai rotasi (dalam derajat): "))
DoRotasi = rotasi(angle=angle_input)
point = DoRotasi(*point)

sx_input = float(input("Masukkan nilai dilatasi sx: "))
sy_input = float(input("Masukkan nilai dilatasi sy: "))
DoDilatasi = dilatasi(sx=sx_input, sy=sy_input)
point = DoDilatasi(*point)

print(f"Koordinat setelah transformasi: {point}")
