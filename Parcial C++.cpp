#include <iostream>

using namespace std;

int main() {
    int a, b, c;

    cout << "Ingrese los tres lados del triángulo: ";
    cin >> a >> b >> c;

    // Verifico si los lados siguen la regla de formar un triangulo
    if (a + b > c && a + c > b && b + c > a) {
        // Determino el tipo de triángulo
        if (a == b && b == c) {
            cout << "Equilátero" << endl;
        } else if (a == b || a == c || b == c) {
            cout << "Isósceles" << endl;
        } else {
            cout << "Escaleno" << endl;
        }
    } else {
        cout << "No es un triángulo" << endl;
    }

    return 0;
}
