from cod_creator.registration import creator_login,creator_phone,creator_parol
from Creator_user.user_creator import UserMost
from cod_creator.Creator_Cars import Car_name_creator,Car_date_creator

def grancum():
    print('voxchuyn sireli ogtater: \n')
    print('kayqum grancvelu hamar yntreq grancum hramany:')
    print('1.grancum')
    print('2.mutq ej \n')

def command():
    command = int(input('yntreq tarberaky: - '))

    while True:
        if command == 1:
            login = input('Login: - ')
            creator_login(msg=login)

            phone = input('Phone: (+374) - ')
            creator_phone(msg=phone)

            password = input('Password: - ')
            creator_parol(msg1=password)
            UserMost().users_add(login=login,phone=phone,password=password)
            break

        elif command == 2:
            print('arach gnalu hamar mutqagreq dzer phone ev passwordy')
            phone = input('Phone: (+374) - ')
            while True:
                if phone in UserMost().Creator_user_phone():
                    print('good')
                    break
                else:
                    print('nman hamarov grancvac ogtater goyutyun chuni')
                    phone = input('krkin porceq: (+374) - ')

            password = input('password: - ')
            while True:
                if password in UserMost().Creator_user_password():
                    print('good')
                    print('bari galust Mersedes salon')
                    break
                else:
                    print('nman password goyutyun chuni bazayum')
                    password = input('krkin porceq: - ')
            break
        else:
            print('nman hraman goyutyun chuni')
            command = int(input('krkin porceq: - '))

def cars_magazin():
    print('1. nayel meqenaner')
    print('2. avelacnel meqena')
    print('3. gnel meqena')
    print('4. Het gnal menu')

def command_cars():
    command = int(input('yntreq tarberaky: - '))
    while True:
        if command == 1:

            car_name = input('Car name: - ')
            Car_name_creator(msg=car_name)

            car_date = input('Car date: - ')
            Car_date_creator(msg=car_date)



if __name__ == '__main__':
    grancum()
    command()
    cars_magazin()
    command_cars()
