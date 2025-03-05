import random
import time
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack!
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    time.sleep(1)  # Adds suspense
    print("\n🔄 Comparing scores... 🔄")
    time.sleep(1.5)

    if u_score == c_score:
        return "🤝 It's a Draw! So close!"
    elif c_score == 0:
        return "💀 You Lose! The opponent has Blackjack!"
    elif u_score == 0:
        return "🎉 Blackjack! You Win!"
    elif u_score > 21:
        return "💥 You went over 21! Game Over!"
    elif c_score > 21:
        return "🔥 The opponent busted! You Win!"
    elif u_score > c_score:
        return "🎊 You Win! Great strategy!"
    else:
        return "😞 You Lose! Better luck next time!"

def play_game():
    print("\n" * 5)  # Clears screen for a fresh start
    print(art.logo)
    print("🎰 Welcome to the Ultimate Blackjack Challenge! 🎰\n")

    user_cards = []
    computer_cards = []
    user_score = 0  # Initialize the user score
    computer_score = 0  # Initialize the computer score
    is_game_over = False

    # 🎴 Dealing Initial Cards
    print("✨ Shuffling the deck... ✨")
    time.sleep(1)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n🃏 Your cards: {user_cards} | Current score: {user_score}")
        print(f"💻 Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\n🔄 Type 'y' to draw another card or 'n' to pass: \n").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
                print("\n✨ Drawing a new card... ✨")
                time.sleep(1)
            else:
                is_game_over = True

    # Dealer's turn 🎲
    while computer_score != 0 and computer_score < 17:
        print("\n💻 Dealer is drawing a card...")
        time.sleep(1)
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results 🏆
    print("\n🎲 Final Results 🎲")
    time.sleep(1)
    print(f"🃏 Your final hand: {user_cards} | Final score: {user_score}")
    print(f"💻 Dealer's final hand: {computer_cards} | Final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("\n🃏 Ready for a round of Blackjack? Type 'y' to play, 'n' to exit: \n").lower() == "y":
    print("\n" * 50)
    play_game()
