def addition(num1, num2): return num1+num2
def subtraction(num1, num2): return num1-num2
def multiplecation(num1, num2): return num1*num2
def division(num1, num2): return num1/num2
def module(num1, num2): return num1%num2 
def default(num1,num2): return "Incorrect Method"


switcher = {
    1: addition,
    2: subtraction,
    3: multiplecation,
    4: division,
    5: module
    }

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Module ''')

choice = int(input("Select operation from 1,2,3,4,5 : "))
print(switcher.get(choice, default)(num1, num2))


