import time
import sys

waitTime = ""
for i in range(1, 10):
    waitTime+="."
    print(f"{waitTime}", end="\r")
    time.sleep(.25)

print("Enter here: ")
sys.stdin.read(1)
