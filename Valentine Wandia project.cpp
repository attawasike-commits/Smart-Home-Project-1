//Valentine's rain detector system
#include <iostream>
#include <thread>
#include <chrono>
using namespace std;
int analogRead(int pin) {
    return 1023; 
}

void digitalWrite(int pin, std::string state) {
     cout << "Buzzer Pin " << pin << " set to " << state << endl;
}

int main() {
    const int rainSensorPin = 0; 
    const int buzzerPin = 9;     
    int rainValue = 0;

    cout << "--- Starting Desktop Rain Detector Simulation ---" << endl;

    for (int i = 0; i < 5; ++i) {
        rainValue = analogRead(rainSensorPin);
        cout << "Rain Sensor Value: " << rainValue << endl;

        if (rainValue < 600) {
            digitalWrite(buzzerPin, "HIGH (ALARM)");
        } else {
            digitalWrite(buzzerPin, "LOW (QUIET)");
        }



        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        cout << "-----------------------------------" << endl;
    }

 bool isRaining = (rainValue < 600); 

    if (isRaining) {
        cout << "Final Status: Rain detected." << endl;
        cout << "Closing windows..." << endl;
    } else {
        cout << "Final Status: No rain detected." << endl;
        cout << "Windows remain open." << endl;
    }

    return 0;
}
