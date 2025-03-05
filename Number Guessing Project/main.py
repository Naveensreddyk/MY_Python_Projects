import random
import art

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(user_guess, original_answer, attempts):
    if user_guess > original_answer:
        print("🔥 TOO HIGH! You've overshot the mark! The number hides beneath... 👀")
        return attempts - 1
    elif user_guess < original_answer:
        print("❄️ TOO LOW! Your guess is crawling on the ground... but the answer soars higher! 🚀")
        return attempts - 1
    else:
        print(f"🎉 BOOM! YOU'VE CRACKED THE CODE! 🎯 The hidden number was **{original_answer}**! 🏆💥")

def difficulty_level():
    level = input("💀 Dare to face the challenge? Choose your path: **'EASY'** or **'HARD'**?\n👉 ").lower()
    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def game_play():
    print(art.logo)
    print("🌟 **WELCOME TO THE ULTIMATE NUMBER GUESSING THRILLER!** 🌟")
    print("🕵️‍♂️ A **mystery number** lies hidden between **1 and 100**... Can you uncover it before it's too late?")

    answer = random.randint(1, 100)
    attempts = difficulty_level()
    guess = 0  # Placeholder to start the loop

    while guess != answer:
        print(f"\n⚠️ **WARNING:** Only **{attempts} attempts** remain. Every move could be your last chance...")
        guess = int(input("🔮 Enter your guess... but beware, every choice matters! 😈\n👉 "))
        attempts = check_answer(guess, answer, attempts)

        if attempts == 0:
            print("💀 **MISSION FAILED!** You're out of chances. The secret number was:", answer)
            print("🔁 **GAME OVER!** Fate has spoken... but will you challenge destiny again? 🔥")
            break

game_play()
