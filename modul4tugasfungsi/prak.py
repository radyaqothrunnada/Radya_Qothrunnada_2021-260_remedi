import math

def point(x, y):
    return x, y

def line_equation_of_two_points(p1, p2):
    M = (p2[1] - p1[1]) / (p2[0] - p1[0])
    C = p1[1] - M * p1[0]
    return M, C

def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        return x + tx, y + ty
    return transformasi

def rotasi(sudut):
    def transformasi(p):
        x, y = p
        radian = math.radians(sudut)
        x_baru = x * math.cos(radian) - y * math.sin(radian)
        y_baru = x * math.sin(radian) + y * math.cos(radian)
        return x_baru, y_baru
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        return x * sx, y * sy
    return transformasi


def transformasi_gabungan(*transforms):
    def gabung_transformasi(p):
        for transformasi in transforms:
            p = transformasi(p)
        return p
    return gabung_transformasi


def dekorator_transformasi_gabungan(func):
    def wrapper(p1, p2):

        tx, ty, sx, sy, sudut_rotasi = 2.0, -3.0, 1.5, 2.0, 60.0

        translasi_transform = translasi(tx, ty)
        dilatasi_transform = dilatasi(sx, sy)
        rotasi_transform = rotasi(sudut_rotasi)

        p1_transformed_translasi = translasi_transform(p1)
        p2_transformed_translasi = translasi_transform(p2)

        p1_transformed_rotasi = rotasi_transform(p1_transformed_translasi)
        p2_transformed_rotasi = rotasi_transform(p2_transformed_translasi)

        p1_transformed_dilatasi = dilatasi_transform(p1_transformed_rotasi)
        p2_transformed_dilatasi = dilatasi_transform(p2_transformed_rotasi)

        print(
            f"\n========== Persamaan garis yang melalui titik A{p1} dan B{p2}: ==========")
        M, C = line_equation_of_two_points(p1, p2)
        print(f"\t\t\t\t\t\t\t\ty = {M:.2f} + {C:.2f}\n")

        print("1.\ta. Koordinat kedua titik setelah translasi:")
        M_translasi, C_translasi = line_equation_of_two_points(
            p1_transformed_translasi, p2_transformed_translasi)
        print(f"\tA{p1_transformed_translasi}, B{p2_transformed_translasi}")
        print("\tb. Persamaan garis setelah translasi : ")
        print(f"\ty = {M_translasi:.2f}x + {C_translasi:.2f}\n")

        print("2.\ta. Koordinat kedua titik setelah rotasi:")
        M_rotasi, C_rotasi = line_equation_of_two_points(
            p1_transformed_rotasi, p2_transformed_rotasi)
        print(f"\tA{p1_transformed_rotasi}, B{p2_transformed_rotasi}")
        print("\tb. Persamaan garis setelah rotasi: ")
        print(f"\ty = {M_rotasi:.2f}x + {C_rotasi:.2f}\n")

        print("3.\ta. Koordinat kedua titik setelah dilatasi :")
        M_dilatasi, C_dilatasi = line_equation_of_two_points(
            p1_transformed_dilatasi, p2_transformed_dilatasi)
        print(f"\tA{p1_transformed_dilatasi}, B{p2_transformed_dilatasi}")
        print("\tb. Persamaan garis setelah dilatasi : ")
        print(f"\ty = {M_dilatasi:.2f}x + {C_dilatasi:.2f}\n")

        return func(p1_transformed_rotasi, p2_transformed_rotasi)
    return wrapper

@dekorator_transformasi_gabungan
def apply_transformations(p1, p2):
    M, C = line_equation_of_two_points(p1, p2)
    return M, C


# Contoh penggunaan
p1_x = float(input("Masukkan koordinat x untuk p1: "))
p1_y = float(input("Masukkan koordinat y untuk p1: "))
p2_x = float(input("Masukkan koordinat x untuk p2: "))
p2_y = float(input("Masukkan koordinat y untuk p2: "))

p1 = point(p1_x, p1_y)
p2 = point(p2_x, p2_y)

equation_transformed = apply_transformations(p1, p2)