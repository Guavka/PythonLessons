from scripts.game.menu import get_player
from scripts.game.round_controller import start_round
from scripts.models.players.bank import Bank


def start_game():
    player = get_player()
    bank = Bank()

    start_round(player, bank)
