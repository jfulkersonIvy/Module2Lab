# Jonathan Fulkerson
# SDEV 220
# Module 2 Lab - Case Study: if...else and while
# This program will take a first and last name as input, along with a GPA. Then it will determine if that student made the Dean's List or the Honor Roll

loop = True
while loop is True:
    lastName = input("Please enter the student's last name (Enter ZZZ to quit): ")
    if lastName == "ZZZ":
        loop = False
    else:
        firstName = input("Please enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))
        if gpa >= 3.5:
            print(f"{firstName} {lastName} has made the Dean's List!")
        elif 3.25 <= gpa < 3.5:
            print(f"{firstName} {lastName} has made the Honor Roll!")
        else:
            print(f"{firstName} {lastName} has a GPA of {gpa}.")
