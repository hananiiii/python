num = int(input("enter a number "))
sum =0
for i in range (1,num+1):
    sum +=i
print(sum)


#########


def isValidSubsequence(array, sequence):
    arr_idx = 0  
    seq_idx = 0  
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)

print(isValidSubsequence([11, 4, 8, 2], [4, 2]))  


#######
lang = input("what's your favorite programming language : ")
if lang=="Python" :
    print("Nice choice!")
elif lang=="Golang" :
    print("You'are a cool kid i see...")
if  lang =="JavaScript" :
     print("Okay Mr.web developer")
else :
 print("I don't know that language.")

 

