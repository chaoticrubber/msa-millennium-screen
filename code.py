#
# gc9a01_picture_locket.py -- Simple Demo of GC9A01 Round LCD 
#
# 2021 - Tod Kurt - todbot.com
#
# Tested on QTPy (SAMD21), QTPy RP2040, and Raspberry Pi Pico (RP2040)
# running CircuitPython 7.
#
# You'll need to install 'gc9a01' package.
# Easiest way to do this is from Terminal:
#  circup install gc9a01
#

import time
import board # type: ignore
import math
import busio
import terminalio
import displayio
import adafruit_imageload
import cst816
import gc9a01 as gc9a01
import microcontroller
# Initialize I2C
i2c = busio.I2C(board.GP7,board.GP6)
touch = cst816.CST816(i2c)

# Check if the touch controller is detected
if touch.who_am_i():
    print("CST816 detected.")
else:
    print("CST816 not detected.")

# Global variables
display_on = True  # Track whether the display is on or off
long_press_threshold = 2  # Threshold in seconds for a long press
touch_start_time = None



def turn_off_display():
    global display_on
    # Turn off the display backlight or use any other method required to turn off your display
    display.brightness = 0  # Assuming your display supports this, otherwise use GPIO to control power
    display_on = False  # Update the state variable

def turn_on_display():
    global display_on
    # Turn on the display backlight or use any other method required to turn on your display
    display.brightness = 1  # Adjust as necessary for your display
    display_on = True  # Update the state variable
    apply_image(i)  # Reapply the current image to refresh the display

#last image needs to be "/imgs/black.bmp" - as the screen turns off when the last image in this string is active 
img_filenames = ("/imgs/home.bmp","/imgs/brat.bmp","/imgs/PB.bmp","/imgs/bate.bmp","/imgs/drone.bmp","/imgs/chaos.bmp","/imgs/spiderface.bmp","/imgs/spider.bmp","/imgs/black.bmp",)

# Release any resources currently in use for the displays
displayio.release_displays()
#elif 'Waveshare RP2040-LCD-1.28 with rp2040' in board_type:
tft_clk = board.LCD_CLK
tft_mosi = board.LCD_DIN
tft_rst = board.LCD_RST
tft_dc = board.LCD_DC
tft_cs = board.LCD_CS
tft_bl = board.LCD_BL
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)
main = displayio.Group()
display.root_group = main
i = 0

def change_image():
    global i  # Declare i as global to modify the global variable
    print(i)
    if len(main) > 0:  # Check if there is an image to remove
        main.pop()  # Remove the current image
    i = (i + 1) % len(img_filenames)  # Update the global i
    if i == 0:  # If it's the first image
        turn_on_display()  # Turn the display on
    apply_image(i)

def apply_image(i):
    if i == len(img_filenames) - 1:  # If it's the last image
        turn_off_display()  # Turn the display off before loading the last image
        
    img_filename = img_filenames[i]
    img_bitmap, img_palette = adafruit_imageload.load(img_filename, bitmap=displayio.Bitmap, palette=displayio.Palette)
    img_tilegrid = displayio.TileGrid(img_bitmap, pixel_shader=img_palette)
    main.append(img_tilegrid)
    time.sleep(0.25)


def turn_off_display():
    # Assuming your display supports this, otherwise use GPIO to control power
    display.brightness = 0

def turn_on_display():
    # Adjust as necessary for your display
    display.brightness = 1

apply_image(i)  # Pass i as an argument

while True:
    try:
        press = touch.get_touch()
        if press:
            change_image()  # No need to pass i, as it's global
    except MemoryError:
        print("MemoryError detected, resetting...")
        microcontroller.reset()  # Reset the microcontroller on MemoryError

