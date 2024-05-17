from pycreate2 import Create2
from pyPS4Controller import Controller

bot = Create2(port="/dev/ttyUSB0", baud=115200)

class BotController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        bot.drive_direct(200, 200) 

    def on_circle_press(self):
        bot.drive_direct(200, 200)

    def on_left_arrow_press(self):
        bot.drive_direct(-200, 200)

    def on_right_arrow_press(self):
        bot.drive_direct(200, -200)

    def on_x_release(self):
        bot.drive_stop()

    def on_circle_release(self):
        bot.drive_stop()

    def on_left_arrow_release(self):
        bot.drive_stop()

    def on_right_arrow_release(self):
        bot.drive_stop()

bot.safe()

controller = BotController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

bot.stop()
