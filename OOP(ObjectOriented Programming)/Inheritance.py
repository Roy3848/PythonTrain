class Car:

    # class attribute
    Country = "Germany"

    # instance attribute
    def __init__(self, brand_name, model, color, price):
        self.brand_name = brand_name
        self.model = model
        self.color = color
        self.price = price

    def car_full_name_(self):
        return "{} {} is the full name of the car.".format(self.brand_name, self.model)

    def fast(self):
        return "{} is very fast car and can be used for racing.".format(self.brand_name)

# Inheritance
# a child class is created named Wheel4
# which inherits the functionality from the parent class Car


class TruckContainer(Car):

    def __init__(self, brand_name, model, color, price, starting_point):
        super().__init__(brand_name, model, color, price)
        # super() function is used to inherit the functionality of the parent class.
        self.starting_point = starting_point


# these are the instances of the child class.
Truck1 = TruckContainer("Ford", "F150", "Black", "$55000", "Kolkata")
Truck2 = TruckContainer("Ford", "F150", "Black", "$55000", "Kolkata")
