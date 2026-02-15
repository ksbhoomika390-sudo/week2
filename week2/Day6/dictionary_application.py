dictionary = {}
while True:
    print("\n---- DICTIONARY MENU ----")
    print("1. Add Word")
    print("2. Search Word")
    print("3. View Dictionary")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        word = input("Enter the word: ")
        meaning = input("Enter the meaning: ")
        dictionary[word] = meaning
        print("Word added successfully!")
    elif choice == "2":
        word = input("Enter the word to search: ")
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found!")
    elif choice == "3":
        print("\n--- Dictionary Words ---")
        for w, m in dictionary.items():
            print(w, ":", m)
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
