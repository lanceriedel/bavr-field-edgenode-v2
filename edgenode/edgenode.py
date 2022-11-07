import asyncio
import uuid
from loguru import logger
import board
import adafruit_tcs34725
i2c = board.I2C()




class EdgeNodeModule:
    def __init__(self) -> None:
        super().__init__()

        # create the FCC objects

    async def run(self) -> None:
        with open('/hostetc/machine-id', 'r') as file:
            uuid = file.read().rstrip()
        
        uuid_field = uuid[-8:]
        logger.debug(f"UUID for board is '{uuid_field}'")

        # Create sensor object, communicating over the board's default I2C bus
        i2c = board.I2C()  # uses board.SCL and board.SDA
        sensor = adafruit_tcs34725.TCS34725(i2c)

        while True:
            await asyncio.sleep(1)
            print('Temperature: {0}K'.format(sensor.color_temperature))
            print('Lux: {0}'.format(sensor.lux))


if __name__ == "__main__":
    edgeNode = EdgeNodeModule()
    asyncio.run(edgeNode.run())

