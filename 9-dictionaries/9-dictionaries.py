# # Dictionary syntax

# # #empty dictionary
# # breakfast_order = {}

# # # define data with KEY and VALUE
# # breakfast_order = {
# #     "main": "Short Stack",
# #     "seat": 3,
# #     "table": 10,
# #     "paid": False,
# # }

# # # access data inside a dictionary with the key name inside of square brackets
# # print(f'the main for seat {breakfast_order["seat"]} is {breakfast_order["main"]}')

# # # access data using value of variable as key
# # table = "main"
# # print(breakfast_order[table])

# # # changing the item inside dictionary
# # breakfast_order["main"] = "eggs over easy"

# # # adding another value to dictionary
# # breakfast_order["side"] = "hash brown and bacon"

# # # deleting something in a dictionary
# # # del breakfast_order["side"]

# # # overriding empty data
# # side = breakfast_order["side"] = ""

# # side = breakfast_order.pop("side")

# #
# user = {
#     "email": "tony@starkindustries.com",
#     "name": {
#         "first": "Tony",
#         "last": "Stark"
#     }
# }

# print(user["email"])
# print(user["name"]["first"])

# # accessing nested data
# print(f"Hello {user['name']['first']} {user['name']['last']}")


# foods = [
#     'pancakes',
#     'waffles',
#     'bagels',
#     'pancakes',
#     'waffles'
# ]

# orders = {}

# for food in foods:
#     if food not in orders:
#         orders[food] = 0
#     orders[food] += 1

# print(orders)

# words = "To be or not to be or do be do be do".split()

# freq = {}

# for words in words:
#     if words not in freq:
#         freq[words] = 0
#     freq[words] += 1

# print(freq)

# highest = None
# for word in freq:
#     current_value = freq[word]
#     if (highest == None):
#         highest = word
    
#     if current_value > freq[highest]:
#         highest = word

# print(highest)

# del freq[highest]

# second_highest = None
# highest = None
# for word in freq:
#     current_value = freq[word]
#     if (second_highest == None):
#         second_highest = word
    
#     if current_value > freq[second_highest]:
#         second_highest = word

# print(second_highest)