if __name__ == '__main__':
 n = int(input().strip())
 if n<100 and n>1:
    
     if n%2 !=0 :
            print("weird")
    
     elif 2<=n<=5 :
            print("Not Weird")
          
     elif 6<=n<=20 :
            print("Weird")
           
     else :
            print("Not Weird")
       

##
if __name__ == '__main__':
    a = int(input())
    b = int(input())
if a<10**10 and b<10**10 :
 print(a+b)
 print(a-b)
 print(a*b)
    
##
if __name__ == '__main__':
    n = int(input())
if 1<=n<=20 :
     for i in range (1,n,1) :
          print(i**2)


####is leap 
def is_leap(year):
  leap = False
  while 1900<=n <=10**5 :
    if year//4 ==0 :
         leap=True
    
    if year // 100 == 0 and year // 400 ==0 :
         leap =True 
    else :
         leap =False
   
    
    return leap

year = int(input())
print(is_leap(year))

