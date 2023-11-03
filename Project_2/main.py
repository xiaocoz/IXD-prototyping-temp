import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
button_val = None
ball_y_position = 300
circle_size = 20
#I want to have several bubbles which is looping around when each one get to the top
#so I create a list to hold all the values in keys
balls = [
    {"x": 50, "y": 600, "diameter": 20},
    {"x": 115, "y": 320, "diameter": 20},
    {"x": 140, "y": 850, "diameter": 20},
    {"x": 200, "y": 400, "diameter": 20},
    {"x": 100, "y": 480, "diameter": 20},
    {"x": 250, "y": 730, "diameter": 20}]


# # load image data and assign it to variable:
# swirl_img = p5.loadImage('swirl.png')

# # load font data and assign it to variable:
# jellee_font = p5.loadFont('Jellee.otf')

def setup():
  p5.createCanvas(300, 300)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)

def draw():
  global data_string, data_list, circle_size
  global sensor_val, button_val, ball_y_position
   # draw lines responding to button data:
  for i in range(8):
    if(button_val == 0):
      p5.background(255)
    else:
      p5.background(79, 249, 255)
      # draw text:
      p5.fill(255, 234, 0)
      # use font installed on computer:
      p5.textFont('Courier')
      p5.textSize(58)
      p5.text('Ahh!', 95, 160)
      # use font from loaded font file:
      #p5.textFont(jellee_font)
      #p5.textSize(24)
      #p5.text(button_val, 190, 100)


  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign 1st item of data_list to sensor_val:
  sensor_val = int(data_list[0])
  # assign 2nd item of data_list to sensor_val:
  button_val = int(data_list[1])

  p5.noStroke() 

  p5.fill(3, 236, 252) 
  
  for ball in balls:

    p5.ellipse(ball["x"], ball["y"], ball["diameter"], ball["diameter"])
    
    if sensor_val < 6:
        # I want the bubbles to go up faster when the sensor_val is smaller(means when my mouth is closer to the cup)
        rise_speed = (6-sensor_val) / 2
        ball["y"] -= rise_speed
        # i want the bubbles to be bigger while higher
        if ball["y"] <= 300:
            ball["diameter"] += 0.2
    #I want the bubbles to go back to the initial y value, so I reset it:    
    if ball["y"] < 0:
        ball["y"] = 300 + ball["y"]
        ball["diameter"] = 20


