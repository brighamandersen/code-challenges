#include <iostream>
#include <string>

void printItems(int array[], int numItems) {
    for (int i = 0; i < numItems; i++) {
            if (i > 0) {
                std::cout << ", ";
            }
            std::cout << array[i];
        }
    std::cout << "\n";
}

void sort(int *array, int numItems) {
    int temp;
    bool didSwap = false;

    do {
        didSwap = false;
        for (int i = 0; i <= (numItems - 2); i++) {
            if (array[i] > array[i + 1]) {
                didSwap = true;
                temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
            }
        }
    } while (didSwap);
}

int main() {
    int numItems = 10;
    int A[numItems] = {5, 8, 2, 29, 4, 7, 1, 1321, 46, 6};
    int *ptr = A;

    // Print items before sort
    printItems(A, numItems);

    // Swap elements (bubble sort)
    sort(ptr, numItems);

    // Print items after sort
    printItems(A, numItems);

    return 0;
}
