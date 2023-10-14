import os, sys, io
import M5
from M5 import *
from hardware import *
import time

pwm1 = None
pin1 = None
pin2 = None
state = 'awake'
i = None


def setup():
  global pin1, pin2, i, state, pwm1, rgb

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  pin2 = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
  # initialize M5 board:
  M5.begin()
  # initialize PWM on pin 1 with default settings:
  pwm1 = PWM(Pin(1))
  rgb = RGB()

def loop():
  global pin1, pin2, i, state, pwm1, rgb
  
  if (state == 'awake'):
      #pin1.on()
      print('awake')
      rgb.fill_color(0xffff00)
      pwm1.duty(500)
      time.sleep_ms(1000)
      if not pin2.value():
        state = 'scare'
        
  elif (state == 'scare'):
        rgb.fill_color(0xff0000)
        #M5.update()
        print('scare')
        for i in range(100):
        # change the PWM duty cycle (pulse width) 
        # with increasing value of loop variable i:
          pwm1.duty(i)
          time.sleep_ms(10)
        # gradually decrease led brightness in a loop:
        for i in range(100):
        # change the PWM duty cycle (pulse width)
        # with decreasing value of 100 - i: 
          pwm1.duty(100 - i)
          time.sleep_ms(10)
        if not pin2.value():
          pin1.off()
          state = 'sleep'
          time.sleep_ms(100)
          
  elif (state == 'sleep'):
      print('sleep')
      pin1.off()
      rgb.fill_color(0x6600cc)
      time.sleep_ms(500)
      if not pin2.value():
        state = 'awake'
        time.sleep_ms(500)
      


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
