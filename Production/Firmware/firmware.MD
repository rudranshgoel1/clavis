## Flashing and Configuring the Keyboard

Steps to install the firmware and configure the keyboard:

### 1. Downloading the Repository
Download or clone this repository to your computer.
https://github.com/rudranshgoel1/clavis.git

### 2. Enter Boot Mode on the Pico
1. Unplug the Raspberry Pi Pico from your computer.
2. Hold down the **BOOTSEL** button on the Pico.
3. While holding the button, plug the Pico into your computer using a USB cable.
4. The computer will detect a new drive named **RPI-RP2**.

### 3. Flash CircuitPython
1. Download the latest CircuitPython `.uf2` for the Raspberry Pi Pico from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/).
2. Drag and drop the `.uf2` file onto the **RPI-RP2** drive.

Once the file finishes copying, the Pico will reboot automatically and appear as a new drive named **CIRCUITPY**.

### 4. Install KMK and the Keymap
1. Download KMK from [kmkfw.io](https://kmkfw.io) and copy the `kmk/` folder to the root of **CIRCUITPY**.
2. Copy `main.py` from this repository to the root of **CIRCUITPY**.

Your drive should look like this:
```
CIRCUITPY/
├── main.py
└── kmk/
```

### 5. Configure the Keymap
The keyboard layout can be customised in `main.py`.

Open the file in a text editor and edit the keymap section to match the layout you want.
After saving the file, the keyboard will automatically reload with the new configuration.

### 6. Test the Keyboard
Unplug and reconnect the keyboard, open a text editor, and press some keys to make sure everything works.

## KABOOM!
IT'S DONE!!!