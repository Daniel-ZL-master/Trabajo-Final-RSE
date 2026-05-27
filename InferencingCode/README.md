# InferencingCode

Código de inferencia en tiempo real para el Arduino Nano BLE 33. Este módulo contiene el firmware que ejecuta el modelo de Machine Learning generado con Edge Impulse directamente en la placa, clasificando en tiempo real los eventos de colisión detectados por el acelerómetro y el giroscopio.

## Descripción

Una vez entrenado el modelo en Edge Impulse y exportada la librería correspondiente (ver `LIBRARY_EDGE_IMPULSE`), este firmware se encarga de:

1. Leer continuamente los datos del IMU (acelerómetro y giroscopio) del Arduino Nano BLE 33.
2. Alimentar el modelo de clasificación con las ventanas de datos capturadas.
3. Obtener la clase predicha y su nivel de confianza.
4. Enviar el resultado por BLE al PC (a través del módulo `BluetoothBridge`).

## Eventos detectados

El modelo clasifica los siguientes eventos:

| Clase | Descripción |
|-------|-------------|
| `colision_lateral_izquierda` | Colisión lateral izquierda en parado |
| `colision_lateral_derecha` | Colisión lateral derecha en parado |
| `colision_alcance` | Colisión por alcance en parado o en movimiento |
| `colision_frontal` | Colisión frontal en movimiento |
| `idle` | Sin evento (estado de reposo) |

## Requisitos

### Hardware
- Arduino Nano BLE 33
- IMU integrado: LSM9DS1 (acelerómetro + giroscopio)

### Software
- [Arduino IDE](https://www.arduino.cc/en/software) 1.8.x o 2.x, o [Arduino CLI](https://arduino.github.io/arduino-cli/)
- Librería del modelo Edge Impulse (incluida en `LIBRARY_EDGE_IMPULSE`)
- Librería `Arduino_LSM9DS1`

## Instalación

1. Instala la librería del modelo Edge Impulse en el Arduino IDE:
   - Ve a **Sketch → Incluir librería → Añadir librería .ZIP**
   - Selecciona el archivo `.zip` de la carpeta `LIBRARY_EDGE_IMPULSE`

2. Abre el sketch principal de esta carpeta en el Arduino IDE.

3. Selecciona la placa **Arduino Nano 33 BLE** y el puerto correspondiente.

4. Compila y carga el firmware:

```bash
# Con Arduino CLI
arduino-cli compile --fqbn arduino:mbed_nano:nano33ble .
arduino-cli upload  --fqbn arduino:mbed_nano:nano33ble --port /dev/ttyACM0 .
```

## Uso

Una vez cargado el firmware, el Arduino:
- Comienza a capturar datos del IMU automáticamente al arrancar.
- Ejecuta el modelo de inferencia de forma continua.
- Transmite los resultados de clasificación por BLE.

Para visualizar los resultados en el PC, usa el módulo `BluetoothBridge` o el Monitor Serie del Arduino IDE.

## Relación con el resto del proyecto

```
Extraction_Code  →  (datos crudos)  →  Edge Impulse (entrenamiento)
                                              ↓
LIBRARY_EDGE_IMPULSE  ←  (modelo exportado)
                              ↓
                       InferencingCode  →  (inferencia en placa)  →  BluetoothBridge
```
