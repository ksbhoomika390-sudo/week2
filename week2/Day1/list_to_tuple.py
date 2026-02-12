n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    value = int(input("Enter element: "))
    my_list.append(value)

my_tuple = tuple(my_list)

print("Tuple:", my_tuple)