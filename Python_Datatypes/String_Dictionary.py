company = 'Roy Mindbowser and Co.'
# text can be between single or double quotation
print(company[3:7])
# Negative Indexing
print(company[-9: -5])


# Format strings
name = "Roy"
Enterprise = "Roy Enterprise"

sentence = "{} is the founder of {}".format(name, Enterprise)
print(sentence)

# input string
name1 = input("Please write your name: ")
Enterprise1 = input("Which is your company: ")

# format the string as per the input by the user
print("{} is an employee of {}.".format(name1, Enterprise1))

# Escape character
"We are so called \"vikings\" from the north."


# DICTIONARY
# dictionary's is an ordered and changeable key value pairs
# which do not accept any duplicate members

car_model = {
    "Brand": "Mercede-Benz",
    "Color": "Black",
    "Country": "Germany"
}


# change items in dictionary
car_model["Color"] = "Blue"
# add items in the dictionary
car_model.update({"Owner": "Sayak Roy"})
print(car_model)
