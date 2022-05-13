from statistics import mean

#local imports
from utils import student_stats
from utils import remove_student
from utils import modify_student_grade
from utils import add_student

def main():
    print("Welcome to grade central\n")
    print("\n")
    
    print("[1] - Enter Grades\n")
    print("[2] - Remove Student\n")
    print("[3] - Student Average Grades\n")
    print("[4] - Exit\n")
    
    message = input("What would you like to do today? (Enter a numner): ")
    
    student_grades = {
        "John": 99,
        "Mathew": 73,
        "Nikki": 100,
        "Salinha": 199999,
        "Okey": 0
    }
    
    print(int(message), isinstance(int(message), int))
    
    if int(message) == 1:
        # get the name of the person and check if they are an admin
        # if they are an admin, then grant them access to enter grades
        admin_names = []
        with open("admins.txt", "r") as admins:
            for name in admins.readlines():
                #print(name)
                
                # got to use removesuffix() because the names end with the \n
                admin_names.append(name.removesuffix("\n"))
            admins.close()
            #print(admin_names)
            
        guest_name = input("Please enter your name: ")
        if guest_name in admin_names:
            print(f"Welcome back admin {guest_name}")
            student_to_modify = input("Which students grade would you like to modify? (Enter a name): ")
            if student_to_modify in student_grades.keys():
                print(f"The student, {student_to_modify} exists\n")
                new_grade = int(input("Please enter their new grade: "))
                if new_grade < 0:
                    print("Please enter a positive grade next time. \nNegative grades do not make sense. Thank you")
                
                student_grades[student_to_modify] = new_grade
            else:
                message = input("That student does not exist. Would you like to create a new student instread? (y or n)")
                if message.upper() == "Y":
                    new_grade = int(input("Please enter the grade for this new student: (Enter a number): "))
                    student_grades[student_to_modify] = new_grade
                    print("Student grade has successfully been modified. Thank you and have a good day!")
                elif message.upper() == "N":
                    print("Thanks, you can now log out.")
        else:
            print("Not an admin")
        print(student_grades)
   
    elif int(message) == 2:
        guest_name = input("Please enter your name: ")
        
        admin_names = []
        with open("admins.txt", "r") as admins:
            for name in admins.readlines():
                #print(name)
                
                # got to use removesuffix() because the names end with the \n
                admin_names.append(name.removesuffix("\n"))
            admins.close()
            #print(admin_names)
                
        if guest_name in admin_names:
            student_to_remove = input("Please enter the students name to be removed: ")
            if not student_to_remove in student_grades.keys():
                print("Student does not exist")
            else: 
                del student_grades[student_to_remove]
        else:
            print("Only admins can remove students. You are not an admin. \nLogging you out immeditely.")
            
        print(student_grades)
    elif int(message) == 3:
        # does not need to be an admin to view the mean of the grades
        
        grades = student_grades.values()
        print(mean(grades))
    elif int(message) == 4:
        print("Thanks for stopping by, you have been logged out successfully!")
    else:
        print("Something is wrong")
        
        
if __name__ == '__main__':
    main()