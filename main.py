import RPi.GPIO as GPIO
import picamera
import tkinter as tk
import time
from subprocess import call
from time import sleep

#--initializing, creating and configuring main window
#### THIS WILL BE IN FUTURE VERSIONS, RIGHT NOW IS IN EXPERIMENTAL FILE gui.py
#--FINISHED SETTING UP WINDOW, Set up GPIO pins & camera

rotated = True; #this will be in a config file.
mp4_command = "MP4Box -add temp.h264 monitoring.mp4"
length = input()

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
GREEN = GPIO.PWM(green, 100)
BLUE = GPIO.PWM(blue, 1)

sleep(2)

RED.start(100)
#film from raspberry pi in a for loop
with picamera.PiCamera() as camera:

    camera.resolution = (640,480)
    if (rotated == True):
        camera.rotation = 180
    else:
        camera.rotation = 0
    
    print("Started recording - DO NOT CLOSE PROGRAM")
    camera.start_recording("temp.h264")
    sleep(600)
    camera.stop_recording()
    print("RECORDING STOPPED")
#CONVERSION
print("Converting...")
BLUE.start(60)
conversion_start = time.time()

call([mp4_command], shell=True)
conversion_stop = time.time()
#Conversion complete, cleanup!

RED.start(0)
GREEN.start(0)
BLUE.start(0)
GPIO.cleanup()


print("Conversion complete, safe to exit program :)")
conversion_time = conversion_stop - conversion_start
print("Conversion took :",conversion_time," seconds")

