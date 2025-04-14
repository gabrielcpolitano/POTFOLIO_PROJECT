// 10. Error Handling
// Write a program that takes a number as input and divides 100 by that number. Handle the case where the input is zero, and print an error message instead.

number = parseInt(prompt("Writing a number: "))

if (number === 0){
    console.log("Error The Number NOT To Be 0")
    
} else if(typeof number === "number" && !isNaN(number)) {
    console.log(100 / number)

} else {
    console.log("Error The Number is Not Avaible")
}