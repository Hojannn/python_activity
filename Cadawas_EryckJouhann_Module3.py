
#main fuction  
def displaymenu():
    con = True
    while con == True:
        print("===========================")
        print("STUDENT INFORMATION SYSTEM")
        print("===========================\n")
        print("1. Display Student Information")
        print("2. Compute Average Grade")
        print("3. Determine Letter Grade")
        print("4. Generate Student ID")
        print("5. Variable Scope Demonstration")
        print("6. Factorial Calculator")
        print("7. Fibonacci Series")
        print("8. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue
        #exit
        if choice == 8:
            
            con = False
            print("Exiting the program. Goodbye Dud!")
        #option 1/ display student information
        elif choice == 1:
            print("Enter The Following Requirements:")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            year = input("Enter Year Level: ")
            displayStudent(name, course, year)
        #option 2/ compute average grade
        elif choice == 2:
            
            try:
                g1 = float(input("Enter Grade 1: "))
                g2 = float(input("Enter Grade 2: "))
                g3 = float(input("Enter Grade 3: "))
                print(computeAverage(g1, g2, g3))
            except ValueError:
                print("Invalid input. Please enter numeric values for grades.")
        #option 3/ determine letter grade
        elif choice == 3:
            try:
                avg = float(input("Enter Your Average Grade: "))
            except ValueError:
                print("Invalid input. Please enter an integer or float for the average grade.")
                continue
            print(determineGrade(avg))
        #option 4/ generate student ID
        elif choice == 4:
            getStudentID()
        #option 5/ variable scope demonstration
        elif choice == 5:
            varScope()
        #option 6/ factorial calculator
        elif choice == 6:
            
            try:
                factorial = int(input("Enter a number to calculate its factorial: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            print(f"Factorial of {factorial} is: {factorialCalc(factorial)}")
        #option 7/ fibonacci series
        elif choice == 7:
            
            try:
                n = int(input("Enter a number to calculate its Fibonacci series: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            print(f"Fibonacci series up to {n}:")
            for i in range(n):
                print(fibonacci(i), end=" ")
            print()
            
#display student 
def displayStudent(name, course, year):
    print("\nStudent Information:")
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Year Level: {year}")
    
#compute average grade
def computeAverage(g1, g2, g3):
    average = (g1 + g2 + g3) / 3
    return f"Average Grade: {average:.2f}"

# determine letter grade
def determineGrade(avg):
    
    if avg >= 90 and avg <= 101:
        return "Letter Grade: A"
    elif avg >= 85 and avg < 90:
        return "Letter Grade: B"
    elif avg >= 80 and avg < 85:
        return "Letter Grade: C"
    elif avg >= 75 and avg < 80:
        return "Letter Grade: D"
    else:
        return "Letter Grade: F"

#generate student ID
def getStudentID():
    import random
    student_id = random.randint(1000, 3000)
    print(f"Generated Student ID: 2026-{student_id}")

#variable scope demonstration/extra?
school = "Laguna State Polytechnic University"
def varScope():
   
    studentName = input("Enter Your Name: ")
    print(f"school: {school}\nStudent Name: {studentName}")
    
#factorial calculator
def factorialCalc(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    return n * factorialCalc(n - 1)
#fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) 
    
if __name__ == "__main__":
    displaymenu()