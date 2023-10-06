import os, sys, io
import M5
from M5 import *
from hardware import *


pin1 = None
pin2 = None


i = None


def setup():
  global pin1, pin2, i

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  pin2 = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)


def loop():
  global pin1, pin2, i
  if pin2.value():
    pin1.on()
  else:
    pin1.off()


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
