from machine import Pin
from do_connect import *
from putFile import *
import time

led = Pin("LED", Pin.OUT)

while True:
    do_connect()
    putFile()
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(300)
