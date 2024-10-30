print("Exercise 10")
import math
size = str(input("Enter the size of the egg, enter g for giant or enter p for small: "))
if size == "g":
    m=67 #gramos
elif size == "p":
    m=47 #gramos
else:
    print("Incorrect Entry")

temp = int(input("Enter the temp of the egg: "))
if temp <=70:
    c= 3.7
    p=1.038
    k=5.4e-3
    tw= 100
    up= (math.pow(m,(2/3))*(c*math.pow(p,(1/3))))
    down=(k*math.pow(math.pi,2))*((math.pow(4*(math.pi/3),(2/3))))
    time1 =up/down
    time2=math.log((0.76*(temp-tw)/(70-tw)))
    time= time1*time2
    minutes = time/60
    print(f"The egg will take {time} seconds or {math.floor(minutes)} minutes to reach the maximum temperature")
else:
    print("The temp is bigger than 70, the egg cannot prepare in this temp")