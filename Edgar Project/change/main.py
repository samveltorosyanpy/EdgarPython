from Admin_panel.AllName import x_men,x_woumen
from grancum.grancman_hamakarg import info_name_panel

def starting_program():
    print('Bari Glust Piple kayq')
    print('Arach gnalu hamar grir qo sery')
    print('-> txa')
    print('-> axchik')
    user_check = input('dzer sery: --> ')
    while True:
        if user_check == 'txa':
            print(f'Bari galust {x_men}-i xumb:')
            print('\n')
            print('Kayqum grancvelu hamar petq e lracneq hetevyal vandaknery:')
            break
        elif user_check == 'axchik':
            print(f'Bari galust {x_woumen}-i xumb')
            print('\n')
            print('Kayqum grancvelu hamar petq e lracneq hetevyal vandaknery:')
            break
        else:
            print('duq uneq sxal porceq krkin')
            user_check = input('dzer sery: --> ')

def starting_info_panel():
    user_check2 = input('name: --> ')
    info_name_panel(message=user_check2)


if __name__ == '__main__':
    starting_program()
    starting_info_panel()


