def add(x, y):
    return x + y

def sub(x,y):
    return x - y

# here mer makes mul and div
def mul(x,y):
    return x * y
def div(x, y):
    return x/y
def main():
    no1 = int(input("Fill in a number: "))
    no2 = int(input("Fill in a second number: "))
    op = input("fill in an operator: ")

    if op == "+":
        print(add(no1, no2))
    elif op == "-":
        print(sub(no1, no2))
    elif op == "*":
        print(mul(no1, no2))
    elif op == "/":
        print(div(no1, no2))
    else:
        print("run the script again with a valid operator!")
main()

print("test if merge is successful")
print("this id end of the work")