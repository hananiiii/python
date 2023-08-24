####is leap 
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))
print(is_leap(year))




##""
if __name__ == '__main__':
    n = int(input())
    if 1<=n<=150 :
        for i in range(1,n+1,1) :
            print(i, end='')