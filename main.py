#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

print("Exercise 2")
radio = float(input("Enter the radio of the circle: "))
perimeter = 2 * 3.1416 * radio
area = 3.1416 * radio ** 2
print(f"The perimeter of the circle is: {round(perimeter,1)} ")
print(f"The area of the circle is: {round(area,1)} ")