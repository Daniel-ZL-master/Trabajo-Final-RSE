# BluetoothBridge

Módulo receptor de datos BLE para el PC. Este script se ejecuta en el ordenador y actúa como puente entre el Arduino Nano BLE 33 y el entorno de trabajo, recibiendo por Bluetooth Low Energy los datos de acelerómetro y giroscopio capturados por la placa.

## Descripción

El Arduino Nano BLE 33 transmite los datos de los sensores IMU (acelerómetro y giroscopio) mediante BLE. Este módulo, ejecutándose en el PC, se suscribe a las notificaciones del dispositivo, recibe los datos en tiempo real y los almacena o procesa según sea necesario.

## Requisitos

- Python 3.8 o superior
- Adaptador Bluetooth compatible con BLE en el PC
- Arduino Nano BLE 33 con el firmware correspondiente cargado

### Dependencias Python

```bash
pip install bleak
```

> La librería [`bleak`](https://github.com/hbldh/bleak) es multiplataforma (Windows, Linux, macOS) y permite la comunicación BLE desde Python.

## Uso

1. Asegúrate de que el Arduino Nano BLE 33 está encendido y ejecutando el firmware de adquisición.
2. Ejecuta el script desde la raíz de esta carpeta:

```bash
python bluetooth_bridge.py
```

3. El script escaneará dispositivos BLE cercanos, se conectará al Arduino y comenzará a recibir datos.

## Estructura de los datos recibidos

Los datos recibidos corresponden a las lecturas del IMU del Arduino Nano BLE 33:

| Campo | Descripción | Unidades |
|-------|-------------|----------|
| `acc_x` | Aceleración en el eje X | m/s² o g |
| `acc_y` | Aceleración en el eje Y | m/s² o g |
| `acc_z` | Aceleración en el eje Z | m/s² o g |
| `gyr_x` | Velocidad angular en el eje X | °/s |
| `gyr_y` | Velocidad angular en el eje Y | °/s |
| `gyr_z` | Velocidad angular en el eje Z | °/s |

## Relación con el resto del proyecto

Este módulo se utiliza principalmente durante la fase de **adquisición de datos** para construir el dataset con el que se entrena el modelo en Edge Impulse. Los datos recibidos se almacenan para su posterior uso en `Extraction_Code`.

## Hardware necesario

- Arduino Nano BLE 33 (con IMU integrado LSM9DS1)
- PC con Bluetooth 4.0 o superior
