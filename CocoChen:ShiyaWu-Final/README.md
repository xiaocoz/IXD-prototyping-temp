# The Empathy Pipe 
Video: 
![Slide 16_9 - 2](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/b59d2381-00bb-4653-a589-db1fe8b9d252)

### Introduction
Our project is an exploration of the evolution of communication, starting from the basic string telephone to the modern digital era. We delved into the idea of transcending auditory communication by converting sound into visual representation. Initially, we were intrigued by the potential of using a light strip to visually express sound volumes captured by a microphone; this formed the foundation of our concept. As our research progressed, we found a profound connection between our concept and the theme of cyberbullying - a scenario where victims often face a barrage of silent yet echoing written abuse. We hypothesized that the principle of karma is relevant in such contexts, where the negative actions directed at others could eventually reverberate back to the abuser. Thus, we incorporated a dynamic visual effect using p5.js, which visually amplifies the spoken attacks by increasing the number and size of red dots projected onto the abuser, correlating with the volume of their speech.
![Slide 16_9 - 4](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/2f0f23f7-f561-4003-baec-0e2fb419e354)
![Slide 16_9 - 6](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/86d60768-ae29-4a6b-83fe-06e70b03dda2)


### Hardware
For our project, we utilized the following hardware components:

- AtomS3 Lite ESP32S3 Dev Kit: This development kit served as the brain of our project, processing the input from the microphone and controlling the LED strip's color changes.
- Microphone Unit (LM393): This sensor detected the sound levels, allowing us to translate volume into visual data.
- Digital RGB LED Weatherproof Strip SK6812: The LED strip provided visual feedback, changing colors based on the sound input to represent the varying intensities of cyberbullying.

### Firmware (MicroPython Code)
Running in the background via Thonny, our MicroPython firmware was crucial for interpreting the sound levels from the microphone and manipulating the LED strip's colors to create a gradient effect. The code continuously sampled the microphone's input and calculated an average volume, which was then used to adjust the LED colors, representing the harshness of spoken words.
````
import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb = None
analog_pin = None
sample_interval = 0.01 
samples_per_50ms = 20 
current_color = (0, 0, 0) 

def setup():
    global rgb, analog_pin
    M5.begin()

    # Initialize RGB LED:
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
    normalized = max(0, min(normalized, 1))  

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

````

### Software
Using p5.js, we created a series of red dots that appeared in tandem with the volume of the sound. The louder the sound, the larger and more numerous the dots became, gradually fading in transparency to signify the karmic return of the abuser's actions.
````
import js as p5
from js import document
import random

data_string = None
data_list = None
sensor_value = None  
red_circles = [] 

def setup():
    p5.createCanvas(1520, 1000)
    p5.frameRate(100)  # Set the frame rate to 100 frames per second for smoother animation

def draw():
    global data_string, data_list
    global sensor_value
    global red_circles  

    data_string = document.getElementById("data").innerText
    data_list = data_string.split(',')
    
    sensor_val = int(data_list[0])
    sensor_value = sensor_val  # Store the most recent sensor value

    # Calculate circle size based on the most recent sensor value
    if 1800 <= sensor_value <= 2100:
        circle_size = p5.map(sensor_value, 2070, 1950, 40, 400)  # Map sensor_value to circle size
        x_pos = random.randint(0, p5.width)  # Random X position
        y_pos = random.randint(0, p5.height)  # Random Y position
        red_circles.append((x_pos, y_pos, circle_size, 255, p5.random(360)))  # Add the circle with opacity 255 and a random hue

    # Update and draw all the red circles
    p5.background(0)
    updated_red_circles = []
    
    for circle_data in red_circles:
        x, y, size, opacity, hue = circle_data

        # Decrease opacity
        opacity -= 2
        if opacity < 0:
            continue  # Skip drawing if opacity is less than 0
        
        # Draw colorful circles with gradients
        for i in range(5):
            fill_color = p5.color(255, 0, 0, opacity)
            p5.fill(fill_color)
            p5.noStroke()
            p5.ellipse(x, y, size - i * 10, size - i * 10)

        updated_red_circles.append((x, y, size, opacity, hue))

    red_circles = updated_red_circles 
````

### Enclosure / Mechanical Design
We crafted the main structure from interconnected pipes, with funnels acting as the ends of our 'telephone.' Translucent paper encased the ends to conceal the hardware and drilled holes in the pipe base allowed for cable management. A projector directed toward the abuser displayed the dynamic visual effects on a wall behind them.


### Project Outcome
To enhance the visual impact of our project, we opted to turn off ambient lighting. This heightened the contrast of the color changes in the physical part and the projections on the abuser.
![Slide 16_9 - 7](https://github.com/xiaocoz/IXD-prototyping-temp/assets/137859417/27f476ff-2913-493f-8c5f-b8c143553a7d)


### Conclusion
Our project, a collaboration between myself and Shiya, was a study in efficient teamwork and innovative thinking. From the outset, we divided our tasks based on our strengths, which significantly boosted our productivity. During our brainstorming sessions, we toyed with the idea of integrating IFTTT to embody the concept of karma — for instance, sending an email to the 'abuser' when loud sounds were detected, simulating the backlash effect of cyberbullying. However, we later decided to pivot from this approach in favor of using graphic projections. This not only circumvented the need to collect email addresses from the audience but also provided immediate, visually impactful feedback, thereby enhancing the project's cohesiveness and elegance.

Throughout the development process, we encountered several challenges. Initially, we envisioned a more complex assembly using longer pipes, but we faced limitations with the LED strip. We discovered that connecting more than 90 LEDs triggered errors in Thonny, forcing us to simplify our design to ensure the smooth functioning of the device. Another challenge was finding the right volume range for the audio input to effectively translate into our desired visual spectrum of small, medium, and large impacts.

Despite these hurdles, the project was a rewarding experience. One such piece of advice was the suggestion to use a mini projector hidden at one end of the pipe, aimed directly at the 'abuser' side. This recommendation was particularly valuable as it eliminated the need for a connected computer, further streamlining and refining our project's design.
