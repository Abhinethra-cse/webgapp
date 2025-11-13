#print string in reverse order
string="abhi nethra alwar"
 reverse_string=string[::-1]
 print("reversed string:",reverse_string)

#generate bill amount with discount
 def bill():
    amount = int(input("Enter amount: "))
    if amount > 1000:
        discount = amount * 0.1
        final_amount = amount - discount
        print("Final amount after 10% discount:", final_amount)
    else:
        print("No discount. Final amount:", amount)

bill()

#username and password login error
username=input("username:")
password=input("password:")
if username=="abhi" and password =="1086":
    print("login successful")
else:
    print("error, incorrect username or password")


#current bill based on units
def current_bill(units):
    if units > 100:
        current_bill=units*5
    else:
        current_bill=units*3
    return current_bill
print("current bill:",current_bill(50))

#email error
def email_check(email):
        if "@" in email and "." in email:
            print("valid email")
        else:
            print("invalid email, please re-enter")
email=input("enter your email:")
email_check(email)

#count and print positive and negative number from the list

list=[10,-23,3,-24,45,-89]
positive_number=[]
negative_number=[]
count_pos=0
count_neg=0
for i in list:
    if i>=0:
        positive_number.append(i)
        count_pos+=1
    else:
        negative_number.append(i)
        count_neg+=1
print("positive numbers:",positive_number)
print("count of positive numbers:",count_pos)
print("negative numbers:",negative_number)
print("count of negative numbers:",count_neg)


#print random number from 1to 100
def random_number():
    import random
    number=random.randint(1,100)
    return number
print("random number:",random_number())

# load before printing every number
import time   

num = int(input("Enter a number: "))

for i in range(num):
    print("Loading...")
    time.sleep(1)   
    print("Number:", i)

#print list of natural number in reverse order
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

#generate random pin
def pin_generator():
    import random
    pin = random.randint(1000, 9999)
    return pin
print("Generated PIN:", pin_generator())


