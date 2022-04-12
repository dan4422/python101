# while loop
# count = 0
# while count < 10:
#     #code to run
#     print(f'number {count}')
#     count += 1

# # while loop increment by 2
# count = 0
# while count < 10:
#     #code to run
#     print(f'number {count}')
#     count += 2

# condition based on user input
# answer = ''
# while answer != 'bye':
#     print('hello?')
#     answer = input('')

while True:
    choice = input('''
    Choose an option:
    A) say hello
    B) do a dance
    C) quit
    ''')

    if choice == 'A':
        print('Hai')
    elif choice == 'B':
        print('Do a dance!')
    elif choice == 'C':
        break
    else:
        print("that's not an option!")

print('Bye!')