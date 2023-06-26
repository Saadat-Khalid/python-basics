#if… elif…else are conditional statements that provide you with the decision making that is required when you want to execute code based on a particular condition.

#Logics

# if the student marks are 90 the result is A Grade

#Simple IF condition

student_marks = 90

if student_marks >= 90:
    print(student_marks, "Congratulations You Got 'A' Grade.... :) ")


# IF ELSE Condition

student_marks = 70

if student_marks >= 80:
    print(student_marks, "Congratulations You Got 'B' Grade.... :) ")
else: 
    print(student_marks, "Your Grade is 'C'")


# IF ELIF & ELSE Condition

student_marks = 60

if student_marks >= 90:
    print(student_marks, "Congratulations You Got 'A' Grade.... :) ")
elif student_marks >= 80 : 
    print(student_marks, "Your Grade is 'B'")
else:  
    print(student_marks, "Your Grade is 'D'")
