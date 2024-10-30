#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

print("Exersice 7")

hora_actual = int(input("Please enter the current time, only the hour in 12 hours format: "))
cantidad_horas = int(input("Please enter the number of hours: "))

new_hour = (hora_actual + cantidad_horas) %12

print(f"In {cantidad_horas} hours it will be {new_hour} o`clock") 