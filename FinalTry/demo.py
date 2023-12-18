import os, sys, io
import M5
from M5 import *
from umqtt import *
from hardware import *


mqtt_client = None


def setup():
  global mqtt_client

  M5.begin()
  mqtt_client = MQTTClient(
      'testclient',
      'io.adafruit.com',
      port=1883,
      user='koko09',
      password='aio_bjLX38gJFRQn4ornm4Sjgvu27187',
      keepalive=0)
  mqtt_client.connect(clean_session=True)


def loop():
  global mqtt_client
  M5.update()
  if BtnA.wasPressed():
    print('button-pressed!')
    mqtt_client.publish('koko09/feeds/button-feed', 'ON', qos=0)
  if BtnA.wasReleased():
    print('button-released!')
    mqtt_client.publish('koko09/feeds/button-feed', 'OFF', qos=0)




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
