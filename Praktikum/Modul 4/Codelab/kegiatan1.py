# Kegiatan 1

# curry function
# def perkalian(a):
#     def dengan(b):
#         return a*b
#     return dengan

# def main():
#     hasil1 = perkalian(5)(1)
#     hasil2 = perkalian(5)(2)
#     hasil3 = perkalian(5)(3)
#     print(hasil1, hasil2, hasil3)

# if __name__ == "__main__":
#     main()

# Hof Function
# def perkalian(a):
#     def dengan(b):
#         return a*b
#     return dengan

# def main():
#     hasil = map(perkalian(5), [1, 2, 3, 4, 5])
#     print(list(hasil))
    
# if __name__ == "__main__":
#     main()



# Kegiatan 1

# curry function
def perkalian(a):
    def dengan(b):
        return a*b
    return dengan


def main():
# # HOF
    hasil = map(perkalian(5), [1, 2, 3, 4, 5])
    print(list(hasil))

# # Curry Function
#     hasil1 = perkalian(5)(1)
#     hasil2 = perkalian(5)(2)
#     hasil3 = perkalian(5)(3)
#     hasil4 = perkalian(5)(4)
#     hasil5 = perkalian(5)(5)
#     print(hasil1, hasil2, hasil3, hasil4, hasil5)

if __name__ == "__main__":
    main()