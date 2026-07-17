from data import students
from student import Student

def add_student():
    roll=int(input("Enter Roll No : "))
    name=input("Enter Name : ")
    college=input("Enter College Name : ")

    student=Student(roll,name,college)
    students.append(student)
    print("Student Added Successfully")

def view_students():
    if len(students)==0:
        print("Student Not Found")
        return None
    for student in students:
        student.display()
    
def search_student():
    roll=int(input("Enter Roll No : "))
    for student in students:
        if student.roll==roll:
            student.display()
            return
    print("Student Not Found")

def delete_student():
    roll=int(input("Enter Roll No : "))
    for student in students:
        if student.roll==roll:
            students.remove(student)
            print(f"{roll} {student.name} Deleted Successfully")
        else:
            print("Student Not Found")
    