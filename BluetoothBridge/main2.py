import asyncio
import json
from bleak import BleakScanner, BleakClient

DEVICE_NAME = "Arduino-ML-Dani"
CHAR_UUID   = "abcd1234-ab12-ab12-ab12-abcdef123456"

def notificacion_recibida(sender, data):
    try:
        predicciones = json.loads(data.decode("utf-8"))
        
        # Ordenar por valor descendente
        predicciones.sort(key=lambda x: x["valor"], reverse=True)
        
        print("\n── Resultado del modelo ──")
        for p in predicciones:
            barra = "█" * int(p["valor"] * 20)
            print(f"  {p['label']:<10} {barra:<20} {p['valor']:.2%}")
    
    except Exception as e:
        print(f"Error parseando datos: {e}")

async def main():
    print("Buscando Arduino-ML-Dani...")
    device = await BleakScanner.find_device_by_name(DEVICE_NAME)
    if not device:
        print("Dispositivo no encontrado")
        return

    async with BleakClient(device, max_mtu=256) as client:
        print(f"Conectado a {device.name}")
        await client.start_notify(CHAR_UUID, notificacion_recibida)
        await asyncio.sleep(60)
        await client.stop_notify(CHAR_UUID)

asyncio.run(main()) 
