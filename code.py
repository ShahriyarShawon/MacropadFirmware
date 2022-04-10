import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time

import board
import microcontroller
from digitalio import DigitalInOut, Direction, Pull

# LED Setup
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

col1 = DigitalInOut(microcontroller.pin.GPIO21)
col1.direction = Direction.OUTPUT

col2 = DigitalInOut(microcontroller.pin.GPIO20)
col2.direction = Direction.OUTPUT

col3 = DigitalInOut(microcontroller.pin.GPIO19)
col3.direction = Direction.OUTPUT
cols = [col1, col2, col3]

row1 = DigitalInOut(microcontroller.pin.GPIO11)
row1.direction = Direction.INPUT
row1.pull = Pull.DOWN

row2 = DigitalInOut(microcontroller.pin.GPIO12)
row2.direction = Direction.INPUT
row2.pull = Pull.DOWN

row3 = DigitalInOut(microcontroller.pin.GPIO13)
row3.direction = Direction.INPUT
row3.pull = Pull.DOWN
rows = [row1, row2, row3]


kbd = Keyboard(usb_hid.devices)
cc  = ConsumerControl(usb_hid.devices)


## Press and release CapsLock.
#kbd.press(Keycode.CAPS_LOCK)
#time.sleep(.09)
#kbd.release(Keycode.CAPS_LOCK)
#
#print("Hello World!")


def btn_one():
    print("One pressed")
    kbd.send(Keycode.CAPS_LOCK)
    pass
def btn_two():
    print("Two pressed")
    kbd.send(Keycode.ALT, Keycode.RETURN)
    pass
def btn_three():
    print("Three pressed")
    kbd.send(Keycode.ALT, Keycode.Q)
    pass
def btn_four():
    print("Four pressed")
    cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
    pass
def btn_five():
    print("Five pressed")
    cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
    pass
def btn_six():
    print("Six pressed")
    pass
def btn_seven():
    print("Seven pressed")
    pass
def btn_eight():
    print("Eight pressed")
    pass
def btn_nine():
    print("Nine pressed")
    pass
btn_functions = {
    "(0,0)": btn_one,
    "(0,1)": btn_two,
    "(0,2)": btn_three,
    "(1,0)": btn_four,
    "(1,1)": btn_five,
    "(1,2)": btn_six,
    "(2,0)": btn_seven,
    "(2,1)": btn_eight,
    "(2,2)": btn_nine,
}

btn_press_buff = []

while True:
    for col_idx, c in enumerate(cols):
        c.value = True
		
        for row_idx, r in enumerate(rows):
            if r.value == True and c.value:
                #print(f"({row_idx},{col_idx}) is pressed")	
                combo_str = f"({row_idx},{col_idx})"
                btn_press_buff.append(combo_str)
                btn_functions[combo_str]()
        c.value = False
    if len(btn_press_buff) != 0:
        print(btn_press_buff)
        btn_press_buff.clear()
    time.sleep(0.075)



