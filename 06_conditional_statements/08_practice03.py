# grade calculator
# -- asign a latter grade based on student's score:
# A(90-100), B(80-89), C(70-79), D(60-69), E(33-59), F(<33)

score = int(input("enter your score: "))


if score > 100:
    grade = "Invalid score, score should be between 0 and 100"

elif score >= 90 and score <= 100:
    grade = "A"

elif score >= 80 and score < 90:
    grade = "B"

elif score >= 70 and score < 80:
    grade = "C"

elif score >= 60 and score < 70:
    grade = "D"

elif score >= 33 and score < 60:
    grade = "E"

else:
    grade = "F"


if grade == "F":
    print("you failed the exam, better luck next time!")

elif grade == "Invalid score, score should be between 0 and 100":
    print(grade)

else:
    print("your score is: ", score)
    print("your grade is: ", grade)
    print("congratulations, you passed the exam $$ ")