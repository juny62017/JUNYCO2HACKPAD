import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # -------------------------------------------------
        # HARDWARE DEFINITION
        # -------------------------------------------------
        # We use KeysScanner because your switches are directly wired to pins 
        # (Direct Pin method), not a Row/Column matrix.
        
        # Pin Mapping from your Netlist:
        # SW1 = D7
        # SW4 = D8
        # SW5 = D10
        # SW6 = D9
        # Encoder Button (SW10-S1) = D3
        
        self.matrix = KeysScanner(
            pins=[board.D7, board.D8, board.D10, board.D9, board.D3],
            value_when_pressed=False, # Switches connect to GND when pressed
            pull=True,                # Enable internal pull-up resistors
            interval=0.02,            # Debounce time
        )
