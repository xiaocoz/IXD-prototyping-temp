import os, sys, io
import M5
from M5 import *
from hardware import *
import time
from driver.neopixel import NeoPixel


rgb = None
state = 'START'
state_timer = 0
np = None


rainbow = [
    (255, 255, 0), (255, 236, 0), (255, 217, 0), (255, 198, 0),
    (255, 179, 0), (255, 160, 0), (255, 141, 0), (255, 122, 0),
    (255, 103, 0), (255, 84, 0), (255, 65, 0), (255, 46, 0)
]



def setup():
  global rgb, input_pin, np, state
  M5.begin()
  state = 'START'

  input_pin = Pin(41, mode=Pin.IN, pull=Pin.PULL_UP)
  np = NeoPixel(pin=Pin(2), n=12)
  
  if (state == 'START'):
    print('start..')
    time.sleep(2)
    for i in range(12):
        np[i] = (255, 140, 0) 
    np.write()
    time.sleep(1)  

    for i in range(12):
        np[i] = (0, 0, 0) 
    np.write()
    
    check_input()


def loop():
  global rgb, state, state_timer, np, rainbow
  M5.update()
  rgb = RGB(io=35, n=1, type="SK6812")
  rainbow = rainbow[-1:] + rainbow[:-1]
  
  
      
  if (state == 'OPEN'):
    print('open')
    time.sleep(1) 
    check_input()
    
   
    
  elif (state == 'CLOSED'):
    if(time.ticks_ms() < state_timer + 1000):
      print('close')
      for i in range(12):
        np[i] = rainbow[i]
        np.write()
        time.sleep_ms(50)
      
    elif(time.ticks_ms() > state_timer + 10000):
      state = 'FINISH'
      print('change to', state)
      state_timer = time.ticks_ms()
      
  elif (state == 'FINISH'):
    print('finish')
    for i in range(12):
        np[i] = (0, 0, 0)
    np.write()
    time.sleep(3)
    check_input()


def check_input():
  global state, state_timer
  if (input_pin.value() == 0):
    if(state != 'CLOSED'):
      print('change to CLOSED')
    state = 'CLOSED'
    state_timer = time.ticks_ms()
  else:
    if(state != 'OPEN'):
      print('change to OPEN')
    state = 'OPEN'
    
    
    
def get_color(r, g, b):
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
      
       