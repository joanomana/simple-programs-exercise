#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa cdel triangulo, dado por el teorema de Pitágoras: c2=a2+b2
from math import sqrt
print("Exercise 6")
print("Program for calculate hypotenuse")
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c=  (a**2)+(b**2)
hypotenuse = sqrt(c)
print(f"The hypotenuse with {a} and {b} is: {round(hypotenuse,16)}")