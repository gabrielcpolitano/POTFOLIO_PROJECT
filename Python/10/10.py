# 10. Error Handling
# Write a program that takes a number as input and divides 100 by that number. Handle the case where the input is zero, and print an error message instead.

try:
  number = int(input("Divisor Number: "))
  result = 100/number
  print(result)
except ZeroDivisionError:
  print("This is Zero Division its not can!!")
except ValueError:
  print("This is not avalable divisor!!")