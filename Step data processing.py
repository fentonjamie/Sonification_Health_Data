import csv
from array import array
import numpy as np

with open('Health Data.csv', newline = '') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    results = []
    for row in reader:
        results.append(row[1])

# create a numpy arry of the data loaded in called data

results_array = array('f', results)
data = np.array(results_array)

# find the maximum value in this array and normalise it by diving every value by the max
# the goal is to create data that varies between about 35 and 80, at the moment it's between 0 and 2000

max = np.amax(data)
normal = np.divide(data, max)
normlog = np.array([])

# make sure no value is 0 as we prepare to log the values if a value is 0 make it 0.001
# print functions are there to check data along the way and catch any mistakes

for i in normal:
    if i == 0:
        i = 0.001
    normlog = np.append(normlog, i)

#log the values to make them closer to each other

logdata = np.log10(normlog)

print(logdata)

# repeat the process again normalise values and then log for a second time, this brings the values into
# the type of range we need for MIDI data

logdatamax = np.min(logdata)
print(logdatamax)
logDataNorm = np.divide(logdata, logdatamax)
print(logDataNorm)

# we now have a reasonable range. But they are reversed do 1 - logDataNorm to make the largest step counts
# the largest numbers

MIDI = 1 - logDataNorm

# add 36 to make all lowest values start at this value
#multiply by 30 to give a good range between lowest and higest. np.rint rounds to interger value

MIDIData = np.rint(MIDI*30 + 36)

CMIDI = []

# Now if the MIDI values are anything other than the value sin the C major scale round them up to a Cmajor scale value

for x in MIDIData:
    if x == 30 or x == 32 or x == 34 or x == 37 or x == 39 or x == 42 or x == 44 or x == 46 or x == 49 or x == 51 or x == 54 or x == 56 or x == 58 or x == 61 or x == 63 or x == 66 or x == 68 or x == 70 or x == 73 or x == 75:
        x = x + 1
    CMIDI = np.append(CMIDI, x)

# MICRO:BIT can't use numpy and the other libaries used to process this data. Do this final array that is created
# Has to be copied across to the main function script

print("Copy this Array into the MIDIData script : ")
for i in CMIDI:
    print(int(i), end = ', ')





