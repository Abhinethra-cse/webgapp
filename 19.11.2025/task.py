#hosiptal details
class Hospital:
    def __init__(self, name, disease):
        self.__patient_name = name
        self.__disease = disease

    def get_details(self):
        return f"Patient: {self.__patient_name}, Disease: {self.__disease}"

    def update_disease(self, new_disease):
        self.__disease = new_disease

p1 = Hospital("Rahul", "diarrhea")
print(p1.get_details())        
p1.update_disease("heart attack")  
print(p1.get_details())


#student attendance program
class Attendance:
    def __init__(self):
        self.__students = {
            "Rahul": "Present",
            "Priya": "Absent",
            "Kiran": "Present",
            "Anjali": "Present"
        }


    def show_attendance(self):
        print("--- Attendance List ---")
        for name, status in self.__students.items():
            print(f"{name} : {status}")


a = Attendance()
a.show_attendance()

#print second largest and third smallest number
nums = [12, 5, 30, 2, 18]
nums.sort()
print("Second Largest =", nums[-2])
print("Third Smallest =", nums[2])

#join number
a= [1,2]
b= [3,4]

c= a+b
print(c)

#remove duplicates
nums = [1,2,3,3,4,4,5,5,5,6]
nums=list(set(nums))
print(nums)

#swap number
a=15
b=30
a,b = b,a
print("a=",a)
print("b=",b)

#print missing number
a=[1,2,3,4,7,8,9,10]
for i in range(1,11):
    if i not in a:
        print("missing number:",i)

#year calendar
import calendar
year = 2025
print(calendar.calendar(year))


#random HEX colour code
import random
letters_numbers = "ABCDEF0123456789"
color = "#"
for i in range(5):
    color += random.choice(letters_numbers)
print("Random Color Code:", color)

#random pick from rock paper scissor
import random
choices = ["rock", "paper", "scissor"]
pick = random.choice(choices)
print("Random Pick:", pick)

#random pick of number in dices
import random

dice = random.randint(1, 6)
print("Dice shows:", dice)


#random password generation
import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(8):   
    password += random.choice(characters)
print("Random Password:", password)

#otp generation
import random
otp = ""
for i in range(6):   
    otp += str(random.randint(0, 9))
print("Your OTP:", otp)

#captcha
import random
import string
captcha = ""
characters = string.ascii_letters + string.digits  
for i in range(6): 
    captcha += random.choice(characters)
print("CAPTCHA:", captcha)


#online order
from abc import ABC, abstractmethod

class OrderSystem(ABC):
    @abstractmethod
    def show_order(self):
        pass


class OnlineOrder(OrderSystem):
    def __init__(self):
        self.__orders = ["waffle", "Burger", "Coffee icecream"]   

    def show_order(self):   
        print("Available Orders:")
        for item in self.__orders:
            print("-", item)

o = OnlineOrder()
o.show_order()
