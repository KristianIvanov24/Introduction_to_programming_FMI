n = int(input("Въведете цяло положително число"))
if n <= 0:
    print('Невалидна стойност') 
else:
    for i in range(1,n+1):
        for k in range(n+1-i, 0, -1): 
            print(i**k, end=" ") 
        print() 
