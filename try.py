def display_person(*args):
    for i in args:
        print(i)

display_person("Emma", "25")

###
def fun1(num):
    return num + 25

fun1(5)
###
def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25) # 25 overriding the default value of 20.

#####
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

####
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

display(emp="Kelly", salary=9000)

##
sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)

##
my_dict = {"name": "Alice", "age": 25, "country": "USA"}

# Remove a key using the del statement
del my_dict["age"] #popitem remove last item
my_dict.pop("name")
my_dict.popitem()

print(my_dict)

 #____________
#dict1 = {"name": "Mike", "salary": 8000}
#temp = dict1.pop("age")
#print(temp)__________________________________# error 

#get givesnone and pop gives error

##
dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2) ##true dictionaries are considered equal if they have the same keys and val order doesn' effect 




