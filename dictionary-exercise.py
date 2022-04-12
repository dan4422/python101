# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923',
# }

# print(phonebook_dict['Elizabeth'])

# phonebook_dict['Kareem'] = '938-489-1234'

# del phonebook_dict['Alice']

# phonebook_dict['Bob'] = '968-345-2345'  

# for key in phonebook_dict:
#     print(key,phonebook_dict[key])


# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies','tennis'],
#     'friends': [
#         {'name':'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography','tennis']},
#         {'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies','tv']},
#     ]
# }

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends']['name' == 'Jasmine']['email'])
# print(ramit['friends'][1]['interests'][1])

# Letter Histogram
# user_input = input('Please enter a word: ')
# word = {}
# for letter in user_input:
#     if letter not in word:
#         word[letter] = 0
#     word[letter] += 1

# print(word)

# Word Histogram
# user_input = input('Please enter a sentence: ').lower().split(' ')
# sentence = {}
# for word in user_input:
#     if word not in sentence:
#         sentence[word] = 0
#     sentence[word] += 1

# print(sentence)

# # Bonus: Histogram Tally

# sorted_sentence = sorted(sentence,key = sentence.get, reverse=True)[:3]
# print(sorted_sentence)
# top3 = {}
# for word in sorted_sentence:
#     top3[word] = sentence[word]
# print(top3)

# structuring data

def contact_card(customer_info):
    for data in customer_info:
        print(f'{data}: {customer_info[data]}')

customer = {
    'name':'daniel lee',
    'address':'3444 Dunbar Ln',
    'email': 'dan4422@gmail.com',
    'credit card number': '8888-8888-8888-5577',
    'customer ID': 11111,}

customers = [
    {
    'name':'tom hanks',
    'address':'545 glenridge drive',
    'email': 'thanks@gmail.com',
    'credit card number': '7777-8928-6958-5848',
    'customer ID': 11113},
{
    'name':'magic johnson',
    'address':'615 lakers road',
    'email': 'mjohnson@gmail.com',
    'credit card number': '1313-2222-3451-7818',
    'customer ID': 11114},
{
    'name':'pat riley',
    'address':'515 miami heat lane',
    'email': 'priley@gmail.com',
    'credit card number': '4141-3021-1054-0002',
    'customer ID': 11115},
{
    'name':'jerry west',
    'address':'415 MLK Ln',
    'email': 'jwest@gmail.com',
    'credit card number': '1021-3025-0841-6281',
    'customer ID': 11116}
]

for customer in customers:
    print(contact_card(customer))
    print(' ')

# Bonus: User Input
# user_input = input('What would you like to do?(print/add/find):').lower()
# if user_input == 'print':
#     for names in customers:
#         print(customers['names'])

# print(customers['names'])
