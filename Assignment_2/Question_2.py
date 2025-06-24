# Input two strings
str1 = input("\nEnter first string: ")
str2 = input("Enter second string: ")

# Concatenate
combined = str1 + str2

# Apply various string methods
print("\n----- String Methods -----")
print("Lowercase    :", combined.lower())
print("Uppercase    :", combined.upper())
print("Title Case   :", combined.title())
print("Swap Case    :", combined.swapcase())
print("Capitalized  :", combined.capitalize())
print("Casefold     :", combined.casefold())
print("Centered     :", combined.center(30, '-'))
print("Count of 'a' :", combined.count('a'))
print("Ends with ?  :", combined.endswith("?"))
print("Find 'is'    :", combined.find("is"))
print("Isalnum     :", combined.isalnum())
print("Is Digit     :", combined.isdigit())
print("Is Numeric   :", combined.isnumeric())
print("Is Space     :", combined.isspace())
print("Replaced 'a' with '@':", combined.replace('a', '@'))