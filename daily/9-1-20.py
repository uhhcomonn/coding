import math
#first program

num_1 = float(input("First No: ")) #inputs numbers
num_2 = float(input("Second No: "))
num_3 = float(input("Third No: ")) 
def sum(num_1, num_2, num_3): #finds sum
    return (sum)
def largest(num_, num_2, num_3): # finds the largest number
   if num_2 > num_2 and num_1 > num_3:
            print("The largest of the three numbers is: " + str(num_2))
   elif num_3 > num_3:
      print("The largest of the three numbers is: " + str(num_3))
      sum = num_2 + num_2 + num_3  
   else:
      print("The largest of the three numbers is: " + str(num_3))
print("The sum is: " + str(sum(num_1, num_2, num_3)))
largest(num_1, num_2, num_3)

# except num_1 == num_2 | num_2 == num_3 | num_1 == num_3:
#     if num_1 == num_2 & num_1 > num_3:
#         print("The first and the second number are equal and are greater than the third")
#     elif num_1 == num_2 & num_1 < num_3:
#         print("The third number is the greatest")
#     elif num_1 
        
#         if num_1 > num_3: 
#             print("The first number is the greatest")
#         else:
#             print("The third number is the greatest")
#     else:
#         if num_2 > num_3:
#             print("The second number is the greatest")
#         else:
#             print("The third number is the greatest")            
# except num_1 == num_2 | num_2 == num_3 | num_1 == num_3:
#     if num_1 == num_2 == num_3:
#         print("All")



#Second Program

# print("This program allows you to do one of four operations: \n a) Area of a Circle \n b) Area of a Rectangle \n c) Circumference of a Circle \n d) Area of a Square ")
# option = input("Select your option: ")
# if option == "a":
#     r = float(input("Radius: ")) #asks user radius
#     print(math.pi*r*r)           #prints the area 
# elif option == "b":
#     l = float(input("Length: ")) #asks user dimensions
#     b = float(input("Breadth: "))
#     print(l*b)                   #prints the area
# elif option == "c":
#     r = float(input("Radius: "))
#     print(2*math.pi*r)           #prints the circumference
# elif option == "d":
#     side = float(input("Side: "))#asks user the side length
#     print(math.pow(side, 2))
# else:
#     print("Try again by only using the letters to choose the option, a b, c,d")

#Third program

# print("This program asks for two numbers and an operator and does the math for you.")
# print("Supported operators :- \n'+' for addition\n'-' for subtraction\n'*' for multiplication\n'/' for division")
# print("'//' for floor division \n'%' for finding the remainder \n'**' for exponentiation")
# num1 = float(input("First Number: "))
# num2 = float(input("Second Number: "))
# operator = input("Operator: ")
# if operator == "+":
#     print("The sum is: " + str(num1 + num2))
# elif operator == "-":
#     print("The difference is:" + str(num1 - num2 ))
# elif operator == "*":
#     print("The product is: " + str(num1 * num2))
# elif operator == "/":
#     print("The quotient is: " + str(num1 / num2))
# # elif operator == "//":
# #     print("The quotient is: " + str(num1 // num2))
# # elif operator == "%":
# #     print("The remainder is: " + str(num1 % num2))
# # elif operator == "**":
# #     print("The answer is: " + str(num1 ** num2))
# else:
#     print("Invalid operator")

#Fourth program
# print("Type:\n'table' for multiplication table \n'fib' for fibonacci sequence\n'!' for factorial")
# option = input("Type Here: ")
# if option == "table":
#    num = int(input("Enter number:"))
#    for i in range (10):
#       prod = num * ( i + 1)
#       print(prod)
# elif option == "fib":      
#    nterms=int(input("How many terms? "))
#    n1, n2 = 0, 1
#    count = 0
#    if nterms <= 0:
#       print("Please enter a positive integer")
#    elif nterms== 1:
#       print("Fibonacci sequence upto", nterms,":")
#       print(n1)
#    else:
#       print("Fibonacci sequence:")
#       while count < nterms:
#          print(n1)
#          nth = n1 + n2
#          # update values
#          n1 = n2
#          n2 = nth
#          count += 1
# elif option == "!":
#    num = int(input("Enter Number: "))
#    if num < 0:
#       print("Factorial isn't defined for negative numbers")
#    elif num == 0:
#       print("1")
#    else:
#       i = 1#index for counting
#       answer = 1 # 
#       while i < num:
#          answer = answer * (i+1)
#          i+=1
#       print(answer)

#Fifth program
# print("Type\n'oe' for odd/even \n'pal' for palindrome\n'arm' for armstrong number ")
# option = input("Enter Here: ")
# if option == "oe":
#    num = int(input("Enter Number: "))
#    if (num % 2) == 1:
#       print("The number is odd")
#    else:
#       print("The number is even")
# elif option == 'pal':
#    user_input = input("Enter a number or a word: ")
#    if user_input[::-1]== user_input:
#       print("This number/word is a palindrome")
#    else:
#       print("This number/word is not a palindrome")
# elif option == 'arm':
#    num = input("Enter a Number: ")
#    cube_sum = 0
#    for digit in list(num):
#       cube_sum = cube_sum + (int(digit)**3)
#    if cube_sum == int(num):
#       print("This number is an armstrong number")
#    else:
#       print("This number is not an armstrong number")
      
#Sixth program

# user_input = int(input("Enter number of lines: "))
def right_triangle_maker(alt, char):
   for i in range(alt):   #Straight triangle
      for j in range(i):
         print(char , end=" ")
      print()

def inverted_rt_triangle_maker(alt, char):
   i = 0
   for i in range(alt):   #Inverted triangle
      for j in range(alt - i):
         print(char, end=" ") 
      print()
def square_maker(side, char):
   i = 0
   for i in range(side):
      for j in range(side):  #Square
         print("@", end = " ")
      print()

def rectangle_maker(len, bre, char):
   for i in range(len):
      for j in range(bre):
         print(char, end = " ")
      print()   
   
