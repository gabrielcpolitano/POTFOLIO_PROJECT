// 7. String Manipulation
// Write a program that takes a user's input string and:
// - Converts it to uppercase.
// - Reverses the string.
// - Counts the number of characters in it.


let userName = prompt("Writing your name: ")

userName = userName.toUpperCase()
console.log(userName)

userName = userName.split("").reverse().join("")
console.log(userName)

userName = userName.length
console.log(userName)
