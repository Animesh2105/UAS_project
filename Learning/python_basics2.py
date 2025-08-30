def sum(x,y):
    z = x+y
    return z

def getNum():
    x = int(input("Enter a number: "))
    return x

num1 = getNum()
num2 = getNum()
print(f"The sum is {sum(num1, num2)}")
