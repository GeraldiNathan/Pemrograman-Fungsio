random_list = [105, 3.1, "Hello", 737, "Python",
               2.7, "World", 412, 5.5, "AI", "Geraldi"]

int_dict = {}
float_tuple = ()
str_list = []

for item in random_list:
    if isinstance(item, int):
        # Pisahkan angka menjadi satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[item] = {"ratusan": ratusan,
                          "puluhan": puluhan, "satuan": satuan}
    elif isinstance(item, float):
        # Data float ke dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Data string ke dalam list
        str_list.append(item)

print("Data int dalam bentuk dictionary:", int_dict, end='\n\n\n')
print("\n\nData float dalam bentuk tuple:", float_tuple, end='\n\n\n')
print("\n\nData string dalam bentuk list:", str_list, end='\n')
