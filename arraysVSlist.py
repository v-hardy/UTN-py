import array

# Lista en Python
my_list = [1, 2, 3, 4, 5]

# Array en Python
my_array = array.array('i', [1, 2, 3, 4, 5])

print("Tamaño de lista:", my_list.__sizeof__())
print("Tamaño de array:", my_array.__sizeof__())
