# 4. If Statements
# Write a program that checks whether a given number is even or odd using an  statement.

num = int(input("Write a number: "))

if num % 2 == 0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")