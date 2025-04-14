# 9. Simple Dictionary
# Create a dictionary with keys as names of people and values as their ages. Write a program to:
# - Print all the keys and values.
# - Add a new person to the dictionary.
# - Update the age of an existing person.

family = {"gabriel": 21, "matheus": 24, "joao miguel": 9}

print(family.keys())
print(family.values())
family["mae"] = 45
print(family)
family["gabriel"] = 22
print(family)

