#include <iostream>
using namespace std;

int main() {
    int num, a = 0, b = 1, c = 0;
    bool pertence = false;

    cout << "Informe um numero inteiro positivo: ";
    cin >> num;

    while (c < num) {
        c = a + b;
        a = b;
        b = c;
    }

    if (c == num) {
        pertence = true;
    }

    if (pertence) {
        cout << num << " pertence a sequencia de Fibonacci." << endl;
    } else {
        cout << num << " nao pertence a sequencia de Fibonacci." << endl;
    }

    return 0;
}
