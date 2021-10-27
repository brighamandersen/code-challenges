#include <iostream>
#include <string>

int main() {
    int numElements = 10;
    int A[numElements] = {5, 8, 2, 29, 4, 7, 1, 1321, 46, 6};
    int temp;
    bool didSwap = false;

    for (int i = 0; i < numElements; i++) {
        if (i > 0) {
            std::cout << ", ";
        }
        std::cout << A[i];
    }
    std::cout << "\n";

    do {
        didSwap = false;
        for (int i = 0; i <= (numElements - 2); i++) {
            if (A[i] > A[i + 1]) {
                didSwap = true;
                temp = A[i];
                A[i] = A[i + 1];
                A[i + 1] = temp;
            }
        }
    } while (didSwap);

    for (int i = 0; i < numElements; i++) {
        if (i > 0) {
            std::cout << ", ";
        }
        std::cout << A[i];
    }
    std::cout << "\n";

    return 0;
}
