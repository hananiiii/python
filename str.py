#get ascii of a char 
char = '*'
ascii_value = ord(char)
print(ascii_value)


#
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString) #true
print(stringList[1] is myString) #true 

#######
#str.count(sub,index)
#isalnum() checks whether a string consists of alphanumeric characters only


######""""""""""""""""""""""""""""""LIST""""""""""""""""""""""""""""""""
"pop in a list removes the last element  .pop() .pop(index)"

#replace element in list 
aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

#
aList = [5, 10, 15, 25]
print(aList[::-2])

# use copy or list to copy a list 
aList = ['a', 'b', 'c', 'd']
my_list = list(aList)
print(my_list)

#
aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)

#
print(len([None])*10) #10

## set 
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Blue") # remove
print(sampleSet)

set2 = sampleSet.copy()
#set2 = set(sampleSet)
#set2.update(sampleSet)
print(set2)

sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red"])
print(sampleSet)

#
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set1.difference_update(set2) # remove from set1 all elemnts commun in set2
print(set1)

#
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
result = set1.isdisjoint(set2) #true if there is no commun elements symmetric_difference
print(result)

# union remove duplicet elem
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {4, 5, 6}
result = set1.union(set2, set3)
print(result)



set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}
set3 = set1.union(set2)
print(set3)

#
aSet = {1, 'PYnative', ('abc', 'xyz'), True} # true is 1
print(aSet)
#set is mutable but can't contain changeable like list and dictionary but can contain unchangeable tuple ...




