# 8. Lists and Indexing
# Create a list of five items (e.g., fruits or numbers). Write code to:
# - Access and print the first and last items.
# - Add a new item to the list.
# - Remove an item from the list.


fruit = ["orange", "apple", "banana"]

first_fruit = fruit[0]
print(first_fruit)

last_fruit = fruit[-1]
print(last_fruit)

fruit.append("chocolate")
print(fruit)

fruit.remove("chocolate")
print(fruit)