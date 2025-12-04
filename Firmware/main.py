#I do not know what the heck I am doing so we'll see if this works
import board
#I did in fact Borrow the basis or really most of this from the Cyao example...
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.LED import LED, AnimationModes
from kmk.extensions.display.ssd1306 import SSD1306

COL0 = board.GP7;
COL1 = board.GP8;
COL2 = board.GP9;
ROW0 = board.GP3;
ROW1 = board.GP2;
ROW2 = board.GP1;
ROW3 = board.GP0;

LED_PIN = board.GP10;

keyboard = KMKKeyboard();

macros = Macros();
keyboard.modules.append(macros);

keyboard.extensions.append(display);

led = LED(
    led_pin=[LED_PIN],
    animation_mode=AnimationModes.BREATHING,
    brightness=50
);
keyboard.extensions.append(led);

keyboard.col_pins = (COL0, COL1, COL2,);
keyboard.row_pins = (ROW0, ROW1, ROW2, ROW3);
keyboard.diode_orientation = DiodeOrientation.COL2ROW;

keyboard.keymap = [
    [KC.ESCAPE,      KC.ANY,   KC.ANY,  ],
    [KC.ANY,      KC.ANY,     KC.ANY,   ],
    [KC.TRNS,      KC.UP,     KC.TRNS,  ],
    [KC.LEFT,   KC.DOWN,   KC.RIGHT     ],
];

if __name__ == '__main__':
    keyboard.go();
