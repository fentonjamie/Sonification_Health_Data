from microbit import *

#This script flashes to the MICROBIT and sends the MIDI data to a DAW via a MIDI cable
#This is where all the array data from the data processing scripts should be inserted

MIDIData = [36, 36, 36, 36, 36, 36, 45, 50, 55, 62, 55, 52, 47, 57, 47, 59, 67, 43, 59, 59, 36, 38, 43, 36]

MIDIDataHeart = [64, 66, 64, 61, 57, 58, 58, 59, 70, 100, 76, 70, 61, 68, 72, 79, 104, 66, 82, 98, 62, 60, 63, 65]

MIDIVelocityData = [78, 81, 76, 75, 70, 71, 71, 72, 85, 122, 92, 86, 74, 83, 88, 96, 127, 81, 100, 120, 75, 73, 77, 79]

#These functions set up the MIDI controller
#If the values are out of the value scope then return

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

#Set last button values to false to begin with as no buttons have been pressed, these will change when buttons have been pressed

Start()
lastA = False
lastB = False
lastC = False
lastD = False

#set variables of timer and itiration value to zero

timer = 0
i = 0

# create the functions to play the MIDI note data, these return the value of the MIDI array that
# the iteration variable i is currently at

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
#set up the variables that determine when the buttons are pressed
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = pin1.is_touched()
    d = pin2.is_touched()

#create the functions that check if the button has been pressed for a, b and c
#If last A is false and A has been pressed that means lastA switches to true and a message is displayed
#If A has been pressed it will make the MIDI notes play, if ressed again it will pause.
#If B is pressed it resets all the buttons to false and sets the iteration number to 0 causing it to restart
# If c is pressed it is similar to A except it iterates through the BPM data
#If d is pressed it itirates through the BPM velocity array

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
        display.scroll("Play BPM data")

    if d is True:
        display.scroll("BPM as velocity")
        lastD = not lastD

#these funtions then play the MIDI notes as the arrays are being iterated through.
#If the timer is at the correct time and the correct button has been pressed it will iterate through the
#array and play the MIDI notes until one of the conditions isn't met

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


#This stops the audio when the array is finished if the itieration value increases above the length of the array
#It will restart and all buttons set back to false

    if i >= len(MIDIData) - 1:
        i = 0
        lastA = False
        lastB = False
        lastC = False
        lastD = False

#At the end of this loop the timer adds 5 to itself and sleeps for 5ms and then runs through to loop again
#to check if any conditions have changed.

    timer = timer + 5

    sleep(5)






