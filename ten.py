#set 
set = {1,3,5,7,9}

print("Set:", set)
set.add(11)
print("Set after adding 11:", set)
set.add('Hello')
set.add('World') 
print("Set after adding 'Hello' and 'World':", set)
set.remove(5)
print("Set after removing 5:", set)
set.union({2,4,6})
print("Set after union with {2,4,6}:", set)
set.intersection({1,2,3})
print("Set after intersection with {1,2,3}:", set)
print("Is 3 in the set?", 3 in set)

print("Type of set:", type(set))

#list

list = [1,2,3,4,5]
print("List:", list)
list.append(6)
print("List after appending 6:", list)
list.remove(3)
print("List after removing 3:", list)
print("Is 4 in the list?", 4 in list)
print("Type of list:", type(list))
print("Length of list:", len(list))
#slicing the list from index 2 to 4
print("Sliced list (2:5):", list[2:5])

list.append('Hello')
print("List after appending 'Hello':", list)
print("Type of list after appending 'Hello':", type(list))
list.insert(0, 'Start')
list.append('End')
print("List after inserting 'Start' at index 0 and appending 'End':", list)

#tuple
tuple = (1,2,3,4,5)
print("Tuple:", tuple)
print("Type of tuple:", type(tuple))
print("Length of tuple:", len(tuple))
tuple2 = (6,7,8)
tuple3 = (1, (1,2), (3,4,5), (5,6))
print("Nested tuple:", tuple3)
tuple4 = tuple3[2]
print("Accessing nested tuple element:", tuple4)
print("Concatenated tuple:", tuple + tuple2)
print("Sliced tuple (1:4):", tuple[1:4])
print("Is 3 in the tuple?", 3 in tuple)
print("Index of 4 in the tuple:", tuple.index(4))
print("Count of 2 in the tuple:", tuple.count(2))
print("Tuple after concatenation:", tuple + tuple2)
print("Index via Access", tuple[2])

#dictionary
property = {"name": "Alice", "age": 30, "city": "New York",
            "hobbies": ["reading", "traveling", "cooking"],
            "education": {"degree": "Bachelor's", "major": "Computer Science"}}
print("Dictionary:", property)
print("Type of dictionary:", type(property))
print("Length of dictionary:", len(property))
print("Accessing value by key 'name':", property["name"])
print("Accessing value by key 'hobbies':", property["hobbies"])
print("Accessing nested dictionary value 'education':", property["education"])
print("Accessing nested dictionary value 'degree':", property["education"]["degree"])
property["age"] = 35
print("Dictionary after updating age:", property)
property["country"] = "USA"
print("Dictionary after adding country:", property)
del property["city"]
print("Dictionary after deleting city:", property)
print("Is 'name' a key in the dictionary?", "name" in property)
print("Keys in the dictionary:", property.keys())
print("Values in the dictionary:", property.values())   
print("Items in the dictionary:", property.items())
print("Value for key 'name':", property.get("name"))
print("Dictionary after copying:", property.copy())
print("Dictionary after clearing:", property.clear())
