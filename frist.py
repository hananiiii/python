num= int(input("how many numbers are there?")) #input is a func waiting for user to enter a number it give it as a string then with int it converted into an integer number 
sum=0
for n in range (num):
    numbers = float(input("Enter a number"))
    sum += numbers

avg = sum / num 
print("Average is :",avg)   

