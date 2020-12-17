import RPi.GPIO as GPIO
import tkinter as tk
import time
from camera import *
from cameraled import *


#--initializing, creating and configuring main window
#### THIS WILL BE IN FUTURE VERSIONS, RIGHT NOW IS IN EXPERIMENTAL FILE gui.py
#--FINISHED SETTING UP WINDOW, Set up GPIO pins & camera

rotated = True; #this will be in a config file.
mp4_command = "MP4Box -add temp.h264 monitoring.mp4"

red = 17
green = 27
blue = 22

length = int(input("Type in length of video: "))
while length <= 0:
    print('Invalid duration of video!')
    length = int(input("Type in length of video: "))

config = open("general.conf")
print(config.read())

#setting camera diode:
GPIO.setmode(GPIO.BCM)

led = CameraLED(LED_RGB)
led.Bind(red,green,blue)

GPIO.setup(blue, GPIO.OUT)
BLUE = GPIO.PWM(blue, 1)
 
sleep(2)

#film from raspberry pi in a for loop
led.On(RED)

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
del camera

BLUE.start(0)
GPIO.cleanup()

del led


print("Conversion complete, safe to exit program :)")
conversion_time = conversion_stop - conversion_start
print("Conversion took :",conversion_time," seconds")

