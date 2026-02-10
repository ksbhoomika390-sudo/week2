n=int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)
numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)
print("Descending order:", numbers)