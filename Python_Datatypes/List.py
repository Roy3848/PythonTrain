fruits = ["apple", "BlackBerry", "Carrot", "Cucumber"]
print(fruits)  # to print the list

fruits.append("Orange")  # To add an item at the end of the list
fruits.insert(1, "Watermelon")  # to add an item at the specific position in the list

# extend function to add items of another list to the first
company = ["Google", "Micrososft", "Amazon"]
fruits.extend(company)

# to remove the value
fruits.remove("apple")
# pop items
fruits.pop(1)  # to remove the items in the list with index number.
# delete the item in the list - del keyword
del fruits[0]
print(fruits)
# this clear() method empties the complete list
company.clear()
print(company)


# LIST COMPREHENSION
# shorter syntax to find a new list from the existing list.
# to find out whether even or not
numbers = [1, 2, 3, 4, 5, 6, 7, 11, 16, 50]
even = [i for i in numbers if i%2==0]
print(even)

fruits1 = ["apple", "blackberry", 'watermelon', "banana", "cherry", "banana"]
change = [x if x != "banana" else "Orange" for x in fruits1]
print(change)

#sort
# basically sort in the alphanumerically
# for text in the alphabetic order and for numbers in ascending order of numerics.
numbers2 = [8, 7, 190, 25, 1, 8]
numbers2.sort()
print(numbers2)
# to order in descending order
numbers2.sort(reverse=True)
print(numbers2)

#  customize the sort function
list = [100, 50, 62, 83, 23]

def my_func(n):
    return abs(n-50)

list.sort(key=my_func)  # calling the function
print(list)  # printing the final result



