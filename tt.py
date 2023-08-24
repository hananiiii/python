import timeit
def myFunc():
    start_time = timeit.timeit()
    s = 0
    for i in range ( 1 , n+1 ):
        s = s + i
    end_time = timeit.timeit()
    return s , end_time-start_time
n = 5
print(myFunc())  

#time and timeit are moduls in python to calcule time 