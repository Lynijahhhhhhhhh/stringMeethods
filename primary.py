# author: Lynijah
# date:07-14-2021

# --------------- Section 1 --------------- #

# 1 | String Methods
#
# 1 - Save your name to a variable named name.
#   a. Center that variable within 30 characters. Print it.
#   b. Print the variable in all upper case.
#   c. Print the variable in all lower case.
#   d. Print the variable capitalized (Look to documentation.)
print("Name Section")

name="Lynijah"
print(name.center(30))
print(name.upper())
print(name.lower())
print(name.capitalize())


print(" ")

# 2 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first instance of the letter a. Print that position.
#   b. Find the first instance of the letter b. Print that position.
#   c. Find the first instance of a word of your choice. Print that position.
print("Sentences")
text= input("Create a Sentence: ")
print(text.find("a"), "is the index of the letter a ")
print(text.find("b"),"is the index of the letter b")
print(text.find("mom"),"is the index of the word  mom")
print(" ")

# 3 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the position of every vowel in text. Save them each to a variable.
#   b. Using a built-in function, print the position of the vowel that shows up last.
#   c. Using a built-in function, print the position of the vowel that shows up first.
print("String Modules")

text= input("Create a sentence: ")
print(text.find("a"),"is the index of vowel a")
print(text.find("e"),"is the index of vowel e")
print(text.find("i"),"is the index of vowel i")
print(text.find("o"),"is the index of vowel o")
print(text.find("u"),"is the index of vowel u")
# print(text[0],"is the first letter")
# print(text[-1],"is the last letter")


# 4 | String Indexing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the 0th letter of the text using string indexing.
#   b. Print the 1st, 2nd, and 3rd letters of the text using string indexing.
#   c. Print the last letter of the text using string indexing.
#       HINT: There are multiple ways of doing this. Is there a function that we can use that will find
#           the position of the last letter, or atleast one off from it?
print(" ")
print(" String indexing")

text=input("Create a sentence: ")
print(text[0],"is the first character")
print(text[0:4],"is the first 4 character")
print(text[-1],"is the last character")


# 5 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Slice text from the 2nd position to the 5th. Print that.
#   b. Slice text from the 0th position to the 8th. Print that.
#   c. Slice text from 3rd position to end. Print that.
#   d. Slice text from the beginning to 5 positions before the last character. Print that.
#       HINT: Use a function to get the last position of the string.
print(" ")
print("String Slicing")

text=input("Create a Sentence Please: ")
print(text[2:5],"are letters in index 2-5")
print(text[0:8],"are letters in index 0-8")
print(text[3:],"are letters in index 3 to end")
print(text[0:len(text)-5],"are letters in index 0 to 5 before end")

# 6 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the text, but only every 2nd character.
#   b. Print the text, but only every 3rd character.
#   c. Print the text, but in reverse order.

print(" ")
print("String Slicing 2")

text= input("Create a sentence: ")
print(text[::2],"are the every other characters of the string given")
print(text[::3],"are the every third characters of the string given")
print(text[::-1],"is the reverse to the string given")