from time import sleep
from pycreate2 import Create2

bot = Create2(port="/dev/ttyUSB0", baud=115200)
    
bot.safe()

bot.drive_direct(10, 10)
sleep(5)
bot.drive_stop()

bot.stop()