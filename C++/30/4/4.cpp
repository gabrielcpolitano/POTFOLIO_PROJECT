// 4. If Statements
// Write a program that checks whether a given number is even or odd using an statement.

#include <iostream>
using namespace std;

int main() {
  int number;

  cout << "Enter a number: ";
  cin >> number;

  if (number % 2 == 0) {
    cout << number << " is even" << endl;
  } else {
    cout << number << " is odd" << endl;
  }

  return 0;

  
}