// Compile and run in one line using 'g++ thermostat.cpp && ./a.exe' or './a.out'

#include <iostream>
#include <string>
#include <limits>

const int MIN_TEMPERATURE = 30.0f;
const int MAX_TEMPERATURE = 100.0f;
const int DEFAULT_TEMPERATURE = 76.0f;

char getCharFromInput(std::istream&);
float getNumberFromInput(std::istream&);
std::string checkNewTemperature(float);
void printThermostat(const float&, std::ostream&);

int main() {
    char command;
    float currentTemperature = DEFAULT_TEMPERATURE;
    float temperatureChange = 0.0f;

    // Welcome prompt
    std::cout << "Hi, welcome to Cpp Thermostat!" << std::endl;

    bool isOn = true;
    while (isOn) {
        std::cout << std::endl;
        printThermostat(currentTemperature, std::cout);

        std::cout << "Enter a command below:" << std::endl;
        command = getCharFromInput(std::cin);

        switch (command) {
            case 'i': { 
                    temperatureChange = getNumberFromInput(std::cin);
                    std::string msg = checkNewTemperature(currentTemperature + temperatureChange);
                    if (msg == "✅") {
                        currentTemperature += temperatureChange;
                    }
                    std::cout << msg << std::endl;
                }
                break;
            case 'd': {
                    temperatureChange = getNumberFromInput(std::cin);
                    std::string msg = checkNewTemperature(currentTemperature - temperatureChange);
                    if (msg == "✅") {
                        currentTemperature -= temperatureChange;
                    }
                    std::cout << msg << std::endl;
                }
                break;
            case 'r':   
                currentTemperature = DEFAULT_TEMPERATURE;
                std::cout << "⏮" << std::endl;
                break;
            case 'o':
                isOn = false;
                std::cout << "⛔" << std::endl;
                return 0; 
            default:
                std::cout << "❌ Invalid command, try again 🔄" << std::endl;
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }

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

std::string checkNewTemperature(float newTemp) {
    if (newTemp > MAX_TEMPERATURE) {
        return "❌ Thermostat cannot exceed 100 ℉ 🔥";
    }
    if (newTemp < MIN_TEMPERATURE) {
        return "❌ Thermostat cannot drop below 30 ℉ 🧊";
    }
    return "✅";
}

void printThermostat(const float& temperature, std::ostream& out) {
    out << "Temperature is " << temperature << " ℉" << std::endl;
}
