# car brand, year
class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_brand(self):
        print("Brand:", self.brand)

    def show_year(self):
        print("Year:", self.year)


c1 = car("BMW", 2021)
c2 = car("Ford", 2022)
c3 = car("Audi", 2019)

c1.show_brand()
c1.show_year()

c2.show_brand()
c2.show_year()

c3.show_brand()
c3.show_year()
  

# student name, marks    
class student:
    def __init__(self, name,marks):
        self.name = name
        self.marks=marks
    def show_name(self):
        print("Name:", self.name)
    def show_marks(self):
        print("Marks:", self.marks)        

s1=student("abhi",89)
s2=student("ajay",78)

s1.show_name()
s1.show_marks()
s2.show_name()
s2.show_marks()


# employee name, salary
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_name(self):
        print("name:", self.name)

    def show_salary(self):
        print("salary:", self.salary)


e1 = employee("ram", 50000)
e2 = employee("raj", 60000)

e1.show_name()
e1.show_salary()

e2.show_name()
e2.show_salary()


# person name, balance
class person:
    def __init__(self, name,balance):
        self.name=name
        self.balance=balance
    def show_name(self):
        print("name:",self.name)
    def show_balance(self):
        print("balance:",self.balance) 

p1=person("alice",100000)
p2=person("bob",150000)
p3=person("charlie",200000)
p4=person("david",250000)
p5=person("eve",300000)

p1.show_name()
p1.show_balance()

p2.show_name()
p2.show_balance()

p3.show_name()
p3.show_balance()

p4.show_name()
p4.show_balance()

p5.show_name()
p5.show_balance()


# bike brand, speed
class bike:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def show_brand(self):
        print("Brand:", self.brand)
    def show_speed(self):        
        print("Speed:", self.speed)

b1=bike("Yamaha",150)
b2=bike("Honda",180)

b1.show_brand()
b1.show_speed()

b2.show_brand()
b2.show_speed()

#phone brand, ram, processor
class phone:
    def __init__(self, brand, ram,processor):
        self.brand = brand
        self.ram = ram
        self.processor=processor
    def show_brand(self):    
        print("Brand:", self.brand)
    def show_ram(self):    
        print("RAM:", self.ram)
    def show_processor(self):
        print("Processor:", self.processor)    

p1=phone("Apple",4,"A14 Bionic")        
p2=phone("Samsung",6,"Exynos 2100")
p3=phone("OnePlus",8,"Snapdragon 888")

p1.show_brand()
p1.show_ram()
p1.show_processor()

p2.show_brand()
p2.show_ram()
p2.show_processor()

p3.show_brand()
p3.show_ram()
p3.show_processor()

#calculator 
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error! Division by zero."
calc = calculator(10, 5)
print("Addition:", calc.add())        
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
