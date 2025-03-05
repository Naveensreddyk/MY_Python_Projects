import random
import hangman_words
import hangman_art
print(hangman_art.logo)
reversed_stages = hangman_art.stages[::-1]
chosen_word = random.choice(hangman_words.word_list)
lives = 6
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
display = ""
guess = ""
old_letter = []
while guess != chosen_word:
    if lives == 0:
        print(f"IT WAS {chosen_word}. YOU LOSE")
        print("GAME OVER. YOU LOSE")
        break
    guess = input("GUESS A LETTER: ").lower()
    temp_display = ""
    if guess in old_letter:
        print("YOU HAVE ALREADY GUESSED THIS LETTER.")
        print(f"YOU HAVE LIVES REMAINING: {lives}")
        print(reversed_stages[6 - lives])
        continue
    if guess not in chosen_word and guess not in old_letter:
        lives -= 1
        print(f"YOU HAVE GUESSED {guess}. YOU LOSE A LIFE")
    for letter in chosen_word:
        if letter == guess:
            temp_display += letter
            old_letter.append(guess)
        elif letter in old_letter:
            temp_display += letter
        else:
            temp_display += "_"
    display = temp_display
    print(display)
    print(f"YOU HAVE LIVES REMAINING: {lives}")
    print(reversed_stages[6-lives])
    if "_" not in display:
        print("YOU WIN")
        break
