# max(list) min(list) sum(list)

#sum of element in a list 
num = int(input("how many numbers in the list ? ")) 
list = []
for i in range(num):
    element = int(input("enter element number " + str(i) + ":"))
    list.append(element)
sum =0
for j in list :
    sum +=j

print("the sum is :", +sum)

#copie list element 

def copie(str,n):
    string = ""
    for i in range(n):
        string = string + str
    return string

strr=input("enter your string")
nn= int(input("enter the number of copies"))
print(copie(strr,nn))

#number of double element in a list 

def fouble(listt,k) :
    count = 0
    for num in listt :
        if num == k :
            count = count + 1
    return count 

elm = int(input("how many elements in the list?"))
lista = []
for y in range(elm):
    k=int(input("enter element number" +str(y)))
    lista.append(k)
m = int(input("enter the number you are looking for?"))
print(fouble(lista,m))

#diff

c1 =set(["black","white","red"])
c2 =set(["black","white"])
print(c1.difference(c2))

# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using set() constructor
my_set = set([1, 2, 3, 4, 5])

# Adding elements to a set
my_set.add(6)

# Removing elements from a set
my_set.remove(3)

# Checking membership in a set
print(2 in my_set)  # Output: True

# Iterating over a set
for element in my_set:
    print(element)

#gcd 

import math

# Find the GCD of two numbers
num1 = 36
num2 = 48
gcd = math.gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", gcd)

import math

# Find the GCD of three numbers

num1 = 36
num2 = 48
num3 = 60
gcd = math.gcd(math.gcd(num1, num2), num3)
print("GCD of", num1, ",", num2, ", and", num3, "is", gcd)



