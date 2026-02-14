try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("You are not eligible to vote.")
    print("You can vote.")
except Exception as e:
    print("Error:", e)