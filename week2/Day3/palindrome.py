string = input("Enter a string: ")
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
