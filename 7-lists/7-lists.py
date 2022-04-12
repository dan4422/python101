# types we've seen so far: string, number (floats, integers), boolean
# new type: list

# #empty list
# names = []

# #list of strings
# names = ['tony','steve','tchala']

# #list of integers
# numbers = [2, 4, 6, 8, 9.0]

# #list of mixed values
# weird = ['pancakes',10,True]

# #access items with index inside square brackets
# # print(names[1]) prints steve
# # print(weird[3]) # IndexError, list is not that long
# # print(numbers[-2]) prints 8. starts from the back
# # print(numbers[1:-1])

# # change value at specific position
# names = ['tony','steve','tchala']
# names[0] = 'peter'
# names.append('tony')
# print(names)

# names.insert(0,'bruce')
# print(names)

# fourth = names.pop(3)
# print(names)
# print(fourth)

# tuples
names = ('tony','steve','tchala')
names[0] = 'peter' # error cause you can't edit or add anything inside a tuple