from models.deck import Deck
from models.players.bank import Bank
from models.players.player import Player


def start_round(player: Player, bank: Bank, bet=100):
    from typing import List

    def get_cards(players: List[Player], count=2):
        assert type(players) == list, 'Нужен лист'

        for i in range(count):
            for player in players:
                player.add_card(deck.get_card())

    def bank_get_cards():
        while True:
            if bank.score >= 15:
                break
            bank.add_card(deck.get_card())

    def player_get_cards():
        while True:
            user_choose = input(
                f'Your score: {player.score}\nGet card?\n1 - Yes\n2 - No')
            if user_choose == '1':
                player.add_card(deck.get_card())
            elif user_choose == '2':
                break
            else:
                print('Error! Input 1 or 2')

    def get_winner():
        print(f'Player score: {player.score}\nBank score: {bank.score}')

        if bank.score == player.score:
            print('Draw')
        elif bank.score > 21:
            if player.score < bank.score:
                print('Player win')
                player.add_money(bet*2)
            else:
                print('Bank win')
        else:
            if player.score < bank.score:
                print('Bank win')
            else:
                print('Player win')
                player.add_money(bet*2)

    deck = Deck()

    player.subtract_money(bet)
    bank.subtract_money(bet)

    get_cards([player, bank])

    bank_get_cards()
    player_get_cards()
    get_winner()
    
    user_choose = input('Start new round?\n1 - Yes\n2 - No')
    if user_choose == '1':
        player.clear_hand()
        bank.clear_hand()
    elif user_choose == '2':
        return
        