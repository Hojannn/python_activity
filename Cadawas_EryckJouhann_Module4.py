class Student:
    def __init__(self, student_id, name, course, year_level, gpa):
        #Public Attribute: This ID attribute can be accessed from outside the class.
        self.student_id = student_id
        #Public Attribute: This name attribute can also be accessed from outside the class.
        self.name = name
        #Protected Attribute: This course attribute is obly accessible within the class or subclasses.
        self._course = course
        #Protected Attribute: This year_level attribute is only accessible within the class or subclasses.
        self._year_level = year_level
        #Private Attribute: This gpa attribute is private and only accessible within the class itself.
        self.__gpa = gpa
        
    #Display student information method
    def display_info(self):
        print(" _____________________________")
        print("|     STUDENT INFORMATION     |")
        print("|_____________________________|")
        print(f" Student ID: {self.student_id}")
        print(f" Name: {self.name}")
        print(f" Course: {self._course}")
        print(f" Year Level: {self._year_level}")
        print(f" GPA: {self.__gpa}")
        print(f" Academic Status: {self.academic_status()}")
        print("_______________________________")

    #Updates the GPA of the student
    def update_gpa(self, new_gpa):
        self.__gpa = float(new_gpa)
        print(f" GPA updated to: {new_gpa}")
        
    #Determines the academic status of the student based on their GPA
    def academic_status(self):
        if self.__gpa <= 1.75:
            return "Dean's Lister"
        elif self.__gpa > 1.75 and self.__gpa <= 3.00:
            return "Regular Student"
        elif self.__gpa > 3.00:
            return "Probation"
        
    #An Alternatove method or Method overloading alterative
    def dis_method(self, *args):
        student_info = (f"ID {self.student_id}, Name: {self.name}")
        if len(args) == 0:
            print(student_info)

        elif len(args) == 1:
            if args[0] == True:
                print(f"{student_info}, Course: {self._course}")

        elif len(args) == 2:
            if args[0] == True and args[1] == True:
                print(f"{student_info}, Course: {self._course}, GPA: {self.__gpa}")


s1 = Student("0125-0077", "Jouhann", "BSCS", 2, 1.43)
s2 = Student("0125-0984", "Josh Wesley", "BSCS", 2, 1.40)
s3 = Student("0125-2990", "Dolf Louise", "BSCS", 2, 1.50)
s4 = Student("0125-0045", "Rafael Palomique", "BSCS", 2, 1.45)
s5 = Student("0125-0822", "Jhowen Marcelo", "BSCS", 2, 1.42)

students = [s1, s2, s3, s4, s5]
# s1.dis_method(True, True)

#Menu function, to handle User input
def menu():
    while True:
        print(" _____________________________")
        print("|        MENU OPTIONS         |")
        print("|_____________________________|")
        print("| 1. Display Student Info     |")
        print("| 2. Add Student              |")
        print("| 3. Remove Student           |")
        print("| 4. Update GPA               |")
        print("| 5. Exit                     |")
        print("|_____________________________|")
        
        try:
            choice = int(input("Please select an option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.")
            continue
        
        if choice == 5:
            print("Exiting the program. Bye!")
            break
        
        elif choice == 1:
            for student in students:
                student.display_info()
                student.academic_status()
                
        elif choice == 2:
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            course = input("Enter Student Course: ")
            year_level = int(input("Enter Student Year Level: "))
            gpa = float(input("Enter Student GPA: "))
            
            new_student = Student(student_id, student_name, course, year_level, gpa)
            students.append(new_student)
            print(f"Student: {student_name} added successfully.")
            
        elif choice == 3:
            try:
                student_id = input("Enter Student ID to remove: ")
                for student in students:
                    if student.student_id == student_id:
                        students.remove(student)
                        print(f"Student with ID {student_id} has been removed.")
                        break
            except ValueError:
                print("Invalid input. Please enter a valid Student ID.")
            else:
                print(f"No student found with ID {student_id}.")
                
        elif choice == 4:
            try:
                student_id = input("Enter Student ID to update GPA: ")
                try:
                    new_gpa = float(input("Enter new GPA: "))
                except ValueError:
                    print("Invalid input. Please enter a valid GPA.")
                    continue
                for student in students:
                    if student.student_id == student_id:
                        student.update_gpa(new_gpa)
                        break
                else:
                    print(f"No student found with ID {student_id}.")
            except ValueError:
                print("Invalid input. Please enter a valid Student ID and GPA.")
  
  
if __name__ == "__main__":
    menu()