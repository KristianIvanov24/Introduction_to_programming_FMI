n = int(input())
if n < 1: 
    print("Inavalid data!") 
else:
    for i in range(n, 0, -1): 
        for j in range(n+1-i, 0, -1): 
            print(i**j, end=' ')
        print()
