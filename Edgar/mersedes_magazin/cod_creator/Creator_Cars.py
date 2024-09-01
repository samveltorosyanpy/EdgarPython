def Car_name_creator(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*()_+[]{}<>?/':
                print('ogtagorceq miayn tar ev tiv')
                msg = input('krkin porceq: - ')
                stop = False

        if stop is True:
            return True
        else:
            stop = True

def Car_date_creator(msg):
    stop = True
    while True:
        if stop is True:
            for x in msg:
                if x not in '0123456789':
                    print('ogtagorceq miayn tiv')
                    msg = input('krkin porceq: - ')
                    stop = False

        if stop is True:
            return True
        else:
            stop = True

def Car_info_creator(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*(){[}]<>?/':
                print('ogtagorceq miayn tver ev tarer')
                msg = input('Krkin porceq: - ')
                stop = False

        if stop is True:
            return True
        else:
            stop = True

def Car_price_creator(msg):
    stop = True
    while True:
        for x in msg:
            if x in '0123456789$':
                return True
            else:
                print('ogtagorceq miayn tiv ev gnayin arjeq')
                msg = input('krkin porceq: - ')
                stop = False

        if stop is True:
            return True
        else:
            stop = True




















