# 7. String Manipulation
# Write a program that takes a user's input string and:
# - Converts it to uppercase.
# - Reverses the string.
# - Counts the number of characters in it.

userName = input("What's your name: ")

uppercase = userName.upper()
reverse = userName[::-1]
count = len(userName)

print(userName)
print(reverse)
print(count)