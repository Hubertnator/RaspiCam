import RPi.GPIO as GPIO
import tkinter as tk
import time
from camera import *


#--initializing, creating and configuring main window
#### THIS WILL BE IN FUTURE VERSIONS, RIGHT NOW IS IN EXPERIMENTAL FILE gui.py
#--FINISHED SETTING UP WINDOW, Set up GPIO pins & camera

rotated = True; #this will be in a config file.
mp4_command = "MP4Box -add temp.h264 monitoring.mp4"

print("Type in length of video:")
length = int(input())

config = open("general.conf")
print(config.read())

#setting camera diode:
GPIO.setmode(GPIO.BCM)

red = 17
green = 27
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

RED = GPIO.PWM(red, 1)
GREEN = GPIO.PWM(green, 1)
BLUE = GPIO.PWM(blue, 1)

sleep(2)

RED.start(100)
#film from raspberry pi in a for loop

camera = Camera()
camera.Resolution(640,480)
camera.Rotate(180)
camera.Record("temp.h264",length)

#CONVERSION
BLUE.start(60)
conversion_start = time.time()
camera.ConvertVideo("temp.h264","monitoring.mp4")
conversion_stop = time.time()

#Conversion complete, cleanup!

RED.start(0)
GREEN.start(0)
BLUE.start(0)
GPIO.cleanup()


print("Conversion complete, safe to exit program :)")
conversion_time = conversion_stop - conversion_start
print("Conversion took :",conversion_time," seconds")

