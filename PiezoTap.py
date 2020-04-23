from microbit import *

def midiNoteOn(chan, n, vel):
    MIDI_NOTE_ON = 0x90
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel])
    uart.write(msg)

def midiNoteOff(chan, n, vel):
    MIDI_NOTE_OFF = 0x80
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_OFF | chan, n, vel])
    uart.write(msg)

def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()
lastPiezoVal = 900
currentPiezoVal = 900
BUTTON_A_NOTE = 35
BUTTON_B_NOTE = 39

while True:
    currentPiezoVal = pin2.read_analog()
    if (currentPiezoVal < 900) * (lastPiezoVal > 900):
        midiNoteOn(0, BUTTON_A_NOTE, 127)
#         print(currentPiezoVal)
    if (currentPiezoVal > 900) * (lastPiezoVal < 900):
        midiNoteOff(0, BUTTON_A_NOTE, 127)
#         print(currentPiezoVal)
    lastPiezoVal = currentPiezoVal
    sleep(50)