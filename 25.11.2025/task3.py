#print the lowest and highest prime number in the list
list = [3, 10, 7, 15, 2, 19]
primes = []
for n in list:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primes.append(n)

print("Lowest =", min(primes))
print("Highest =", max(primes))


#print the hcf and lcm of the numbers
a = 10
b = 20


hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i


lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("HCF =", hcf)
print("LCM =", lcm)

#total array
arr = [1, 2, 3]
total = 0

for num in arr:
    total += num

print(total)

#print largest and smallest array
arr = [1, 2, 3]

small = arr[0]
large = arr[0]

for n in arr:
    if n < small:
        small = n
    if n > large:
        large = n

print("Smallest =", small)
print("Largest =", large)

#print the string
arr = [1, "hello", 25, "abc", 5, "python"]

for x in arr:
    try:
        int(x)     
    except:
        print(x)   

#remove the empty
arr = [[1, 2], [], [3, 4]]

new_arr = []

for x in arr:
    if x != []:       
        new_arr.append(x)

print(new_arr)

#calendar
import calendar
mm = 12
yy = 2025
print(calendar.month(yy, mm))

#print values dictionary in separate
d = {'a': 1, 'b': 2, 'c': 3}

for key in d.keys():
    print(key, "=", d[key])

#call the name with the number
num = int(input("Enter number: "))

if num == 1:
    print("Abhi")
elif num == 2:
    print("nethra")
elif num == 3:
    print("alwar")
elif num == 4:
    print("maha")
else:
    print("Invalid number")

#change order with the index
num = "12345"
order = [3, 4, 1, 2, 0]
result = ""
for i in order:
    result += num[i]

print(result)

#fizzbuzz
num = 10

if num % 2 == 0 and num % 5 == 0:
    print("fIzzBuzz")
elif num % 2 == 0:
    print("fIzz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by 2 or 5")
