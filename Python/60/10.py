# 10. Error Handling
# Write a program that takes a number as input and divides 100 by that number. Handle the case where the input is zero, and print an error message instead.


try:
  number = float(input("Enter your number: "))
  result = 100 / number
  print(result)

except ZeroDivisionError:
  print("Error: not can 0")

except ValueError:
  print("Error: Invalied Number")