try:
  num = float(input("Enter a number to divide 100 by: "))
  result = 100 / num
  print("Result:", result)
except ZeroDivisionError:
  print("Error: Cannot divide by zero.")
except ValueError:
  print("Error: Please enter a valid number.")