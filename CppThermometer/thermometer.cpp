// Compile and run in one line using 'g++ thermometer.cpp && ./a.exe'

#include <iostream>
#include <string>

const int MIN_TEMP = 30.0f;
const int MAX_TEMP = 100.0f;
const int DEFAULT_TEMP = 76.0f;

char getCharFromInput(std::istream&);
float getNumberFromInput(std::istream&);
void printThermostat(const float&, std::ostream&);

int main() {
    std::string currentFile = "";
    std::string outputFileName = "";
    std::string inputFile = "";
    std::string outputFile = "";
    std::string command = "";
    float currentTemp = DEFAULT_TEMP;
    float tempChange = 0.0f;

    // std::ifstream is("input.txt");
    // char c;
    // while (is.get(c)) {
    //     std::cout << c;
    // }

    getCharFromInput(std::cin);

    printThermostat(currentTemp, std::cout);

    return 0;
}

char getCharFromInput(std::istream& in) {
    char c;
    in >> c;
    return c;
}

float getNumberFromInput(std::istream& in) {
    float f;
    in >> f;
    return f;
}

void printThermostat(const float& temp, std::ostream& out) {
    out << "Temp is " << temp << std::endl;
    out << "test\n";
}