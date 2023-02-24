drink1_name = 'Coffee'

drink1_volume1 = '350ml'
drink1_volume1_price = 300

drink1_volume2 = '400ml'
drink1_volume2_price = 400

drink2_name = 'Tea'

drink2_volume1 = '400ml'
drink2_volume1_price = 400

while True:
    print('Welcome!')
    user_choose = input(f'1.{drink1_name}\n2.{drink2_name}\n3.Exit\n')

    if user_choose == '1':
        print(f'You choose {drink1_name}:\n\
1.{drink1_volume1}: {drink1_volume1_price}\n\
2.{drink1_volume2}: {drink1_volume2_price}\n\
3.Exit')        
        user_choose = input('Input menu item index: ')
        
        if user_choose == '1':
            print(f'{drink1_name} {drink1_volume1} {drink1_volume1_price}')
        elif user_choose == '2':
            print(f'{drink1_name} {drink1_volume2} {drink1_volume2_price}')
        elif user_choose == '3':
            break
        else:
            print('Error menu item!')        
    elif user_choose == '2':
        print(f'You choose {drink2_name}:\n\
1.{drink2_volume1}: {drink2_volume1_price}\n\
2.Exit')     
        if user_choose == '1':
            print(f'{drink2_name} {drink2_volume1} {drink2_volume1_price}')
        elif user_choose == '2':
            break
        else:
            print('Error menu item!')
    elif user_choose == '3':
        break
    else:
        print('Error menu item!')