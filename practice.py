grocery_list = [
    {
        'name':'chicken alfredo',
        'items':['chicken','alfredo','pasta', 'basil', 'salt'],
    },
    {
        'name':'chicken fried rice',
        'items':['chicken','rice','eggs','carrots','peas'],
    }
]

x = 'chicken fried rice'
g_list = ['carrots','peas']
for list in grocery_list:
    if x == list['name']:
        for item in list['items']:
            if item in g_list:
                for item in g_list:
                    list['items'].remove(item)

print(grocery_list)