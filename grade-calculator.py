# calculate school grades
math= float(input("Enter a number your grade for math:\n"))
history= float(input("Enter a number your grade for history:\n"))
reading= float(input("Enter a number your grade for reading:\n"))
science= float(input("Enter a number your grade for science:\n"))
media= float(input("Enter a number your grade for media:\n"))

sum=math+history+reading+science+media 
average_grade= sum/5

if average_grade > 90:
    print("Execllent job your grade is: A")
elif  average_grade >80:
    print("Great job your overall grade is: B")
elif    average_grade > 70:
    print( "keep working your overall grade is:D")
elif average_grade > 60:
    print("Keep pushing your overall grade is: C")
else:
    print("you can do better push hard it is possible your grade is :E")