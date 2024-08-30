def Car_name_creator(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*()_+[]{}<>?/':
                print('ogtagorceq miayn tar ev tiv')
                msg = input('krkin porceq: - ')
                stop = False
        break

def Car_date_creator(msg):
    stop = True
    while True:
        for x in msg:
            if x in '0123456789':
                return True
            else:
                print('ogtagorceq miayn tiv')
                msg = input('krkin porceq: - ')
                stop = False

















