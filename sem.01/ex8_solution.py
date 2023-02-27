binary = input("Enter a 5-digit binary number: ")

decimal = (int(binary[0]) * 16) + (int(binary[1]) * 8) + (int(binary[2]) * 4) + (int(binary[3]) * 2) + int(binary[4])
print("The decimal equivalent is:", decimal)
