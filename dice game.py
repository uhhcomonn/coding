import math
import inquirer
import random
# def dice_guessing():
#     dice_num = random.randint(1,6)
#     for tries in range(3):
#         try:
#             user_num = int(input("Guess the number: "))
#             if user_num in range(1,7):
#                 break
#             else:
#                 print("The number you have entered isn't a dice number")
#         except ValueError:
#             print("Please enter a number")
# def dice_roller():
#     rolls = int(input("How many times do you want to roll the dice: "))
#     for i in range(rolls):
#         dice_num = random.randint(1,6)
#         return dice_num
# def multiple_dice():
#     rolls = int(input("How many times do you want to roll the dice: "))
#     sum = 0
#     for j in range(rolls):
#         dice_num = random.randint(1,6)
#         sum+= dice_num
#     return sum
# options = {dice_guessing(), dice_roller(), multiple_dice()}
# inquirer.List(name="User choice", message="Choose an operation: ", choices=options, default=dice_roller(), ignore= False, validate=True)
def main():
    for tries in range(3):
        try:
            times = int(input("How many times do you want to roll the dice: "))
            if times > 0:
                break
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Please enter a number")
    for i in range(times):
        print(random.randint(1,6))
if __name__ == "__main__":
    main()