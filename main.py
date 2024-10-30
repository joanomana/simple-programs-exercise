#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

print("Exercise 8")

number = float(input("Please enter a number to display the decimal part: "))
parte_entera = int(number)
parte_decimal = number - parte_entera
print(f"The whole part of {number} is {abs(round(parte_decimal,2))}")