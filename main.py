#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

print("Exercise 5")

number = int(input("Enter a number of 3 digits to invert: "))
invert_number = str(number)[::-1]
print(f"The number {number} invert is {invert_number} ")