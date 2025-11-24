#print only character in the items
items = ['a', 3, 'b', 7, 'c', 10]

for x in items:
    if str(x).isalpha():   
        print(x)


#multiple exceptions
try:
    x = int("abc1234")   
except (ValueError, TypeError, IndexError):
    print("Error happened")

#exception as e
try:
    x = int("abc")
except Exception as e:
    print("Error:", e)

#exception handling inside function
def divide(value):
    try:
        x = int(value)
        print(10 / x)
    except (ZeroDivisionError, ValueError):
        print("Error: invalid input or division by zero")

divide("10")
divide("0")
divide("abc")



