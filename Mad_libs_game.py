user_data = [
    input("Enter a name: ").strip(),
    input("Enter a colour: ").strip(),
    input("Enter an animal: ").strip(),
    input("Enter an object: ").strip(),
    input("Enter a place: ").strip().capitalize(),
    input("Enter an occupation: ").strip()]
animal = user_data[2]
occupation = user_data[4]
vowels = ["a", "e", "i", "o", "u"]
# if animal[0] in vowels:
#     article = "an"
# else:
#     article = "a"
# if occupation[0] in vowels:
def article(word):
    vowels = {"a", "e", "i", "o", "u"}
    if word[0] in vowels:
        return "an"
    else:
        return "a"
print(user_data[0].capitalize(), "went to the school with a", user_data[1], "backpack.")
print("He met", article(user_data[2]), user_data[2], "on the way there.")
print("The", user_data[2], "tried to attack", user_data[0]+ "." )
print(user_data[0].capitalize(), "used", article(user_data[3]), user_data[3], "to defend.")
print(article(user_data[-1]).capitalize(), user_data[-1], "from", user_data[-2], "saw this and rushed.") 
print("The", user_data[-1], "called the cops in time and saved the day.")
print(user_data[0], "thanked the", user_data[-1], "and continued on his way.")

