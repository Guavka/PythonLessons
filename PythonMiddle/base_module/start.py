'''
from utils.console import print_data as console_print
from utils.logger import print_data as logger_print


if __name__== '__main__':
    console_print('test')
    logger_print('test')
'''
'''
from utils import print_data

if __name__== '__main__':
    print_data('test')
'''

from game.logic import start_game

if __name__== '__main__':
    start_game()