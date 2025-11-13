#for loop examples
for i in range(2,13,4):
   print(i)

#print each character 
word ="abhinethra"
for ch in word:
   print(ch)
  
#factorial of a number
num=5
fact=1
for i in range(1,num+1):
   fact*=i
  
print ("factorial is :",fact)

# while loop example
i=2
while(i <=7):
   print(i)
   i+=2

#print numbers from n to 1
num=int(input("enter a number:"))
while(num>0):
   print("number is:",num)
   num=num-1

#pattern printing
for i in range(1,6):
    for j in range(1,i+2):
        print(j,end="" )
    print()

#sum of first 50 natural numbers
i=0
total=0
while(i<=50):
    total=total+i
    i=i+1
print(total)    

#print even numbers between 2 to 30
for i in range(2,30,2):
    print(i)

# multiplication 
num=int(input("enter the number:"))
for i in range (1,5):
    print(i*2)

# multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# pattern printing
for i in range(6):
    for j in range(6):
       print("*",end="")
    print()         


# infinite loop
num =int(input("enter the number:"))
while(num>0):
    print(num)
    num=num+1

# Count vowels in a word
word="abhinethra"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count = count + 1

print("Number of vowels:", count)

# pattern printing
for i in range(1,4):
    for j in range(1,4):
        print(i*j,end="")
    print()

# skip multiples of 3
for i in range(1, 21):
    if i % 3 == 0:    
        continue    
    print(i)

# print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1

#reverse a number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10       # take last digit
    rev = rev * 10 + digit # add digit to reverse
    num = num // 10        # remove last digit

print("Reversed number:", rev)

# sum of digits of a number
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10      # get last digit
    total += digit        # add to total
    num = num // 10       # remove last digit

print("Sum of digits:", total)

# count digits in a number
num = int(input("Enter a number: "))
count = 0

while num > 0:
     num //= 10  
     count += 1

print("Number of digits:", count)

# product of first 5 numbers
pdt = 1

for i in range(1, 6):
    pdt *= i

print("Product of first 5 numbers:",pdt)

# even odd
num=int(input("number:"))
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

# even odd function
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


check_even_odd(10)
check_even_odd(7)



