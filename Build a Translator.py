# topic includes functions, for loop, string methods, etc.
# also return keyword in function, also input function.
# mostly a function return the value that we ask the function to give us.
# return keyword works like we ask for something to do, it gives us what we ask for.

def translate(sentence):
    translation = ""  # to get the fina; result
    for letter in sentence:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a sentence: ")))


