// 8. Lists and Indexing
// Create a list of five items (e.g., fruits or numbers). Write code to:
// - Access and print the first and last items.
// - Add a new item to the list.
// - Remove an item from the list.


fruit = ["apple", "banana", "chocolate"]

console.log(fruit[0])
console.log(fruit[fruit.length - 1])

fruit.push("cherry")
console.log(fruit)

fruit.splice(2, 1)
console.log(fruit)