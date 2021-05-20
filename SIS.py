# Simple Student Information System

import csv

fields = ['ID NUMBER', 'NAME OF STUDENT', 'COURSE', 'YEAR LEVEL', 'GENDER']
data = 'students.csv'

def menu():
    print("================================")
    print("================================")
    print(":  STUDENT INFORMATION SYSTEM  :")
    print("================================")
    print("================================")
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")


def create():
    print("--- ADD STUDENT DATA ---")
    print("========================")

    stud_data = []
    for field in fields:
        x = input(field + ": ")
        stud_data.append(x)

    with open(data, "a") as file:
        writer = csv.writer(file)
        writer.writerows([stud_data])

    print("Saved!")
    input("Press any key to continue")
    return


def read():

    print("--- LIST OF STUDENTS ---")
    print("========================")
    with open(data, "r") as file:
        reader = csv.reader(file)
        for field in fields:
            print(field, end='       ')
        print("\n------------------------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end='       ')
            print("\n")

    input("Press any key to continue")
    
    
def update():

    print("--- UPDATE STUDENT ---")
    print("======================")
    number = input("Enter ID no. to update: ")
    index_stud = None
    updated_data = []
    with open(data, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if number == row[0]:
                    index_stud = counter
                    print("Student found at index ",index_stud)
                    stud_data = []
                    for field in fields:
                        x = input(field + ": ")
                        stud_data.append(x)
                    updated_data.append(stud_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_stud is not None:
        with open(data, "w") as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)
    else:
        print("ID No. not found!")

    input("Press any key to continue")
    
    
def delete():

    print("--- DELETE STUDENT ---")
    print("======================")
    number = input("Enter ID no. to delete: ")
    stud_found = False
    updated_data = []
    with open(data, "r") as file:
        reader = csv.reader(file)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if number != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    stud_found = True

    if stud_found is True:
        with open(data, "w") as file:

            writer = csv.writer(file)
            writer.writerows(updated_data)
        print("ID no. ", number, "is deleted!")
    else:
        print("ID No. does not exist!")

    input("Press any key to continue.")


def search():
    
    print("--- SEARCH STUDENT ---")
    print("======================")
    number = input("Enter ID no. to search: ")
    with open(data, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                if number == row[0]:
                    print("----- Student Found! -----")
                    print("ID NUMBER ", row[0])
                    print("NAME OF STUDENT: ", row[1])
                    print("COURSE: ", row[2])
                    print("YEAR LEVEL: ", row[3])
                    print("GENDER: ", row[4])
                    break
        else:
            print("ID No. does not exist!")
    input("Press any key to continue")


while True:
    menu()

    choice = input("What do you wish to do? Enter the number: ")
    if choice == '1':
        create()
    elif choice == '2':
        read()
    elif choice == '3':
        search()
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