import os, json


class UserClass:
    def __init__(self):
        self.path = os.getcwd() + "/db/users.json"
        self.cars = os.getcwd() + "/db/cars.json"
        with open(self.path, 'r') as file:
            text = file.read()
            self.data = json.loads(text)
        with open(self.cars, 'r') as file:
            cars_text = file.read()
            self.cars = json.loads(cars_text)

    def get_user_logins(self):
        logins = []
        for user in self.data['users']:
            logins.append(user['login'])
        return logins

    def update(self):
        new_data = json.dumps(self.data)

        with open(self.path, 'w') as fail:
            fail.write(new_data)

    def get_user_by_id(self, user_id):
        for user in self.data['users']:
            if user['id'] == user_id:
                return user
        return False

    def get_user_by_login(self, user_login):
        for user in self.data['users']:
            if user['login'] == user_login:
                return user
        return False

    def get_user_password_by_login(self, login):
        for user in self.data['users']:
            if user['login'] == login:
                return user['password']

    def create_now_user(self, login, password, phone, user_date):
        new_id = self.data["users"][-1]['id'] + 1
        self.data['users'].append(
            {"id": new_id, "login": login, "password": password, "phone": phone, "date": user_date})
        self.update()

    def update_user_data(self, user_id, **kwargs):
        user = self.get_user_by_id(user_id=user_id)
        for kw in kwargs:
            if kw in list(user.keys()):
                user[kw] = kwargs[kw]
        self.update()

    def cars_update(self):
        new_cars = json.dumps(self.cars)
        with open(self.cars, 'w') as file:
            file.write(new_cars)

    def get_cars_login(self):
        logins = []
        for x in self.cars['cars']:
            logins.append(x['login'])
        return logins

    def creator_new_cars(self, create_at,name,model,description):
        new_cars_id = self.cars['cars'][-1]['id'] + 1
        self.cars['cars'].append({"id" : new_cars_id, "create_at" : create_at, "name" : name, "model" : model, "description" : description})
    cars_update()

    def get_cars_by_id(self, cars_id):
        for car in self.cars['cars']:
            if car['id'] == cars_id:
                return car
        return False

    def get_cars_by_name(self, name):
        for car in self.cars['cars']:
            if car['name'] == name:
                return car
        return False

    def get_model_by_create_at(self, create_at):
        for car in self.cars['cars']:
            if car['create_at'] == create_at:
                return car['model']
        return False

    def update_cars_data(self,cars_id, **kwargs):
        cars = self.get_cars_by_id(cars_id=cars_id)
        for kw in kwargs:
            if kw in list(cars.keys()):
                cars[kw] = kwargs[kw]
        self.cars_update()






# user = UserClass()
# print(user.get_user_password_by_login("AAAAAA"))
# print(user.get_user_logins())
# user.update_user_data(user_id=2, password='Torosyan')
# user.create_now_user(login="Samvel001", password="Admin001", phone="99999999", user_date="2000-08-26")
# print(user.get_user_by_id(user_id=2))