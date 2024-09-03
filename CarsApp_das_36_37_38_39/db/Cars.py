import os,json

class Cars:
    def __init__(self):
        self.cars = os.getcwd() + "/db/cars.json"
        with open(self.cars, 'r') as file:
            cars_text = file.read()
            self.cars = json.loads(cars_text)

    def cars_update(self):
        new_cars = json.dumps(self.cars)
        with open(self.cars, 'w') as file:
            file.write(new_cars)

    def creator_new_cars(self, create_at,name,model,description):
        new_cars_id = self.cars['cars'][-1]['id'] + 1
        self.cars['cars'].append({"id" : new_cars_id, "create_at" : create_at, "name" : name, "model" : model, "description" : description})


    def get_cars_by_id(self, cars_id):
        for car in self.cars['cars']:
            if car['id'] == cars_id:
                return car
        return False

    def get_cars_by_name(self, name):
        for car in self.cars['cars']:
            if car['name'] == name:
                return (f" Car creat_at: -> {car['create_at']} \n Car name: -> {car['name']} \n Car model: -> {car['model']} \n Car description: -> {car['description']}")

    def get_model_by_create_at(self,create_at):
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
