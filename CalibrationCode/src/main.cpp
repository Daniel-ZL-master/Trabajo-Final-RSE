#include <Arduino.h>
#include <Arduino_BMI270_BMM150.h>
#include "BBTimer.hpp"

BBTimer timer(BB_TIMER1);

volatile bool readyToRead = false;

// Esta función se ejecuta por hardware cada 10ms
void triggerSample() {
    readyToRead = true;
}

void setup() {
    Serial.begin(115200);
    while (!Serial);

    if (!IMU.begin()) {
        while (1) {Serial.println("Failed to initialize IMU!");}
    }

    timer.setupTimer(10000, triggerSample);
    timer.timerStart();
}

void loop() {
    if (readyToRead) {
        readyToRead = false; // Reseteamos el flag
        
        float ax, ay, az, gx, gy, gz;
        if (IMU.accelerationAvailable() && IMU.gyroscopeAvailable()) {
            IMU.readAcceleration(ax, ay, az);
            IMU.readGyroscope(gx, gy, gz);

            // Salida para Edge Impulse
            Serial.print(ax); Serial.print("\t");
            Serial.print(ay); Serial.print("\t");
            Serial.print(az); Serial.print("\t");
            Serial.print(gx); Serial.print("\t");
            Serial.print(gy); Serial.print("\t");
            Serial.println(gz);
        }
    }
}