import random
import math
rand_num = random.randint(0, 100)



for tries in range(5):
    try:
       user_num = int(input("Guess the number: "))
       if user_num in range(0, 101):
           break
       else:
           print("The number you have entered isnt between 0 and 100")
    except ValueError:
        print("You haven't entered a number, Try again!")




score = 5
# def hint(argument):
#     switcher={
#         0 : "mult_num = rand_num\nprint('These numbers are the multiples: ')\ni= 1\nwhile mult_num <=100:\n    i+=1\n    mult_num*=i\n    if mult_num <= rand_num:\n        mult_num=rand_num\n    else:\n        print(mult_num)\n        mult_num=rand_num"
#         1 : "if rand_num > user_num:\n    print('Your number is high')\nelse:\n    print('Your number is low')"
        
#     }
#     return switcher.get(argument, "Something went wrong")
#class hints(object):
def multiple(rand_num):
    for j in range(3):
        i = random.randint(0,10)
        multnum = rand_num*i
        return multnum
def hilo(rand_num, user_num) :
    diff = user_num - rand_num
    if diff in range(-10,0):
        return "You're low but close"
    elif diff in range(1,11):
        return "You're high but close"
    elif diff in range(-25,0):
        return"You're low"
    elif diff in range(1,26):
        return"You're high"
    elif diff < 0:
        return "You're too low"
    elif diff > 0:
        return "You're too high"
    else:
        return "Something went wrong"
def divisible(rand_num):
    for i in range(rand_num, 1,  -1):
        if ((rand_num % i) == 0) and rand_num != i:
            return i
while score > 0:
    if rand_num == user_num:
        print("You win") 
        break
    else:
        score -= 1
        print("You didn't guess correctly")
        hints ={ 0 :  "These are the multiples:\n" +  str(multiple(rand_num)),
                 1 : hilo(rand_num, user_num),
                 2 : "The number is divisible by:\n" + str(divisible(rand_num)),
                 }
        print(random.choice(hints))
        tries = 0
        for tries in range(5):
            try:
                user_num = int(input("Try again:"))
                if user_num in range(0, 101):
                    break
                else:
                    print("The number you have entered isnt between 0 and 100")
            except ValueError:
                print("You haven't entered a number, Try again!")

if score <= 0:
    print("You Lose")
    print("The number is ", rand_num)
else:
    print("Your Score is ", score)
print("The game has ended")
