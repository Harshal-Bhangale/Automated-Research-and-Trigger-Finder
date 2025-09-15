# Python String Method 
'''
 Python string methods is a collection of in-built Python functions that operates on lists.
 Note: Every string method in Python does not change the original string instead returns a new string with the changed attributes. 

    1. lower()
    2. upper()
    3. title()
    4. swapcase()
    5. capitalize()
'''

str_UpperCase = "HARSHAL BHANGALE"
str_LowerCase = "harshal bhangale"
str_MixCase = "Harshal Bhangale"

print("Original String :-",str_UpperCase)
print("Lower Case :-",str_UpperCase.lower())
print("Upper Case :-",str_LowerCase.upper())
print("Title Case :-",str_UpperCase.title())
print("Swap Case :-",str_MixCase.swapcase())
print("Capitalize Case :-",str_LowerCase.capitalize())

# casefold() :- Convert string to lowercase.
# casefold() is similar to lower() but it is stronger. It converts all characters to lowercase
# str = "HarsHal BhanGale"
# print("casefold() :-",str.casefold())
# # Difference between casefold() and lower() 
# string = "ß" 
# print("Using lower():", string.lower())
# print("Using casefold():", string.casefold())

# String center() method creates and returns a new string that is padded with the specified character.
# str = "Harshal"
# print(str.center(50,'*'))

# count() function returns the number of occurrences of a substring within a String.
# str = "Harshal"
# print("h is Harshal :-", str.count('h'))

