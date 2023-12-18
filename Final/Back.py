import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb = None
analog_pin = None
sample_interval = 0.01  # Sampling interval in seconds
samples_per_50ms = 5  # Number of samples per 0.05 seconds
current_color = (0, 0, 0)  # Initialize the current color

def setup():
    global rgb, analog_pin
    M5.begin()

    # Initialize RGB LED (assuming using pin G7 and 10 LEDs):
    rgb = RGB(io=7, n=90, type="SK6812")

    # Initialize an analog pin for input:
    analog_pin = ADC(Pin(1), atten=ADC.ATTN_11DB)

def loop():
    global rgb, analog_pin, current_color
    average_value = get_average_volume()

    # Map the average volume to a color between red and blue
    target_color = map_volume_to_color(average_value, 1800, 2000)

    fade_to_color(current_color, target_color)
    current_color = target_color
    print(average_value)

    time.sleep(0.05)  # Update color at a rate of once per 0.05 second

def get_average_volume():
    total_value = 0
    for _ in range(samples_per_50ms):
        total_value += analog_pin.read()
        time.sleep(sample_interval)
    return total_value // samples_per_50ms

def map_volume_to_color(value, min_value, max_value):
    # Map the value to a range between 0 and 1
    normalized = (value - min_value) / (max_value - min_value)
    normalized = max(0, min(normalized, 1))  # Clamp between 0 and 1

    # Map the normalized value to a color
    r = int((1 - normalized) * 255)
    b = int(normalized * 255)
    return (r, 0, b)


def fade_to_color(current_color, target_color, steps=50, delay=0.005):
    for step in range(1, steps + 1):
        r = int(current_color[0] + (target_color[0] - current_color[0]) * step / steps)
        g = int(current_color[1] + (target_color[1] - current_color[1]) * step / steps)
        b = int(current_color[2] + (target_color[2] - current_color[2]) * step / steps)
        rgb.fill_color(get_color(r, g, b))
        time.sleep(delay)

def get_color(r, g, b):
    # Convert separate r, g, b values to one rgb_color value:
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
