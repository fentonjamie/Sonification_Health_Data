import csv
from array import array
import numpy as np

with open('Health Data.csv', newline = '') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    results = []
    for row in reader:
        results.append(row[1])


results_array = array('f', results)
data = np.array(results_array)

max = np.amax(data)

normal = np.divide(data, max)

normlog = np.array([])

for i in normal:
    if i == 0:
        i = 0.001
    normlog = np.append(normlog, i)

logdata = np.log10(normlog)

print(logdata)

logdatamax = np.min(logdata)

print(logdatamax)

logDataNorm = np.divide(logdata, logdatamax)

print(logDataNorm)

MIDI = 1 - logDataNorm

MIDIData = np.rint(MIDI*30 + 36)

CMIDI = []

for x in MIDIData:
    if x == 30 or x == 32 or x == 34 or x == 37 or x == 39 or x == 42 or x == 44 or x == 46 or x == 49 or x == 51 or x == 54 or x == 56 or x == 58 or x == 61 or x == 63 or x == 66 or x == 68 or x == 70 or x == 73 or x == 75:
        x = x + 1
    CMIDI = np.append(CMIDI, x)

print("Copy this Array into the MIDIData script : ")
for i in CMIDI:
    print(int(i), end = ', ')





