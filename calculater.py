first = input("Enter 1st no: ")
operator = input("Enter operator(+,-,*,/,%): ")
second = input("Enter 2nd no: ")
first = int(first)
second = int(second)
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first+second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("invalid-no-operator")
