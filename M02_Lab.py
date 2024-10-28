"""Author: Anthony Hutson
   Date Written: 10/28/2024
   Program Name: M02_Lab
   This program will ask the user for a student last name, if the input isn't "ZZZ" the program 
   will then prompt the user for the student's first name. After, the program will ask for the GPA as
   a float variable and calculate if the GPA is higher than 3.50 and 3.25"""

#Creation of exit variable for while loop
lastName = input("Please enter the students' last name or 'ZZZ' to quit: ")


while lastName != "ZZZ":
    firstName = input("Please enter the first name of the student: ")
    gpa = float(input("Please enter the students' GPA: "))

    if gpa > 4 or gpa < 0:
        print(f"Error, GPA not within accepted parameters")
        break
    elif gpa >= 3.5:
        print(f"Congrats! {firstName} {lastName} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"Congrats! {firstName} {lastName} has made Honor Roll!")
    else:
        print(f"Don't worry {firstName} {lastName} keep studying")
    
    lastName = input("Please enter another students' last name or 'ZZZ' to quit: ")