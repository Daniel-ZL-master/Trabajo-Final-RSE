# LIBRARY_EDGE_IMPULSE

Librería de inferencia exportada desde [Edge Impulse Studio](https://studio.edgeimpulse.com) para el Arduino Nano BLE 33. Contiene el modelo de Machine Learning entrenado para la clasificación de eventos de colisión, listo para ser integrado en el firmware de inferencia.

## Descripción

Edge Impulse exporta el modelo entrenado como una librería Arduino (`.zip`) que incluye el modelo cuantizado, el procesado de señal (DSP) y el motor de inferencia optimizado para microcontroladores. Esta librería se usa directamente en `InferencingCode`.

La librería encapsula:

- **Impulso** (pipeline completo): bloque de extracción de características + clasificador.
- **Parámetros del modelo**: pesos de la red neuronal cuantizados para ejecutarse en hardware con recursos limitados.
- **Motor de inferencia**: basado en TensorFlow Lite for Microcontrollers (TFLite Micro).

## Clases del modelo

El modelo clasifica las siguientes categorías:

| Etiqueta | Descripción |
|----------|-------------|
| `colision_lateral_izquierda` | Impacto lateral por la izquierda en parado |
| `colision_lateral_derecha` | Impacto lateral por la derecha en parado |
| `colision_alcance` | Impacto por alcance (parado o en movimiento) |
| `colision_frontal` | Impacto frontal en movimiento |
| `idle` | Estado de reposo, sin evento |

## Instalación en Arduino IDE

1. Descarga o localiza el archivo `.zip` de esta carpeta.
2. En el Arduino IDE: **Programa → Incluir librería → Añadir librería .ZIP...**
3. Selecciona el archivo `.zip` de la librería.
4. La librería quedará disponible para ser incluida en sketches:

```cpp
#include <nombre-del-proyecto_inferencing.h>
```

## Instalación con Arduino CLI

```bash
arduino-cli lib install --zip-path LIBRARY_EDGE_IMPULSE/tu-proyecto.zip
```

## Actualización del modelo

Si se reentrena el modelo en Edge Impulse Studio (por ejemplo, con más datos o cambiando la arquitectura), hay que:

1. Ir a **Deployment** en Edge Impulse Studio.
2. Seleccionar **Arduino library** y hacer clic en **Build**.
3. Descargar el nuevo `.zip` y sustituir el contenido de esta carpeta.
4. Recompilar y recargar el firmware de `InferencingCode`.

## Referencia

- [Edge Impulse - Exportar librería Arduino](https://docs.edgeimpulse.com/docs/run-inference/arduino-library)
- [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers)
