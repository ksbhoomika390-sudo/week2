file = open("sample.txt", "w")   # "w" mode creates file if not exists
file.write("Hello, this is my first file in Python.\n")
file.write("I am learning file handling.")
file.close()
print("File created and written successfully.")
