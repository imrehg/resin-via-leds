import os
from time import sleep
import gpio

try:
    PIN = int(os.getenv('PIN', 1))
except (TypeError, ValueError):
    PIN = 1

if __name__ == '__main__':
    value = 0
    gpio.setup(PIN, gpio.OUT)
    while True:
        gpio.set(PIN, value)
        value = 1 - value
        sleep(0.25)
