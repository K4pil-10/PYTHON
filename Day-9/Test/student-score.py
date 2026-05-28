student_scores={
    "Kapil": 90,
    "Subash": 95,
    "Bikram": 99,
    "Ram": 85,
    "Mikey": 71,
    "Baji": 61,
    "UFO": 51
}

student_grade= {}
for student in student_scores:
    print(student)
    score = student_scores[student]
    print(score)
    if score >=91:
        student_grade[student] = "Outstanding"
    elif score >=81:
        student_grade[student]= "Excellent"
    elif score >= 71:
        student_grade[student] = "Good"
    elif score >= 61:
        student_grade[student]= "Work hard"
    else :
        student_grade[student]= "Fail"
print(student_grade)