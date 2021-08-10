#include <iostream>
#include <string>
using namespace std;

// Global variables
const int BOARD_DIMENSION = 3;  // Number of squares wide and tall
string board[BOARD_DIMENSION][BOARD_DIMENSION]; 
const string X = "X";
const string O = "O";

bool isTaken(string square) {
    if (square == X || square == O) return true;
    return false;
}

void printBoard() {
    cout << endl;
    for (int i = 0; i < BOARD_DIMENSION; i++) {
        for (int j = 0; j < BOARD_DIMENSION; j++) {
            if (j == 0) cout << " | ";

            if (!isTaken(board[i][j])) cout << " ";
            cout << board[i][j] + " | ";
        }
        cout << endl;
    }
    cout << endl;
}

bool performTurn(bool xTurn, int row, int col) {
    if (row < 1 || row > BOARD_DIMENSION || col < 1 || col > BOARD_DIMENSION) {
        cout << "Invalid input.  Keep input between 1 and " + to_string(BOARD_DIMENSION) + "." << endl << endl;
        return false;
    }
    
    if (isTaken(board[row - 1][col - 1])) {
        cout << "Spot already taken." << endl << endl;
        return false;
    }

    if (xTurn) {
        board[row - 1][col - 1] = X;
    } else {
        board[row - 1][col - 1] = O;
    }
    return true;
}

bool checkCombination(string spot1, string spot2, string spot3) {
    if (!isTaken(spot1) || !isTaken(spot2) || !isTaken(spot3)) return false;
    if (spot1 == spot2 && spot2 == spot3) return true;
    return false;
}

bool someoneWon() {
    // Top left -> bottom right diagonal
    if (checkCombination(board[0][0], board[1][1], board[2][2])) return true;

    // Bottom left => top right diagonal
    if (checkCombination(board[2][0], board[1][1], board[0][2])) return true;

    // Top row
    if (checkCombination(board[0][0], board[0][1], board[0][2])) return true;

    // Middle row
    if (checkCombination(board[1][0], board[1][1], board[1][2])) return true;

    // Bottom row
    if (checkCombination(board[2][0], board[2][1], board[2][2])) return true;

    // Top col
    if (checkCombination(board[0][0], board[1][0], board[2][0])) return true;

    // Middle col
    if (checkCombination(board[0][1], board[1][1], board[2][1])) return true;

    // Right col
    if (checkCombination(board[0][2], board[1][2], board[2][2])) return true;

    return false;
}

string getTurnTeam(bool xTurn) {
    if (xTurn) {
        return X;
    }
    return O; 
}

int main() {
    bool xTurn = true;

    cout << "Welcome to C++ Tic Tac Toe!" << endl;

    printBoard();

    int row = 0;
    int col = 0;

    bool gameOver = false;
    while (!gameOver) {
        cout << "It's " + getTurnTeam(xTurn) + "'s turn!" << endl;

        bool validInput = false;
        while (!validInput) {
            cout << "Enter a row #: ";
            cin >> row;

            cout << "Enter a column #: ";
            cin >> col;

            if (!performTurn(xTurn, row, col)) continue;
            
            validInput = true;
        }
        
        printBoard();


        if (someoneWon()) {
            gameOver = true;
            break;
        }
        xTurn = !xTurn;
    }

    cout << "Game over! " << getTurnTeam(xTurn) << "'s won." << endl;

    return 0;  
}


