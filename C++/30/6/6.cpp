// 6. Functions
// Define a function that takes two numbers as arguments and returns their sum. Test the function by calling it with different inputs.

#include <iostream>
using namespace std;

int addNumbers(int num1, int num2) {
  return num1 + num2;
}

int main() {
  cout << addNumbers(1, 10) << endl;
  cout << addNumbers(1, 20) << endl;
  cout << addNumbers(1, 30) << endl;
  cout << addNumbers(1, 40) << endl;

  return 0;
}