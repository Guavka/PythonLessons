from modules.coffee_machine_rework import get_coffee_order
from utils import print_data

if __name__ == '__main__':

    drink_dict = {
        'кофе': {
            200: 100,
            300: 150,
            350: 200
        },
        'чай': {
            300: 100,
            400: 120
        },
        'латте': {
            200: 120,
            300: 170,
            400: 220
        },
        'эспрессо': {
            150: 100,
        },
    }

    add_dict = {
        'лимон': 5,
        'молоко': 20,
        'корица': 10,
    }

    order = get_coffee_order(drink_dict=drink_dict, 
                             add_dict=add_dict,
                             input_fn=input,
                             output_fn=print_data)
    print_data(order)