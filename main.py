
print("hello world!");

myColors = ["blue", "red", "green", "yellow", "brown", "orange"]

print("this my fovourt", myColors)

message = "Welcome to the python world!"
score = 100
price = 19.99
is_complete = True

print(type(message), type(score), type(price), type(is_complete))

a = 10
b = 5

# Addition
print("Addition:", a + b)

# Subtraction

print("Subtraction:", a - b)

# Multiplication

print("Multiplication:", a * b)

# Division

print("Division:", a / b)

# Conditions (if-else)
age = int(input("Enter your age:") )

if age >= 18:
    print("You are eligible to vote")
elif age == 18: 
    print("You are just 18 years old")
else: 
    print("You are not eligible to vote")

# Loops

for i in range(3):
   print("hello!", i)

# While Loop

count = 0

while count < 3:
    print("hello!", count)
    count += 1


# Functions

def greet(name):
    print(f"Hello, {name}!")
    
greet("Yasin")