num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

if (num1 > num2) and (num1 > num3):
    print(f"{num1} is greater")
if (num2 > num1) and (num2 > num3):
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")