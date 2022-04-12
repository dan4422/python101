
phonebook = []
while True:
    user_input = input("""
    Electronic Phone Book
    ========================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit

    What do you want to do (1-5)?:
    """)
    if user_input == '1':
        find_name = input('Name?: ')
        for name in phonebook:
            if find_name == name["Name"] :
                print(f'Found Entry for {name["Name"]}: {name["Phone Number"]}')
    elif user_input == '2':
        name = input('Name?: ')
        number = input('Number?: ')
        entered_person = {"Name": name, "Phone Number": number}
        phonebook.append(entered_person)
        print(f'Entry stored for {name}.')
    elif user_input == '3':
        delete_name = input('Name?: ')
        for person in phonebook:
            if  delete_name == person["Name"]:
                i = phonebook.index(person)
                del phonebook[i]
        print(f'Deleted entry for {delete_name}')
    elif user_input == '4':
        for person in phonebook:
            print(f'Found entry for {person["Name"]}: {person["Phone Number"]}')
    elif user_input == '5':
        break
    else:
        print('Try again!')
print('Bye!')

