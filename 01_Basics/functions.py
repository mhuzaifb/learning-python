def greet():
    print("Hello, MHuzaif")
greet()
def greet(name):
    print(f"Hello, {name}")
greet("Beigh")
greet("Ali")
greet("Ahmed")
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
introduce("Mhuzaif", 18)
introduce("Ali", 20)
def add(a, b):
    print(a + b)
add(5, 3)
def add(a, b):
    return a + b
result = add(5, 3)
print(result)
print(result * 2)
print(result / 10)
print(result % 2)
print(result // 2)
print(result - 10)
print(result + 10)
print(result == 10)
def multiply(a, b):
    return a * b
answer = multiply(4, 5)
print(answer)
print(answer * 2)
print(answer / 10)
print(answer % 2)
print(answer // 2)
print(answer - 10)
print(answer + 10)
print(answer == 10)
def greet(name="Mhuzaif"):
    print(f"Hello, {name}")
greet()
greet("Ali")
def power(number, exponent=2):
    return number ** exponent
print(power(5))
print(power(5, 3))
def multiply(a, b=2):
    return a * b
answer = multiply(5)
print(answer)
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")
introduce("Mhuzaif", 18, "Srinagar")
introduce(age=18, city="Srinagar", name="Mhuzaif")
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
print(check_age(65))
print(check_age(4))
def square(number):
    return number * number
answer = square(32)
print(answer)
print(answer / 2)
print(answer // 2)
print(answer % 2)
print(answer ** 2)
print(answer - 22)
def is_adult(age):
    return age >= 18
print(is_adult(23))
print(is_adult(2))
def calculate(a, b):
    return a + b, a - b
result = calculate(10, 3)
print(result)
addition, subtraction = calculate(10, 3)
print(addition)
print(subtraction)
def math_operations(a, b):
    return a + b, a - b, a * b, a / b
add, subtract, multiply, divide = math_operations(10, 2)
print(add)
print(subtract)
print(multiply)
print(divide)
def student_info(name, age):
    return name, age
name, age = student_info("Mhuzaif", 18)
print(name)
print(age)
def add_all(*numbers):
    print(numbers)
    print(len(numbers))
add_all(11, 2, 22)
add_all(22, 33, 434)