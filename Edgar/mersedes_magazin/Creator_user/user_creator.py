import os,json

class UserMost:
    def __init__(self):
        self.path = os.getcwd() + r"\Creator_user\users.json"
        with open(self.path, 'r') as file:
            text = file.read()
            self.data = json.loads(text)

    def update(self):
        new_data = json.dumps(self.data, indent=4)
        with open(self.path, 'w') as file:
            file.write(new_data)

    def users_add(self,login,phone,password):
            new_id = self.data["users"][-1]['id'] + 1
            self.data['users'].append({'id' : new_id, 'login' : login, 'phone' : phone, 'password' : password})
            self.update()

    def Creator_user_phone(self):
        phones = []
        for x in self.data["users"]:
            phones.append(x['phone'])
        return phones

    def Creator_user_password(self):
        passwords = []
        for x in self.data["users"]:
            passwords.append(x["password"])
        return passwords




