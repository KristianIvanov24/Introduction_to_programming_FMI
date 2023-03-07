number = int(input())

if number % 2 == 0:
    if 2 <= number <= 10:
        print("Even between 2 and 10")
    elif 11 <= number <= 20:
        print("Even between 11 and 20")
    else: 
        print("Even over 20")
else:
    print("Odd")
