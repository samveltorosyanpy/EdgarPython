def creator_login(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*()+{}[]:;<>?/':
                print('logini mech chi tuylatrvum ogtagorcel nshaner')
                msg = input('porceq krkin: - ')
                stop = False

        if len(msg) < 6 < 15:
            print('logini mech petq e lini 6ic mec ev 15ic poqr text')
            msg = input('krkin porceq: - ')
            stop = False

        if stop is True:
            return True
        else:
            stop = True

def creator_phone(msg):
    stop = True
    while True:
            for x in msg:
                if x not in '0123456789':
                    print('ogtagorceq miayn tver')
                    msg = input('krkin porceq: - ')
                    stop = False

            if len(msg) < 7:
                print('heraxosahamary petq e unena 8nish ')
                msg = input('krkin porcel: (+374) - ')
                stop = False

            if stop is True:
                return True
            else:
                stop = True

def creator_parol(msg1):
    stop = False
    while True:
        for x in msg1:
            if x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                print('good')
                return False
            stop = False

        print('greq nvazaguyny mek mecatar')
        msg1 = input('krkin porceq: - ')

        for y in msg1:
            if y in '0123456789+-_':
                print('good')
                return True
            stop = False


            print('ogtagorceq nvazaguyny mek nish (+-_)')
            msg1 = input('krkin porceq: - ')



