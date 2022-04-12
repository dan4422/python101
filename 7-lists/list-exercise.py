# working with a list
list = []
print(list)
list.append(1)
print(list)
list.append(55)
print(list)
list.append(67)
print(list)
list.append(77)
print(list)
list.append(23)
print(list)
list.pop(0)
print(list)
list[1] = 17
print(list)
list.pop()
print(list)

#bonus exercise
# How can you take a new values and insert it into the middle of a list?
list.append(99)
midpoint = len(list)/2
list.insert(int(midpoint),'hi')
print(list)
# How can you merge two lists together?
list2 = [33,10,63,82]
list3 = list + list2
print(list3)
# How can you access multiple values from inside an existing list?
print(list[1:4])