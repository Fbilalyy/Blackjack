import random


def generate_deck(_suits, _cards):
    random.seed(0)
    n = 0
    deck = [(i, j) for i in _suits for j in _cards]
    random.shuffle(deck)
    while True:
        yield deck[n]
        n += 1
        if n == 52:
            random.shuffle(deck)
            n = 0


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shuffled_deck = generate_deck(suits, cards)


def get_next_card():
    return next(shuffled_deck)


cards_values = {
    ('Spades', 'A'): 10,
    ('Hearts', 'A'): 10,
    ('Clubs', 'A'): 10,
    ('Diamonds', 'A'): 10,
    ('Spades', '2'): 2,
    ('Hearts', '2'): 2,
    ('Clubs', '2'): 2,
    ('Diamonds', '2'): 2,
    ('Spades', '3'): 3,
    ('Hearts', '3'): 3,
    ('Clubs', '3'): 3,
    ('Diamonds', '3'): 3,
    ('Spades', '4'): 4,
    ('Hearts', '4'): 4,
    ('Clubs', '4'): 4,
    ('Diamonds', '4'): 4,
    ('Spades', '5'): 5,
    ('Hearts', '5'): 5,
    ('Clubs', '5'): 5,
    ('Diamonds', '5'): 5,
    ('Spades', '6'): 6,
    ('Hearts', '6'): 6,
    ('Clubs', '6'): 6,
    ('Diamonds', '6'): 6,
    ('Spades', '7'): 7,
    ('Hearts', '7'): 7,
    ('Clubs', '7'): 7,
    ('Diamonds', '7'): 7,
    ('Spades', '8'): 8,
    ('Hearts', '8'): 8,
    ('Clubs', '8'): 8,
    ('Diamonds', '8'): 8,
    ('Spades', '9'): 9,
    ('Hearts', '9'): 9,
    ('Clubs', '9'): 9,
    ('Diamonds', '9'): 9,
    ('Spades', '10'): 10,
    ('Hearts', '10'): 10,
    ('Clubs', '10'): 10,
    ('Diamonds', '10'): 10,
    ('Spades', 'J'): 10,
    ('Hearts', 'J'): 10,
    ('Clubs', 'J'): 10,
    ('Diamonds', 'J'): 10,
    ('Spades', 'Q'): 10,
    ('Hearts', 'Q'): 10,
    ('Clubs', 'Q'): 10,
    ('Diamonds', 'Q'): 10,
    ('Spades', 'K'): 11,
    ('Hearts', 'K'): 1,
    ('Clubs', 'K'): 11,
    ('Diamonds', 'K'): 1,
}


def calculate_total_value(cards_set):
    total_value = 0
    for card in cards_set:

        total_value += cards_values[card]
    return total_value


print("Sage's money:")
print("Number of games:")
money_of_sage = int(input())
numbers_of_games = int(input())
for game_number in range(int(numbers_of_games)):
    game_number += 1
    print("\nGame:", game_number)
    cards_of_sage = set()
    cards_of_king = set()
    cards_of_sage.add(get_next_card())
    cards_of_sage.add(get_next_card())
    cards_of_king.add(get_next_card())
    cards_of_king.add(get_next_card())
    points_of_sage = calculate_total_value(cards_of_sage)
    points_of_king = calculate_total_value(cards_of_king)
    h_s = ""
    one_card_point_of_king = calculate_total_value([list(cards_of_king)[1]])
    print("King’s cards:", "(*)", list(cards_of_king)[1])
    print("Total value:", one_card_point_of_king)
    print("Sage’s cards:", list(cards_of_sage))
    print("Total value:", points_of_sage)
    game = ""
    while game_number:
        if game_number <= numbers_of_games:
            game_number = True
            if points_of_sage < 21:
                print("Do you want to hit or stand? [H/S]")
                h_s = input().lower()
                if h_s == "hit" or h_s == "h":
                    cards_of_sage.add(get_next_card())
                    points_of_sage = calculate_total_value(cards_of_sage)
                    points_of_king = calculate_total_value(cards_of_king)
                    print("Sage’s cards:", list(cards_of_sage))
                    print("Total value:", points_of_sage)
                    while game:
                        print("Do you want to hit or stand? [H/S]")
                        h__s = input().lower()
                        if h__s == "hit" or h__s == "h":
                            cards_of_sage.add(get_next_card())
                            points_of_sage = calculate_total_value(cards_of_sage)
                            points_of_king = calculate_total_value(cards_of_king)
                            print("Sage’s cards:", list(cards_of_sage))
                            print("Total value:", points_of_sage)
                            if points_of_sage >= 21:
                                money_of_sage -= 50
                                print("You busted! You lost!")
                                break

                            elif points_of_sage == 21:
                                money_of_sage += 50
                                print("It is Blackking! You won!")
                                break
                            elif points_of_sage < 21:
                                break
                        elif h__s == "stand" or h__s == "s":
                            one_card_point_of_king = calculate_total_value([list(cards_of_king)[0]])
                            points_of_king = calculate_total_value(cards_of_king)
                            print("King’s cards:", list(cards_of_king))
                            print("Total value:", points_of_king)
                            while points_of_king < 17:
                                cards_of_king.add(get_next_card())
                                points_of_king = calculate_total_value(cards_of_king)
                                print("King’s cards:", list(cards_of_king))
                                print("Total value:", points_of_king)
                                if points_of_king >= 17 and points_of_king <= 21:
                                    if points_of_king > points_of_sage:
                                        money_of_sage -= 50
                                        print("King has higher value. You lost!")
                                        game = False
                                    elif points_of_king < points_of_sage:
                                        money_of_sage += 50
                                        print("You have higher value. You won!")
                                        game = False
                                    elif points_of_king == points_of_sage:
                                        print("It is a tie!")
                                        game = False
                                elif points_of_king > 21:
                                    money_of_sage += 50
                                    print("King busted! You won!")
                                    game = False
                        break
                elif h_s == "stand" or h_s == "s":
                    one_card_point_of_king = calculate_total_value([list(cards_of_king)[0]])
                    points_of_king = calculate_total_value(cards_of_king)
                    print("King’s cards:", list(cards_of_king))
                    print("Total value:", points_of_king)
                    while points_of_king < 17:
                        cards_of_king.add(get_next_card())
                        points_of_king = calculate_total_value(cards_of_king)
                        print("King’s cards:", list(cards_of_king))
                        print("Total value:", points_of_king)
                    if points_of_king >= 17 and points_of_king <= 21:
                        if points_of_king > points_of_sage:
                            money_of_sage -= 50
                            print("King has higher value. You lost!")
                            break
                        elif points_of_king < points_of_sage:
                            money_of_sage += 50
                            print("You have higher value. You won!")
                            break
                        elif points_of_king == points_of_sage:
                            print("It is a tie!")
                            break
                    elif points_of_king > 21:
                        money_of_sage += 50
                        print("King busted! You won!")
                        break
                else:
                    game = False
            elif points_of_sage == 21:
                money_of_sage += 50
                print("It is Blackking! You won!")
                break
            else:
                money_of_sage -= 50
                print("You busted! You lost!")
                break
        else:
            game_number = False

print(money_of_sage)
