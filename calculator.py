# n1 = float(input("Enter first number: "))
# operator = input("Enter operator: ")
# n2 = float(input("Enter second number: "))
# operator_list = {
#     "+" : n1+n2,
#     "-" : n1-n2,
#     "*" : n1*n2,
#     "/" : n1/n2 if n2!=0 else "Can't divide by zero",
#     "//": n1//n2 if n2!=0 else "Can't divide by zero",
#     "%" : n1%n2 if n2!=0 else "Can't divide by zero",
#     "**": n1**n2,




# }
# print(operator_list[operator])
expression = input("Enter an expression: ")
exec("ans = "+ expression )
print(ans)