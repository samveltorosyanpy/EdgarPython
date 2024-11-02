# import time
# class Door():
#     def __init__(self, color):
#         self.color = color
#
#     def open(self):
#         print(f"open {self.color}")
#         time.sleep(1)
#         self.close()
#
#     def close(self):
#         print(f"close {self.color}")
#
#
#
# class Window(Door):
#     def __init__(self, color, glace_color):
#         super().__init__(color)
#
#         self.glace_color = glace_color
#
#     def openW(self):
#         print(f"smol opening {self.color}")
#         time.sleep(1)
#         self.close()
#
#
#
#
#
# door1 = Door("Red")
# window1 = Window("Blue", "black")
#
# window1.openW()
# door1.open()
# window1.close()

from datetime import datetime
import time
class Person:
    def __init__(self, ident, user_name, user_status):
        self.id = ident
        self.user_name = user_name
        self.user_status = user_status
        self.create_at = datetime.now()

    def create_order(self):
        print("order creating ...")


class Admin(Person):
    def __init__(self, ident, user_name, user_status):
        super().__init__(ident, user_name, user_status)

    def product_add(self, product_name, product_price):
        print(f"created product: {product_name} - {product_price}")


class Manager(Person):
    def __init__(self, ident, user_name, user_status):
        super().__init__(ident, user_name, user_status)

    def edit_post_price(self, product_price):
        print(f"edited product price: {product_price}")



person1 = Person(1, "Sam", "USER")
person1.create_order()

admin1 = Admin(2, "Edgar", "ADMIN")
admin1.product_add("New car", 5000)
admin1.create_order()

manager1 = Manager(3, "Syuzi", "Mangaer")
manager1.create_order()
manager1.edit_post_price(2000)





