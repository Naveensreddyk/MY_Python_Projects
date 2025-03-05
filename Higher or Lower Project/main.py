import random
from art import logo, vs
from game_data import data

def formating_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers and user_guess == "a":
        return "You are right"
    elif a_followers > b_followers and user_guess == "b":
        return "You are wrong"
    elif a_followers < b_followers and user_guess == "a":
        return "You are wrong"
    elif a_followers < b_followers and user_guess == "b":
        return "You are right"
print(logo)
score = 0
game_play = True
account_b = random.choice(data)
while game_play:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    print(f"Compare A: {formating_data(account_a)}")
    print(vs)
    print(f"Against B: {formating_data(account_b)}")
    guess = input("Who has the more followers. Type A or B:").lower()

    correct_answer = check_answer(guess, a_followers_count, b_followers_count)
    if correct_answer == "You are right":
        score += 1
        print("\n" * 30)
        print(logo)
        print(f"You are Right and your current score is {score}.")

    else:
        print(f"Sorry, that is wrong and your final score is {score}.")
        game_play = False



