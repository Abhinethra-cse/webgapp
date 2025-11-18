#print 10 employee name and age
class employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
e1=employee("john",25)    
e2=employee("doe",30)
e3=employee("smith",28)
e4=employee("jane",22)
e5=employee("alice",27)
e6=employee("bob",35)
e7=employee("charlie",29)
e8=employee("david",31)
e9=employee("eve",24)
e10=employee("frank",33)
print(e1.name,e1.age)
print(e2.name,e2.age)
print(e3.name,e3.age)
print(e4.name,e4.age)
print(e5.name,e5.age)
print(e6.name,e6.age)
print(e7.name,e7.age)
print(e8.name,e8.age)
print(e9.name,e9.age)
print(e10.name,e10.age)


#class variable
class student:
    school="ABC High School"
    def __init__(self, name ):
        self.name=name
s1=student("john")
s2=student("doe")
print(s1.school)
print(s2.school)


#class variable example
class employee:
    company="XYZ Corp"
    def __init__(self, name, age):
        self.name=name
        self.age=age
e1=employee("john",25)
e2=employee("doe",30)
print(e1.company,e1.age)
print(e2.company,e2.age)

#change school name with@classmethod
class student:
    school="abc"
    @classmethod
    def change_school(cls, new_name):
        cls.school=new_name    
student.change_school("XYZ High School")
print(student.school)

#count of object
class student:
    count=0
    def __init__(self, name):
        self.name=name
        student.count +=1
s1=student("ram")
s2=student("anu")
s3=student("raj")

print(student.count)

#change country name
class person:
    country="austria"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_country( cls , new_country):
        cls.country=new_country

p1 = person("anu")
p2 = person("ram")
p3 = person('raj')
p4 = person("abi")
p5 = person("hari")

person.change_country("India")  
print(p1.name, person.country)      
print(p2.name, person.country)      
print(p3.name, person.country)      
print(p4.name, person.country)      
print(p5.name, person.country)      

#change salary
class employee:
    salary="60,000"
    @classmethod
    def change_salary(cls ,new_salary):
        cls.salary=new_salary
employee.change_salary("1000000")
print(employee.salary)

#largest number
a = 10
b = 25
c = 17

print("The three numbers are:", a, b, c)

largest = max(a, b, c)

print("The largest number is:", largest)

#amount balance
balance = 200   

print("Your balance is:", balance)

if balance < 1000:
    print("Warning: Your balance is low!")


#train ticket booking
print("----- TRAIN TICKET BOOKING SYSTEM -----")

name = input("Enter Passenger Name: ")
from_station = input("From Station: ")
to_station = input("To Station: ")

print("\nChoose Class:")
print("1. General  (Rs.100)")
print("2. Sleeper  (Rs.150)")
print("3. AC       (Rs.300)")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    seat_class = "General"
    price = 100
elif choice == 2:
    seat_class = "Sleeper"
    price = 150
elif choice == 3:
    seat_class = "AC"
    price = 300
else:
    print("Invalid choice! Defaulting to General.")
    seat_class = "General"
    price = 100

tickets = int(input("Enter number of tickets: "))

total_amount = tickets * price

print("\n----- BOOKING SUMMARY -----")
print("Passenger Name :", name)
print("From           :", from_station)
print("To             :", to_station)
print("Class Selected :", seat_class)
print("Tickets Booked :", tickets)
print("Price Per Ticket :", price)
print("------------------------------")
print("Total Amount   :", total_amount)


#password length
password = "Abhi@123"

print("Password is:", password)
print("Length of password is:", len(password))
