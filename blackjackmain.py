import random


def dealcards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    # Check for a Blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Adjust for Ace (11) if sum exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_scorev(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Opponent has blackjack!"
    elif u_score == 0:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You lose! You went over 21."
    elif c_score > 21:
        return "You win! Opponent went over 21."
    elif c_score < u_score:
        return "You win!"
    else:
        return "You lose!"


def play_blackjack():
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Initial deal
    for i in range(2):
        user_card.append(dealcards())
        computer_card.append(dealcards())

    # Game loop
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your Cards: {user_card}, Your Score: {user_score}")
        print(f"Computer's First Card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice_draw = input("Type 'y' to draw a card, or 'n' to pass: ").lower()
            if user_choice_draw == "y":
                user_card.append(dealcards())
            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_card.append(dealcards())
        computer_score = calculate_score(computer_card)

    # Compare final scores
    final_result = compare_scorev(user_score, computer_score)
    print(f"Your final hand: {user_card}, Final Score: {user_score}")
    print(f"Computer's final hand: {computer_card}, Final Score: {computer_score}")
    print(final_result)


# Main loop to continue playing
while True:
    play_blackjack()
    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if play_again != 'y':
        break

print("Thanks for playing!")
