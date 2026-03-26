import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.matrix import MatrixScanner, DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins=(
        board.GP0,  board.GP1,  board.GP2,  board.GP3,
        board.GP4,  board.GP5,  board.GP6,  board.GP7,
        board.GP8,  board.GP9,  board.GP10, board.GP11,
        board.GP12, board.GP13,
    ),
    row_pins=(
        board.GP16, board.GP17, board.GP18, board.GP19, board.GP20,
    ),
    diode_orientation=DiodeOrientation.COL2ROW,
)

layers = Layers()

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP27, board.GP26, None, False),
)

keyboard.modules = [layers, encoder_handler]

_______ = KC.TRNS

keyboard.keymap = [

    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.MUTE,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSPC,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.NO,   KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.RALT, KC.MO(1),KC.APP,  KC.RCTL, KC.NO,
    ],

    [
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.MUTE,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.PSCR, KC.SLCK, KC.PAUS, KC.DEL,
        _______, _______, _______, _______, _______, _______, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, _______, _______, _______, KC.NO,
        _______, _______, _______, _______, _______, _______, _______, KC.MUTE, KC.VOLD, KC.VOLU, _______, _______, KC.NO,   KC.NO,
        _______, _______, _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, KC.NO,   _______, _______, _______, KC.RESET,KC.NO,
    ],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),   # Layer 0
    ((KC.MPRV, KC.MNXT),),   # Layer 1
]

if __name__ == '__main__':
    keyboard.go()