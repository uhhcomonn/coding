import random
import inquirer
rps = ["Rock", "Paper", "Scissors"]
user_choice = [inquirer.List(name = "rps", message = "Please choose one:", choices = rps, carousel=True)]
player = inquirer.prompt(user_choice)
player = player['rps']
def comprock(player):
    if player == "Rock":
        return "Tie"
    elif player == "Paper":
        return "You Win"
    elif player == "Scissors":
        return "You Lose"
    else:
        return "Error"
def comppaper(player):
    if player == "Paper":
        return "Tie"
    elif player == "Scissors":
        return "You Win"
    elif player == "Rock":
        return "You Lose"
    else:
        return "Error"
def compscissors(player):
    if player == "Scissors":
        return "Tie"
    elif player == "Paper":
        return "You Lose"
    elif player == "Rock":
        return "You Win"
comp_choice = [comprock(player), comppaper(player), compscissors(player)]
result = random.choice(comp_choice)
print(result) 