from db.User import UserClass
from validators.register_vals import val_date, val_login, val_password, val_phone

def login():
    login = input("greq dzer login")
    while True:
        if login in UserClass().get_user_logins():
            print('good')
            break
        else:
            login = input("ayd anunov user goyutyun chuni porceq krkin")

    password = input("greq dzer parol@")
    while True:
        if password == UserClass().get_user_password_by_login(login):
            print('good')
            break
        else:
            password = input("paroly hamapatasxan chi greq krkin")


def register():
    phone = input("greq heraxosahamary")
    val_phone(phone)
    login = input("stexceq login")
    val_login(login)
    user_date = input("greq dzer cnndyan amis amsativ@ (YYYY-MM-DD): -  ")

    if val_date(msg=user_date):
        password1 = input("stexceq parol")
        password2 = input("krkneq nor paroly")

        if val_password(password1, password2) is True:
            UserClass().create_now_user(login=login, password=password2, phone=phone, user_date=user_date)
    else:
        return


def start():
    print("""grancvel kam mutq linel
1) login
2) grancvel
    """)
    while True:
        c = input("yntreq: ")
        if c == "1":
            login()
            break
        elif c == '2':
            register()
            break
        else:
            print("chka nman hraman skseq noric")



if __name__ == "__main__":
    start()



# x[0] = 6
#
# print(id(x))




# 4377553200