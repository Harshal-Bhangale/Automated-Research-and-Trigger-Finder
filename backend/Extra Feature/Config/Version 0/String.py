String1 = "Haxshal Bhangale"

print("Initial String",String1)

# Python String Positive Indexing
print("First Character of String is:",String1[8])  

#  Python String Negative Indexing
print("First Character of String is:",String1[-11])

print(String1[9:16])

print(String1[::-1])

# String1 = "Harsh Bhangale"
# print(String1)

# list1 = list(String1)
# list1[2] = "r"
# String2 = ''.join(list1)
# print(String2)
# OR
# String3 = String1[0:2] + 'r' + String1[3:]
# print(String3)  


# Deleting a character
# Python strings are immutable, that means we cannot delete a character from it. When we try to delete the character using the del keyword, it will generate an error.
# del String1[6]
# print(String1)

# String2 = String1[0:2] + String1[3:]
# print(String2)

# del String2
# print(String2)

#  Default Order
Str1 = "{} {} {}".format('Harsh','Ritesh','Ritvij')
print(Str1)

# Positional Formatting
Str2 = "{1} {0}".format('Harsh','Bhangale')
print(Str2)

# Keyword Formatting
Str3 = "{B} {H}".format(H='Harshal',B='Bhangale')
print(Str3)

arr = [12,3,15,4]
print("Sum:-",sub(arr))

