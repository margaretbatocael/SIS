# Simple Student Information System

import csv

student_fields = ['ID NUMBER', 'NAME', 'COURSE', 'YEAR LEVEL', 'GENDER']
student_database = 'students.csv'

def menu():
    print("================================")
    print("================================")
    print(":  STUDENT INFORMATION SYSTEM  :")
    print("================================")
    print("================================")
    print("1. Add New Student")
    print("2. Display List of Students")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. Delete a Student")
    print("6. Exit")


def create():
    print("--- ADD STUDENT DATA ---")
    print("========================")

    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input(field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data is saved!")
    input("Press 'Enter' to continue")
    return


def read():
    global student_fields
    global student_database

    print("--- STUDENT RECORDS ---")
    print("=======================")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n------------------------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end='\t |')
            print("\n")

    input("Press 'Enter' to continue")


def search_student():
    global student_fields
    global student_database

    print("--- SEARCH STUDENT ---")
    print("======================")
    roll = input("Enter ID no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found! -----")
                    print("ID NUMBER(YYYY-NNNN: ", row[0])
                    print("NAME: ", row[1])
                    print("COURSE: ", row[2])
                    print("YEAR LEVEL: ", row[3])
                    print("GENDER: ", row[4])
                    break
        else:
            print("ID No. not found!")
    input("Press 'Enter' to continue")


def update():
    global student_fields
    global student_database

    print("--- UPDATE STUDENT ---")
    print("======================")
    roll = input("Enter ID no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student found at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID No. not found!")

    input("Press 'Enter' to continue")


def delete():
    global student_fields
    global student_database

    print("--- DELETE STUDENT ---")
    print("======================")
    roll = input("Enter ID no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:

            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID no. ", roll, "is deleted!")
    else:
        print("ID No. not found!")

    input("Press 'Enter' to continue.")

while True:
    menu()

    choice = input("What do you wish to do? Enter the number: ")
    if choice == '1':
        create()
    elif choice == '2':
        read()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update()
    elif choice == '5':
        delete()
    else:
        break

print("================")
print("================")
print(":  Thank You!  :")
print("================")
print("================")
