# Imports
import sys

# Input
byte = input("\n")

# Check if contains anything that isn't a 0 or 1; exits program if invalid
for char in byte:
    if char != "1" and char != "0":
        print("Invalid bit sequence. Must contain only 1s and 0s.\n")
        sys.exit()

# Loop through bit sequence and convert to decimal
dec = 0
for i in range(0, len(byte)):
    dec += 2**i if byte[i] == "1" else 0

# Output
print("Bit Sequence -> " + byte)
print("Decimal Number -> " + str(dec) + "\n")
