import openpyxl
import os

filename="students_data.xlsx"

if not os.path.exists(filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "students"

    sheet.append(["student ID", "Name", "Age", "Class", "Phone", "Email"])
    workbook.save(filename)
    print("[ ]Excel file created:", filename)

def add_student():
    student_id=input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    std_class = input("Enter Class: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    workbook = openpyxl.load_workbook(filename)
    sheet = workbook["students"]

    sheet.append([student_id, name, age, std_class, phone, email])
    
    workbook.save(filename)
    print("✔ Data saved successfully!")

while True:
    print("\n--- Student Data Entry ---")
    add_student()

    more = input("Do you want to add another student? (yes/no): ").lower()
    if more != "yes":
        print("Exiting program. All data saved!")
        break