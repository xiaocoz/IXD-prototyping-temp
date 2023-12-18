import js as p5
from js import document
import random

data_string = None
data_list = None
sensor_value = None  # Store the most recent sensor value
red_circles = []  # Declare red_circles as a global variable

def setup():
    p5.createCanvas(1520, 1000)
    p5.frameRate(100)  # Set the frame rate to 100 frames per second for smoother animation

def draw():
    global data_string, data_list
    global sensor_value
    global red_circles  # Use the global keyword to access the global variable

    data_string = document.getElementById("data").innerText
    # Split data_string by comma, making a list:
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
            fill_color = p5.color(255, 0, 0, opacity)  # Solid red color with varying opacity
            p5.fill(fill_color)
            p5.noStroke()
            p5.ellipse(x, y, size - i * 10, size - i * 10)

        updated_red_circles.append((x, y, size, opacity, hue))

    red_circles = updated_red_circles  # Update the red_circles list