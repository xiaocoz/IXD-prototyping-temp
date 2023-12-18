import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
circle_size = 20

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
    global sensor_val

    data_string = document.getElementById("data").innerText
    # 我们假设数据字符串的格式是 "mic_total_volume = <number>"
    # 先分割字符串，然后提取 <number> 部分
    try:
        sensor_val_str = data_string.split('=')[1].strip()
        sensor_val = int(sensor_val_str)
    except (IndexError, ValueError) as e:
        # print("Error parsing sensor value:", e)
        sensor_val = 0  # 或者设置为默认值

    p5.background(255)
    p5.fill(100, 100, 255)

    # 圆的大小由 sensor_val 控制
    circle_size = map_value(sensor_val, 1800, 2100, 40, 10)
    p5.ellipse(150, 150, circle_size, circle_size) 
    
    print(circle_size)

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


