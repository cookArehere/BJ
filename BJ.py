import random

"""
задание под звездочкой большое. Но попробуйте.

Пишем игру в 21. Создать массив "карт" рандомно их перемешать и выдавать "игроку" пока не скажет стоп или не проиграет. 

карта - словарь. Масть, Название, очки.  Не надо мудрить с "вариантами очков карт" упрощенно. 
Интересует работа с циклами, словарями, функциями :)
Помним про единую ответственность. Разбиваем на примитивные действия. 
С начала пишем каркас с запассенными функциями, а потом заполняем "пропуски". 

пока не стоп или перебор
 предложить карту
 вывести текущие очки.
если не перебор набирать себе карт (я не знаю точных правил как правильно 
если тоже не в курсе пусть скрипт набирает до 18ти очков например или проигрыша)
"""


def create_cart_decks(x=1):
    """
    Создает список переменных карт
    :param x: количество колод
    :return: последовательность карт (cart_значениекарты_масть, cart_значениекарты_масть...)
    """
    carts = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    carts_suit = ["heart", "diamond", "club", "spade"]
    cart_deck = []

    for i in carts:
        for j in carts_suit:
            cart_deck.append(f"cart_{i}_{j}")
    return cart_deck * x


def fill_carts(cart_deck):
    """
    ссоздает  словари(карты) с ключами name, suit, points
    :return: масив словарей(карт)
    """

    cart = {
        "name": "",
        "suit": "",
        "points": "",
    }

    fill_cart_deck = []

    for i in cart_deck:
        weight = i.replace("cart_", "").split("_")
        if weight[0] == "J":
            weight[0] = "2"
        elif weight[0] == "Q":
            weight[0] = "3"
        elif weight[0] == "K":
            weight[0] = "4"
        elif weight[0] == "A":
            weight[0] = "11"
        i = {**cart, "name": i, "suit": weight[1], "points": weight[0]}
        fill_cart_deck.append(i)
    return fill_cart_deck


def name_cards(card_order):
    """
    собирает в список карты на руках
    :param card_order: словарь карт
    :return: список состоящий с назманий карт
    """
    name_cards = []
    for i in card_order:
        name_cards.append(i["name"])
    return name_cards


def points_cards(card_order):
    """
    подсчитывает количесвот очет на руках
    :param card_order: словарь карт
    :return: количесво очков на руках
    """
    points_cards = 0
    for i in card_order:
        points_cards += int(i["points"])
    return points_cards


if __name__ == '__main__':

    cart_deck = create_cart_decks()
    game_deck = fill_carts(cart_deck)
    play = input("Would you like to play the game? y/n:")

    if play.lower() == "y":
        computer_cards = [game_deck.pop(random.randint(0, len(game_deck) - 1)),
                          game_deck.pop(random.randint(0, len(game_deck) - 1))]
        human_cards = [game_deck.pop(random.randint(0, len(game_deck) - 1)),
                       game_deck.pop(random.randint(0, len(game_deck) - 1))]
        name_computer_cards = name_cards(computer_cards)
        points_computer_cards = points_cards(computer_cards)
        name_human_cards = name_cards(human_cards)
        points_human_cards = points_cards(human_cards)

        play = (input(
            f"You carts is {name_human_cards} and you have {points_human_cards} points \n Do you need one more card? y/n:"))

        while play.lower() == "y":
            human_cards.append(game_deck.pop(random.randint(0, len(game_deck) - 1)))
            name_human_cards = name_cards(human_cards)
            points_human_cards = points_cards(human_cards)
            if points_human_cards > 21:
                print(
                    f"You carts is {name_human_cards} and you have {points_human_cards} points \n It's more as 21 points. You are lose!")
                break
            play = (input(
                f"You carts is {name_human_cards} and you have {points_human_cards} points \n Do you need one more card? y/n:"))
        else:
            # компьютер берет себе каты
            counter = points_computer_cards % 10
            yes = ["y" * counter, "n" * (10 - counter)]

            while random.choice(yes) == "y" or points_computer_cards <= 15:
                computer_cards.append(game_deck.pop(random.randint(0, len(game_deck) - 1)))
                name_computer_cards = name_cards(computer_cards)
                points_computer_cards = points_cards(computer_cards)
                counter = points_computer_cards % 10
                yes = ["y" * counter, "n" * (10 - counter)]

            if points_computer_cards > 21:
                print(f"My carts is {name_computer_cards} and I have {points_computer_cards} points\n"
                      f"Your carts is {name_human_cards} and you have {points_human_cards}\n"
                      f"I have more as 21 points. You are WIN!")
            elif points_computer_cards > points_human_cards:
                print(f"My carts is {name_computer_cards} and I have {points_computer_cards} points\n"
                      f"Your carts is {name_human_cards} and you have {points_human_cards}\n"
                      f"I have more points. You are lose!")
            elif points_computer_cards < points_human_cards:
                print(f"My carts is {name_computer_cards} and I have {points_computer_cards} points\n"
                      f"Your carts is {name_human_cards} and you have {points_human_cards}\n"
                      f"You have more points. You are WIN!")
            elif points_computer_cards == points_human_cards:
                print(f"My carts is {name_computer_cards} and I have {points_computer_cards} points\n"
                      f"Your carts is {name_human_cards} and you have {points_human_cards}\n"
                      f"We have same points. It's draw.")
