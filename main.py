from operations import *

while True:
    print("-"*20)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("-"*20)

    choice=int(input("Enter Choice : "))

    if choice==1:
        add_student()
    elif choice==2:
        view_students()
    elif choice==3:
        search_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
