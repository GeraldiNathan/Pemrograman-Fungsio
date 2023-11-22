import math

# Funct  Transalasi
def translasi(tx, ty):
    def translasi_poin(x, y):
        return x + tx, y + ty
    return translasi_poin

# Funct Dilatasi
def dilatasi(sx, sy):
    def dilatasi_poin(x, y):
        return x * sx, y * sy
    return dilatasi_poin

# Funct Rotasi
def rotasi(angle):
    def rotate_poin(x, y):
        radian_angle =  math.radians(angle)
        new_x = x * math.cos(radian_angle) - y * math.sin(radian_angle)
        new_y = x * math.sin(radian_angle) + y * math.cos(radian_angle)
        return new_x, new_y
    return rotate_poin

point = (2, 1)

# Translasi
DoTranslasi = translasi(tx=2, ty=-1)
poin_translasi = DoTranslasi(*point)
print(f"Koordinat setelah translasi: {poin_translasi}")

# Dilatasi
DoDilatasi = dilatasi(sx=2, sy=-1)
poin_dilatasi = DoDilatasi(*point)
print(f"Koordinat setelah dilatasi: {poin_dilatasi}")

# Rotasi
DoRotasi = rotasi(angle=30)
poin_rotasi = DoRotasi(*point)
print(f"Koordinat setelah rotasi: {poin_rotasi}")
