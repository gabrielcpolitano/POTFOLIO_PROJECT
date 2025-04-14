#include <iostream>
using namespace std;

int main() {
    double num1, num2;

    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;

    double addition = num1 + num2;
    double subtraction = num1 - num2;
    double multiplication = num1 * num2;
    double division;

    if (num2 != 0) {
        division = num1 / num2;
    } else {
        cout << "Division by zero is not allowed." << endl;
    }

    cout << addition << endl;
    cout << subtraction << endl;
    cout << multiplication << endl;

    if (num2 != 0) {
        cout << division << endl;
    }

    return 0;
}