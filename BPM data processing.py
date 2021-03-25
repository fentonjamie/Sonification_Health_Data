from array import array
import numpy as np
import csv


with open('Health Data.csv', newline = '') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    results = []
    for row in reader:
        results.append(row[2])

# create numpy array of results data

results_array = array('f', results)
MIDIData = np.array(results_array)

#for note velocity data just normalise array and multiply by 127 (maximum velocity)

VelData = ((MIDIData/np.amax(MIDIData))*127)
#BeatData = ((1 - (0.99 * MIDIData/np.amax(MIDIData)))*5000)

#If the data isn't in the Cmajor scale round up a semitone to make it in C major

CMIDI = []

for x in MIDIData:
    if x == 56 or x == 58 or x == 61 or x == 63 or x == 66 or x == 68 or x == 70 or x == 73 or x == 75 or x == 78 or x == 80 or x == 82 or x == 85 or x == 87 or x == 90 or x == 92 or x == 94 or x == 97 or x == 99 or x == 102 or x == 104 or x == 106 or x == 109 or x == 111 or x == 114:
        x = x + 1
    CMIDI = np.append(CMIDI, x)

#As this couldn't be done in the MICROBIT python script the arrays should be copied into the main function script arrays

print("Copy this Array into the MIDIData script : ")
for i in CMIDI:
    print(int(i), end = ', ')

print("Copy this Array into the MIDIVel array : ")
for i in VelData:
    print(int(i), end = ', ')











