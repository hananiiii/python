# For STRING 

my_string = "Hello"

         # Adding

  # Output: Hello World
world = "World2"
new_string=my_string +" {}".format(world)
print(new_string)

         # Removing
new_string = my_string.replace("H", "")
print(new_string)  # Output: ello

         # Accessing
print(my_string[0])      # Output: H
print(my_string[1:4])    # Output: ell

         # Getting
print(len(my_string))    # Output: 5
print(my_string.upper()) # Output: HELLO


#FOR SETS

my_set = {1, 2, 3}

      # Adding
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

      # Removing
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

      # Accessing
for element in my_set:
    print(element)  # Output: 1, 3, 4

      # Getting
print(len(my_set))  # Output: 3
print(my_set.union({5, 6}))  # Output: {1, 3, 4, 5, 6}

#FOR LISTS


my_list = [1, 2, 3]

      # Adding
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

      # Removing
my_list.remove(2)
print(my_list)  # Output: [1, 3, 4]

      # Accessing
print(my_list[0])     # Output: 1
print(my_list[1:3])   # Output: [3, 4]

      # Getting
print(len(my_list))   # Output: 3
print(my_list.count(1))  # Output: 1


#For DICTIONARY

my_dict = {"name": "John", "age": 30}

           # Adding/Updating
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

          # Removing
del my_dict["age"]
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

          # Accessing
print(my_dict["name"])  # Output: John

          # Getting
print(len(my_dict))     # Output: 2
print(my_dict.keys())   # Output: dict_keys(['name', 'city'])



