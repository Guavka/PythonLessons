from modules.coffee_machine_new import get_coffee_order

if __name__ == '__main__':
    drink_dict = {
        'кофе': {
            '200': 100,
            '300': 150,
            '400': 200
        },
        'чай': {
            '150': 80,
            '200': 100
        },
        'латте': {
            '350': 170,
            '400': 220
        },
        'капучино': {
            '300': 200,
            '350': 250
        },
    }

    add_dict = {
        'лимон': 5,
        'молоко': 20,
        'корица': 10,
        'ничего': 0
    }

    order = get_coffee_order(add_dict=add_dict, drink_dict=drink_dict)
    print(order)
