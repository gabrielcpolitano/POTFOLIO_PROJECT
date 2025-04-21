// 5. Loops
// Create a loop that prints the numbers from 1 to 10, using both a loop and a loop.

#include <iostream>
using namespace std;

int main() {
  for (int i = 1; i <= 10; i++) {
    cout << i << endl;
  }

  int counter = 1;
  while (counter <= 10) {
    cout << counter << endl;
    counter++;
  }

  return 0;
}