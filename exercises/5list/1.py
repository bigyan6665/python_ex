student_marks = [45,56,78,45,90]
lowest_marks = min(student_marks)
if(lowest_marks < 40):
    print("you have failed")
else:
    total_obtained = sum(student_marks)
    total = 500
    percent = total_obtained/total * 100
    grade = ""
    if(percent >= 90):
        grade = "A"
    elif(percent >= 80):
        grade = "B"
    elif(percent >= 70):
        grade = "C"
    elif(percent >= 60):
        grade = "D"
    elif(percent < 60):
        grade = "F"    
    print(f"Congratulations, you have passed with grade = {grade} ")