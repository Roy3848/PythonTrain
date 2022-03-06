class Car:

    # class attribute
    Country = "Germany"

    # instance attribute
    def __init__(self, brand_name, model, color, price):
        self.brand_name = brand_name
        self.model = model
        self.color = color
        self.price = price

    # methods (instance methods, means the behaviors of the instances)
    # self should be used by convention in the instance methods with the instance attributes.
    # Because the instance methods are applicable for all the instances present, not any specific.
    # so it is better to use self so that the action in the method will be applied to all the instances
    # but if we put any specific instance name then the action will be applied to only that instance.
    def car_full_name_(self):
        return "{} {} is the full name of the car.".format(self.brand_name, self.model)

    def fast(self):
        return "{} is very fast car and can be used for racing.".format(self.brand_name)


# these are the objects/ instances of the class.
Car1 = Car("Mercedes", "S Class", "White", "$75000")
Car2 = Car("Volkswagen", "Vento", "Grey", "$65000")

# access the class attribute
# instance accessing the class attribute
print("Mercedes is a {} based car.".format(Car1.Country))
print("Volkswagen is a {} based car.".format(Car2.Country))

# access the instance attribute
print("{} is car of {} brand".format(Car1.model, Car1.brand_name))
print("{} is car of {} brand".format(Car2.model, Car2.brand_name))

# access the instance methods
print(Car1.car_full_name_())
print(Car2.car_full_name_())

print(Car.__dir__(Car2))