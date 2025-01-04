#include <iostream>
using namespace std;

int main() {
    // Step 1: Print the first line
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    // Step 2: Print the middle lines
    for (int i = 4; i >= 2; i--) {
        // Print leading spaces
        for (int j = 0;j< 2*(i-1); j++) {
            cout << " ";
        }
        // Print the number
        cout << i << endl;
    }

    // Step 3: Print the last line
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
