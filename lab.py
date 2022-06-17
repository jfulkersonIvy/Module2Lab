# Jonathan Fulkerson
# SDEV 220
# Module 2 Lab - Case Study: if...else and while
# This program will take a first and last name as input, along with a GPA. Then it will determine if that student made the Dean's List or the Honor Roll

# This will allow us to exit the program if "ZZZ" is entered
loop = True
while loop is True:
    lastName = input("Please enter the student's last name (Enter ZZZ to quit): ")

    # If "ZZZ" is the last name, exit the program
    if lastName == "ZZZ":
        loop = False

    # If anything else is entered, continue
    else:
        firstName = input("Please enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))

        # Depending on the GPA, we display corresponding messages
        if gpa >= 3.5:
            print(f"{firstName} {lastName} has made the Dean's List!")
        elif 3.25 <= gpa < 3.5:
            print(f"{firstName} {lastName} has made the Honor Roll!")
        else:
            print(f"{firstName} {lastName} has a GPA of {gpa}.")
