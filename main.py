print("Exercise 9")

import math
note1=int(input("Enter the first grade: "))
note2=int(input("Enter the second grade: "))
lab=int(input("Enter the lab grade: "))

minimun_grade = 59.5

final_grade_necesary = (minimun_grade - (lab*0.3))/0.7
print(final_grade_necesary)

note3=round((final_grade_necesary*3)-(note1+note2))+1

print(f"To pass the class you need {note3} in the contest")