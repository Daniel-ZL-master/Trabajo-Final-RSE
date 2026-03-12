import asyncio
from bleak import BleakClient, BleakScanner

# Configuración: Nombre del dispositivo y el UUID de la característica
DEVICE_NAME = "RC_Car_IMU"
CHARACTERISTIC_UUID = "2A57"


def notification_handler(sender, data):
    """
    Se ejecuta automáticamente cada vez que el Arduino envía datos.
    'data' es un objeto de bytes.
    """
    # Si tus datos son 3 floats (12 bytes), los desempaquetamos:
    import struct
    try:
        # '<3f' significa: little-endian, 3 floats
        values = struct.unpack('<3f', data)
        print(f"Datos recibidos: X={values[0]:.2f}, Y={values[1]:.2f}, Z={values[2]:.2f}")
    except Exception as e:
        print(f"Error al decodificar: {e}")


async def run():
    print(f"Buscando el dispositivo '{DEVICE_NAME}'...")

    # Buscamos el dispositivo por nombre
    device = await BleakScanner.find_device_by_filter(
        lambda d, ad: d.name and d.name.lower() == DEVICE_NAME.lower()
    )

    if not device:
        print("Dispositivo no encontrado. ¿Está encendido?")
        return

    print(f"Dispositivo encontrado en {device.address}. Conectando...")

    # Conexión sin emparejamiento (Evita errores de timeout por seguridad)
    async with BleakClient(device, timeout=20.0) as client:
        print("Conectado exitosamente.")

        # Iniciamos la escucha de notificaciones
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        print("Escuchando notificaciones... (Presiona Ctrl+C para salir)")

        # Mantenemos el programa vivo
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\nDesconectado por el usuario.")
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")