import RPi.GPIO as GPIO
import picamera
import tkinter as tk
from subprocess import call
from time import sleep


#--initializing, creating and configuring main window
#### THIS WILL BE IN FUTURE VERSIONS, RIGHT NOW IS IN EXPERIMENTAL FILE gui.py
#--FINISHED SETTING UP WINDOW, Set up GPIO pins & camera

rotated = True; #this will be in a config file.
mp4_command = "MP4Box -add temp.h264 monitoring.mp4"

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

#GREEN.start(100)
RED.start(100)
#film from raspberry pi in a for loop
with picamera.PiCamera() as camera:

    camera.resolution = (1280,720)
    if (rotated == True):
        camera.rotation = 180
    else:
        camera.rotation = 0
    
    print("Started recording")
    camera.start_recording("temp.h264")
    sleep(15)
    camera.stop_recording()
    print("RECORDING STOPPED")
#CONVERSION
print("Converting...")
BLUE.start(60)
call([mp4_command], shell=True)

#Conversion complete, cleanup!

RED.start(0)
GREEN.start(0)
BLUE.start(0)
GPIO.cleanup()
print("Conversion complete, safe to exit program :)")
