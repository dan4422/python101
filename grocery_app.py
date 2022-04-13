def groceries(groceries):
    print(" ")
    for grocery in groceries:
        print(f"Name of grocery list: {grocery['name'].title()}")
        print("List of grocery items:")
        print(",".join(grocery['items']))
        print(" ")

# create a list of dictionaries that has a name and a list of items
grocery_list = []
while True:
    user_input = input("""Welcome to the Grocery App!
What would you like to do today?
    1. Create a Grocery List
    2. Add items to a Grocery List
    3. Delete items from a Grocery List
    4. View all items from a Grocery List
    5. Delete a Grocery List
    6. View all Grocery List and Items
    7. Exit the app
    """)

    if user_input == '1':
        grocery_name = input('What would you like to name the grocery list?: ')
        grocery_items = input('List the grocery items needed followed by a comma: ')
        items_list = grocery_items.lower().strip(" ").split(",")
        grocery = {"name": grocery_name.lower(), "items": items_list}
        grocery_list.append(grocery)
        print(f'Added a grocery list named {grocery_name}')
    elif user_input == '2':
        grocery_name = input('Name of grocery list you would like to add items to?: ').lower()
        new_grocery_items = input('What items would you like to add?: ')
        list_new_grocery_items = new_grocery_items.lower().strip(" ").split(",")
        for list in grocery_list:
            if grocery_name == list['name']:
                for items in list_new_grocery_items:
                    list['items'].append(items)
        print('Added the new grocery items!')
    elif user_input == '3':
        grocery_name = input('Name of grocery list you would like to delete items from?: ').lower()
        delete_grocery_items = input('List the grocery items you want deleted followed by a comma: ')
        delete_grocery_items_list = delete_grocery_items.lower().strip().split(",")
        for list in grocery_list:
            if grocery_name == list['name']:
                for item in list['items']:
                    if item in delete_grocery_items_list:
                        for item in delete_grocery_items_list:
                            list['items'].remove(item) # deleting the items works but there can be no spaces at all in the list of items when inputting!
        print('Deleted grocery items!')
    elif user_input == '4':
        grocery_name = input('Which grocery list would you like to see the existing items for?: ')
        for list in grocery_list:
            if grocery_name == list['name']:
                print(",".join(list['items']))
    elif user_input == '5':
        grocery_name = input('Which grocery list would you like to delete?: ')
        groceries(grocery_list)
        for list in grocery_list:
            if grocery_name == list['name']:
                i = grocery_list.index(list)
                del grocery_list[i]
        print(f'Deleted grocery list - {grocery_name}')
    elif user_input == '6':
        groceries(grocery_list)
    elif user_input == '7':
        break

print('Thanks for using the Grocery App. Bye!')
