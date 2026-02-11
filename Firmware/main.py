import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry

# Load the hardware definition from kb.py
keyboard = KMKKeyboard()

# -------------------------------------------------
# 1. ROTARY ENCODER (Knob)
# -------------------------------------------------
# Pin A = D2, Pin B = D1
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.D2, board.D1, None, False),)
# Map rotation to Volume Up / Volume Down. 
# The 3rd slot is KC.NO because the button is handled in the matrix below.
encoder_handler.map = [((KC.VOLU, KC.VOLD, KC.NO),)]

# -------------------------------------------------
# 2. RGB LEDS (Underglow)
# -------------------------------------------------
# Data Pin = D0
rgb = RGB(
    pixel_pin=board.D0,
    num_pixels=6,
    val_limit=100,    # Max brightness (0-255)
    hue_default=0,    # Red start color
    sat_default=255,
    val_default=100,
    rgb_order=(1, 0, 2) # GRB order (Standard for SK6812)
)
keyboard.extensions.append(rgb)

# -------------------------------------------------
# 3. OLED DISPLAY
# -------------------------------------------------
# I2C Pins: SCL = D5, SDA = D4
i2c_bus = busio.I2C(board.D5, board.D4)

display_driver = Display(
    display_class=adafruit_displayio_ssd1306.SSD1306_I2C,
    width=128,
    height=32,
    i2c_bus=i2c_bus,
    flip=False,       # Change to True if screen is upside down
    brightness=1.0,
    dim_time=20,
    dim_target=0.1,
    off_time=60,
)

# What to show on screen
display_driver.entries = [
    TextEntry(text='Rudras HackPad', x=0, y=0, y_anchor='O'),
    TextEntry(text='Layer: 0', x=0, y=12),
]
keyboard.extensions.append(display_driver)

# -------------------------------------------------
# 4. KEYMAP (What the buttons do)
# -------------------------------------------------
# Order: SW1, SW4, SW5, SW6, EncoderButton
keyboard.keymap = [
    [
        KC.UP,      # SW1 (Top)
        KC.LEFT,    # SW4 (Left)
        KC.DOWN,    # SW5 (Bottom)
        KC.RIGHT,   # SW6 (Right)
        KC.ENTER,   # Encoder Button (Pushing the knob)
    ]
]

if __name__ == '__main__':
    keyboard.go()
