#multiplication of two numbers
def multiply(a,b):
    return a*b
result=multiply(5,6)
print("multiplication is:",result)

#square of a number
def square(a):
    return a*a
result=square(13)
print("square is:",result)

#cube of a number
def cube(a):
    return a*a*a
result=cube(7)
print("cube is:",result)

#fibonacci series
n=int(input("enter the number:"))
a,b=0,1
count=0
while count<n:
    print(a,end="")
    a,b=b,a+b
    count+=1

# greeting message
def create_message(name):
    return f"hello,{name}"
def show_message(m):
    print("received :",m)
m=create_message("abhinethra")
show_message(m)

# last digit of a number
def last_digit(num):
    result = num % 10
    return result

print("Last digit:", last_digit(3568))

# count vowels in a word
def vowels_count(word):
    word = word.lower()
    vowels = "aeiou"
    count = 0
    list_vowels = []  
    
    for ch in word:
        if ch in vowels:
            count += 1
            list_vowels.append(ch)
    
    return count, list_vowels


count, vowel_list = vowels_count("abhi")
print("Number of vowels:", count)
print("Vowels in the word:", vowel_list)

# check prime number
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if prime(number):
    print(number, "is a prime number.")    
else:
    print("it is not a prime number.")

# check leap year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
#uppercase or lowercase
def lower_upper(char):
    if char.islower():
        return "lowercase"
    elif char.isupper():
        return "uppercase"
    else:
        return "not an alphabet"
char = input("Enter a character: ")
result = lower_upper(char)
print(f"The character is {result}.")


# extract uppercase letters from a word
def upper_case(word):
    result = ""
    for ch in word:
        if ch.isupper():
            result += ch
    return result

word = input("Enter the word: ")
print("Uppercase letters:", upper_case(word))

# check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


check_even_odd(10)
check_even_odd(7)

