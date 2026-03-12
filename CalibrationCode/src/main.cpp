#include <Arduino.h>
#include <ArduinoBLE.h>
#include <Arduino_BMI270_BMM150.h>
#include "BBTimer.hpp"

BLEService sensorService("180D");
// Cambiamos a BLERead | BLENotify para enviar bytes binarios (24 bytes = 6 floats)
BLECharacteristic dataChar("2A57", BLERead | BLENotify, 24);

BBTimer sampleTimer(BB_TIMER0);
volatile bool readyToRead = false;

void timerCallback() { readyToRead = true; }

void setup()
{
    if (!IMU.begin())
        while (1)
            ;
    if (!BLE.begin())
        while (1)
            ;
    BLE.setConnectionInterval(80, 160);
    BLE.setLocalName("RC_Car_IMU");
    BLE.setAdvertisedService(sensorService);
    sensorService.addCharacteristic(dataChar);
    BLE.addService(sensorService);
    BLE.advertise();
    BLE.setEventHandler(BLEConnected, [](BLEDevice central)
                        { digitalWrite(LED_BUILTIN, HIGH); });
    BLE.setEventHandler(BLEDisconnected, [](BLEDevice central)
                        { digitalWrite(LED_BUILTIN, LOW); });
    delay(500);
    // Ajustamos a 20ms (50Hz) para mayor estabilidad BLE
    sampleTimer.setupTimer(20000, timerCallback);
    sampleTimer.timerStart();
}

void loop()
{
    if (!BLE.connected()) {
    BLE.advertise();
  }
    BLEDevice central = BLE.central();
    if (central && central.connected())
    {
        if (readyToRead)
        {
            readyToRead = false;
            float data[6];
            IMU.readAcceleration(data[0], data[1], data[2]);
            IMU.readGyroscope(data[3], data[4], data[5]);

            // Enviamos el array de floats como bytes
            dataChar.writeValue((byte *)data, sizeof(data));
        }
    }
}