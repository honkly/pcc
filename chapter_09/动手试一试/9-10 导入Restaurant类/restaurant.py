class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def describe_restaurant(self):
        print(self.name + ":" + self.type)

    def open_restaurant(self):
        print("Restaurant is OPEN!")