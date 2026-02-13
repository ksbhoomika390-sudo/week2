with open("sample.txt", "r") as file:
    text="Hi am bhoomika.\nI am learning file handling."
    line = file.readline()
    print(text,line)