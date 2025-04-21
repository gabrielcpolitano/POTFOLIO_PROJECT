// 7. String Manipulation
// Write a program that takes a user's input string and:
// - Converts it to uppercase.
// - Reverses the string.
// - Counts the number of characters in it.

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  string userName;

  cout << "Enter a string: ";
  getline(cin, userName); // Reads the entire line include the spaces

  // Convert to uppercase
  string uppercaseString = userName;
  
  transform(uppercaseString.begin(), uppercaseString.end(), uppercaseString.begin(), ::toupper); // transform(begin, end, saved, function)
  cout << uppercaseString << endl;

  // Reverse the string
  string reversedString = userName;
  reserse


  return 0;
}