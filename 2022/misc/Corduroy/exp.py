#!/usr/bin/env python3

from scipy.io import wavfile
import numpy as np

# For better results, use e.g. Audacity's noise reduction function on the WAV file before running this script
rate, data = wavfile.read("ljud.wav")

def window(size):
    return np.ones(size) / float(size)

# Read the WAV data and take a running average of its amplitude
values = np.absolute(np.array(data))
avg = np.convolve(values, window(50), "same")

high = False # Was the last state high or not (low)
last_change = 0 # Used to ignore transitions between bits
bit_length = 150 # Number of samples per bit, obtained visually through Audacity
result = ""

for index, sample in enumerate(avg):
    # Skip iteration if this is not a transition
    if not ((sample > 4500 and not high) or (sample < 4500 and high)):
        continue

    high = not high
    # Check if this transition aligns with the expected bit interval
    if index - last_change > bit_length:
        # Don't treat the first transition as a bit
        if last_change == 0:
            last_change = index - 150
        else:
            result += "1" if high else "0"
            last_change = index

result_int = int(result, 2)
print(result_int.to_bytes((result_int.bit_length() + 7) // 8, "big").decode(errors="replace"))
