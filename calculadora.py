print()
print()
print()
result = 0

print("This is a calculator, you have to choose between multiplication / division / subtraction / sum / module")

operation = input("What kind of operation are you doing?").upper()

first_number = float(input("What is your first number?"))
second_number = float(input("What is the second number?"))

if operation == "MULTIPLICATION":
    result = first_number * second_number
if operation == "DIVISION":
    result = first_number / second_number
if operation == "SUBTRACTION":
    result = first_number - second_number
if operation == "SUM":
    result = first_number + second_number
if operation == "MODULE":
    result = first_number % second_number

print("This is the result : {}".format(result))
