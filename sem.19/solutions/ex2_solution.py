class roman_arab_numbers:
    def __init__(self, roman_number="", arabic_number=0):
        self.rn = roman_number
        self.an = arabic_number

    def roman_arabic(self):
        D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        arabicn = 0
        for i in range(1, len(self.rn)):
            a = D[self.rn[i - 1]]
            b = D[self.rn[i]]
            if a >= b:
                arabicn += a
            else:
                arabicn -= a
        arabicn += D[self.rn[-1]]
        self.an = arabicn
        return arabicn

    def __str__(self):
        if self.an == 0:
            self.roman_arabic()

        ss = f"Римски запис: {self.rn}\n"
        ss += f"Арабски запис: {self.an}\n"
        ss += "_____________________\n"
        return ss


print(roman_arab_numbers("MMXX"))
print(roman_arab_numbers("MCMLXXV"))
print(roman_arab_numbers("DCLXVI"))
print(roman_arab_numbers("DIX"))
print(roman_arab_numbers("VIII"))
