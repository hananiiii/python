 #challenge 01
def Capital_indexes(str) :
    list = []
    for i in range (len(str)) :
        if str[i].isupper() :
            list.append(i)
    return list
string = input("enter a string")
print(Capital_indexes(string))

#challenge 02

def mid(strn):
    middle = (len(strn) - 1) // 2
    if (len(strn) % 2) == 0:
        return ""
    else:
        return strn[middle]

app = input("Enter your string: ")
print(mid(app))

#challenge 03
def online_count(statuses) :
    count = 0
    for  status in statuses.values():
        if status == "offline":
            continue
        if status == "online" :
            count =count + 1
    return count
        
num = int(input("enter number of names in the dictionary"))
statuus = {} #empty dictionary
for i in range(num) :
   name= input("enter name " )
   stat= input("enter status " )
   statuus[name] =stat

print(online_count(statuus))

#challenge 04 
import random 
def random_numbers() :
    resultt = random.randint(0, 100)
    return resultt
   
n1= random_numbers()
print(n1)
n2= random_numbers()
print(n2)

#challenge 05

def only_ints(a,b):
    if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool) :
        return True 
    else :
        return False
    
print(only_ints(5,4))

#challenge 06 :
def double_letters(c) :
    for i in range(len(c)-1) :
        if c[i] == c[i+1] :
            return True
    return False
            
            
res = input("enter your string:" )
print(double_letters(res))




        




      



