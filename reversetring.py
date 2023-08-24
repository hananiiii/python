String =input(" enter your string ")
print ( String)
inverse = String[::-1] #sequence[start:end:step]
print(inverse)

#create a list and tuple with comma separated num

values = input("Enter some values separated by commas: ")
value_list = values.split(",")
value_tuple = tuple(value_list)
print("List:", value_list) #[]
print("Tuple:", value_tuple) #() or nothing 
#tuple same as list but can't add or remove or after it's definded also can contain alot of data types


#numbers ceparated by , 

numbers =[] #empty list
while len(numbers) < 4: #returns the number of elements in the numbers list.
    num = input("enter a valid number")
    if num.isdigit(): # verify if the num is valid or not 
        numbers.append(num) 
    else:
        print("please enter a valid number!")

numbers_str = '/'.join(numbers) #concatenate the elements of the numbers list into a single string
print(numbers_str)

#how to get file extension 

file_Name = input("enter file name")
ext=file_Name.split(".")
print(repr(ext[-1])) #ext[-1] accesses the last element of the list
#list[-1] is the last element in the list

#%s for string 
#%i for integer

name=input("enter your age")
age=int(input("enter your age"))
message="my name is %s ,i'm %s years old" %(name,age)
print(message)

