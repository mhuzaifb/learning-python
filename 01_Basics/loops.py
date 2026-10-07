count = 1
while count <= 5:
    print(count)
    count += 1
#1-10
num = 1
while num <= 10:
    print(num)
    num += 1
#2-10 even
even = 2
while even <= 10:
    print(even)
    even += 2
#User
i = 1
user = int(input("Enter your number: "))
while i <= user:
    print(i)
    i += 1
#For
for i in range(1, 6):
    print(i)
#1-10
for t in range(1, 11):
    print(t)
#even
for e in range(2, 10):
    if e % 2 == 0:
     print(e)
#Even 2
for e in range(2, 11, 2):
    print(e)
#User
user = int(input("Give the number to print: "))
for i in range(1, user  + 1):
    print(i)
#for without user input
for i in range(10, -2, -1):
    print(i)
for i in range(2, 21, 2):
    print(i)
for i in range(1, 20, 2):
    print(i)
_num1 = int(input("Enter your number: "))
for i in range(1,11):
    print(_num1, "x", i, "=", i * _num1)
for i in range(1, 16):
    print(f"{_num1} x {i} = {_num1 * i}")
for i in range(1, 11):
    if i == 7:
        break
    print(i)
print("Out Baby")
for i in range(1, 20):
    if i == 15:
        continue
    print(i)
print("Again Out Baby")
for i in range(1, 10, 2):
    for j in range(1, 10, 3):
        print(i, j)
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()