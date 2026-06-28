questions = [
    ("Which data type is immutable in Python?", "A. List", "B. Dictionary", "C. Tuple", "D. Set", "C"),
    ("Which keyword is used for loop?", "A. loop", "B. for", "C. repeat", "D. do", "B"),
    ("Which symbol is used for comments?", "A. //", "B. #", "C. /*", "D. --", "B"),
    ("Which function takes user input?", "A. print()", "B. type()", "C. input()", "D. len()", "C"),
    ("Which data structure stores key-value pairs?", "A. List", "B. Tuple", "C. Set", "D. Dictionary", "D"),
    ("Python is a ?", "A. Language", "B. Browser", "C. OS", "D. Editor", "A"),
    ("Which operator is used for multiplication?", "A. +", "B. -", "C. *", "D. /", "C"),
    ("Which function displays output?", "A. input()", "B. print()", "C. len()", "D. str()", "B"),
    ("List is ?", "A. Mutable", "B. Immutable", "C. Fixed", "D. None", "A"),
    ("Which keyword is used for conditions?", "A. for", "B. if", "C. while", "D. break", "B")
]

print("===== PYTHON QUIZ SYSTEM =====")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

score = 0
wrong = []

for q in questions:
    print("\n" + q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    ans = input("Your Answer (A/B/C/D): ").upper()

    if ans == q[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        wrong.append((q[0], q[5]))

total = len(questions)
percent = (score / total) * 100

if percent >= 90:
    grade = "O"
elif percent >= 80:
    grade = "A+"
elif percent >= 70:
    grade = "A"
elif percent >= 60:
    grade = "B+"
elif percent >= 50:
    grade = "B"
else:
    grade = "F"

print("\n====== RESULT REPORT ======")
print("Name :", name)
print("Roll :", roll)
print("Score :", score, "/", total)
print("Percentage :", round(percent, 2), "%")
print("Grade :", grade)

if percent >= 50:
    print("Result : PASS")
else:
    print("Result : FAIL")

if len(wrong) > 0:
    print("\nWrong Answers:")
    for i in wrong:
        print("Question:", i[0])
        print("Correct Answer:", i[1])