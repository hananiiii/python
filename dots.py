#challenge 07 :
def add_dots(srrt) : 
    for i in range (len(srrt)) :
        resu = ".".join(srrt)
        return resu 
    
def remove_dots(stri) :
    resul =stri.replace('.', '')
    return resul
    
print(add_dots("test"))
print(remove_dots("t.e.s.t"))
print(remove_dots(add_dots("test")))

#challenge 08 :
def count(k): 
    syllabe =1
    for i in range(len(k)) :
        if k[i] != "-" :
            continue
        if k[i] == "-" :
            syllabe =syllabe + 1
    return syllabe
print(count("teste"))

#challenge 09 :
def is_anagram(s,ss):
    if len(s) != len(ss) :
        return False 
    count =0
    count2=0
    for i in range(len(s)-1) :
      if s[i] == s[i+1] :
          count =count +1
      for j in range(len(ss)-1) :
          if ss[j]==s[i] :
              count2 = count2 +1
    if count2 == count :
       for i in range(len(s)) :
        if s[i] not in ss :
            return False 
    return True
     
print(is_anagram("test","tess"))

#challenge 09/2 :
def is_anagram(s, t):
    return sorted(s) == sorted(t)
print(is_anagram("test","tess"))

#challenge 10 :
  #nested list [[],[]] 

nested_list = [[1, 2], [3, 4]]
for inner_list in nested_list:
    for element in inner_list:
        print(element)
listi =[]
for inner_list in nested_list:
    for element in inner_list:
        listi.append(element)
print(listi)


#challenge 10/2 :
def flatten(nes_list):
    listo =[]
    for i in nes_list:
      for element in i:
        listo.append(element)
    return listo 

print(flatten([[1, 2], [3, 4]]))


#challenge 11 :
def largest_difference (listtt) :
     
     for i in range(len(listtt)-1) :
        for j in range(len(listtt)-1) :
         
          if listtt[i] > listtt[j] :
              max=listtt[i]
             
          else :
              min=listtt[i]     
     return max-min
 
print(largest_difference([10,2,3]))


def largest_difference(lst):
    max_value = -100
    min_value = 100

    for num in lst:
        num = max(-100, min(100, num))
        max_value = max(max_value, num)
        min_value = min(min_value, num)

    return max_value - min_value

print(largest_difference([10, 2, 3])) 

#challenge 11 :
def div_3(i) :
    if i % 3 == 0 :
     return True 
    else :
     return False
print(div_3(6))


#challenge 12:
def get_row_col(stri):
   my_tuple=[]
   if stri[0] == "A" :
      col =0 
   if stri[0] =="B" :
      col =1
   if stri[0] =="C" :
      col =2
   if stri[1] == "1" :
      row =0 
   if stri[1] =="2" :
      row =1
   if stri[1] =="3" :
      row =2
   my_tuple.append(row)
   my_tuple.append(col)
   return tuple(my_tuple) #o convert the list my_tuple into a tuple

print(get_row_col("A3"))

#challenge 13 :
def palindrome(str):
   for i in range(len(str)//2):
    
         if str[i] != str[len(str)-1 -i]  :
            return False

   return True 
print(palindrome("ana"))


#challenge 14 :
def palindrome(str):
   for i in range(len(str)//2):
    
         if str[i] == str[len(str)-1] :
            return True
         else :
            return False 
print(palindrome("a"))

#challeneg 15 :
def up_down(k):
   myy_tube =[]
   up = k+1
   down =k-1
   myy_tube.append(down)
   myy_tube.append(up)
   return tuple(myy_tube)
print(up_down(5))

#challeneg 16 :
def consecutive_zeros(sttr) : #110011100011 outptu should be 3
   count =0
   max_count=0
   for i in sttr :
      if i == "0" :
       count +=1
      else :
       max_count=max(max_count,count)
       count=0
   max_count=max(max_count,count)
   return max_count

print(consecutive_zeros("11001110011"))

#challenge 17 :
def all_equal(lisst):
   for i in range(len(lisst)-1) :
      if lisst[i] != lisst[i+1] :
         return False 
    
   return True 
print(all_equal([1]))

#challenge 18 :
def triple_and(a,b,c):
   if a==b==c== True :
      return True
   else :
      return False 
print (triple_and(True,True,True))

#challenge 19 :
number = 42
string_number = str(number)
print(string_number)  # Output: "42"

def convert(lista):
    return list(map(str, lista))

print(convert([1, 2, 3]))  


#challenge 20 :

   # zap(
   # [0, 1, 2, 3],
    #[5, 6, 7, 8]
   # )
    #Should return:

    #[(0, 5),
    #(1, 6),
    #(2, 7),
    #(3, 8)]


def zap(a,b) :
    while len(a) ==len(b) :
     return [(a[i], b[i]) for i in range(len(a))]

print(zap([0,  3], [5, 6]))  


#challenge 21 :
def validate(code):
    if "def" not in code:
        return "missing def"

    if ":" not in code:
        return "missing :"

    if "(" not in code or ")" not in code:
        return "missing paren"

    if "()" in code:
        return "missing param"

    if "    " not in code:
        return "missing indent"

    if "validate" not in code:
        return "wrong name"

    if "return" not in code:
        return "missing return"

    return True

# Testing the function with its own code
own_code = '''
def validate(code):
    if "def" not in code:
        return "missing def"

    if ":" not in code:
        return "missing :"

    if "(" not in code or ")" not in code:
        return "missing paren"

    if "()" in code:
        return "missing param"

    if "    " not in code:
        return "missing indent"

    if "validate" not in code:
        return "wrong name"

    if "return" not in code:
        return "missing return"

    return True
'''

print(validate(own_code))  # Output: True


#challenge 22:

def list_xor(n,list1,list2) :
  if n not in list1 and n not in list2 :
     return False 
  if n in list1 and n in list2 :
     return False 
  else :
     return True 
  
print(list_xor(1, [1, 2, 3], [1, 5, 6]))


#challenge 23 :
#The *args parameter allows a function to accept any number of positional arguments.

def param_count(*args):
    return len(args)
print(param_count()) 



#challenge 24 :
def format_number(number):
    return "{:,.0f}".format(number)

# Test case
print(format_number(1000000))  

#"{:,.0f}": This is a format string that specifies how the number should be formatted. Let's break it down further:

#:: Marks the beginning of the format specification.
#,: Specifies the comma as the thousands separator.
#.0f: Specifies that the number should be formatted as a floating-point number with no decimal places.


      


   


