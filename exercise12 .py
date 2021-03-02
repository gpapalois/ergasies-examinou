file = input("Δώσε ένα αρχείο ascii.")
for i in range(len(file)):
    letter = file[len(file)-i -1]
    number = ord(letter)
    number2 = 128 - number
    ascii = chr(number2)
    print(ascii ,end ="")