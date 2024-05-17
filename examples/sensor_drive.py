from time import sleep
from pycreate2 import Create2

bot = Create2(port="/dev/ttyUSB0", baud=115200)
    
sensor = bot.get_sensors()

bot.safe()

for i in range(0, 1000):
    if sensor.wall:
        bot.drive_direct(-10, -10)
        sleep(1)
        bot.drive_direct(10, -10)
        sleep(1)
        bot.drive_stop()
    else:
        bot.drive_direct(10, 10)

bot.stop()
