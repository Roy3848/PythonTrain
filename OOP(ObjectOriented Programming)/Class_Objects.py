# creating a class is the blueprint for creating objects.
# Class is to create the real world datatype.

# Object has their own attributes and methods.
# brand_name, model, color, price are all the attributes of the objects.
# and here we have not mentioned any methods. method means functions in the body of the class.
# we can use self with the methods by convention.

class Car:

    # class attribute
    Country = "Germany"

    # instance attribute
    def __init__(self, brand_name, model, color, price):
        self.brand_name = brand_name
        self.model = model
        self.color = color
        self.price = price


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

