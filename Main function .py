from microbit import *

MIDIData = [36, 36, 36, 36, 36, 36, 45, 50, 55, 62, 55, 52, 47, 57, 47, 59, 67, 43, 59, 59, 36, 38, 43, 36]

time = ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM']

MIDIDataHeart = [64, 66, 64, 61, 57, 58, 58, 59, 70, 100, 76, 70, 61, 68, 72, 79, 104, 66, 82, 98, 62, 60, 63, 65]

MIDIVelocityData = [78, 81, 76, 75, 70, 71, 71, 72, 85, 122, 92, 86, 74, 83, 88, 96, 127, 81, 100, 120, 75, 73, 77, 79]

MIDIBeatData = [772, 729, 802, 827, 903, 887, 884, 876, 665, 92, 550, 650, 833, 700, 620, 494, 19, 736, 433, 125, 821, 859, 791, 754]

zipped = zip(MIDIData, MIDIDataHeart, time, MIDIVelocityData, MIDIBeatData)

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
lastA = False
lastB = False
lastC = False
lastD = False

timer = 0
i = 0

# create the functions to play the MIDI note and heart data and velocity heart data

def PlayMidiNote():
        x = MIDIData[i]
        return x
def PlayHeartData():
        y = MIDIDataHeart[i]
        return y
def PlayHeartVel():
        z = MIDIVelocityData[i]
        return z

while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = pin1.is_touched()
    d = pin2.is_touched()

#create the functions that see if the button has been pressed for a and b

    if a is True and lastA is False:
        display.scroll("Play")
        lastA = not lastA

    elif a is True and lastA is True:
        display.scroll("Pause")
        lastA = not lastA

    if b is True:
        display.scroll("Resart")
        midiNoteOff(1, PlayMidiNote(), 0)
        midiNoteOff(2, PlayHeartData(), 0)
        lastA = False
        lastD = False
        lastC = False
        i = 0

    if pin1.is_touched() is True:
        lastC = not lastC
        display.scroll("C")

    if d is True:
        display.scroll("BPM as vel")
        lastD = not lastD

#run through the arrays if the correct requirements are met

    if timer % 1000 == 0 and i < len(MIDIData) - 1 and lastA is True:
        i = i + 1
        midiNoteOn(1, PlayMidiNote(), 127)

    if timer % 1000 == 500 and i < len(MIDIDataHeart) - 1 and lastC is True:
        if lastA is False:
            i = i + 1 #increase array number if A isnt running through
        midiNoteOn(2, PlayHeartData(), 127)


    if timer % 1000 == 0 and i < len(MIDIData) - 1 and lastD is True:
        i = i + 1
        lastA = False
        lastC = False
        midiNoteOn(1, PlayMidiNote(), PlayHeartVel())


#This stops the audio when the array is finished

    if i >= len(MIDIData) - 1:
        i = 0
        lastA = False
        lastB = False
        lastC = False
        lastD = False

    timer = timer + 5

    sleep(5)



