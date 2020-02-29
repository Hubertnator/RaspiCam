import RPi.GPIO as GPIO
LED_SINGLE_CHANNEL = "4fbc5e3c9838c7427e1bceba6bf61e52"
LED_RGB = "31b5b427135c4c95ef5c1467964b0a61"
# ALL = 5
COMPAT = 0
SINGLE = 1
RED = 2
GREEN = 3
BLUE = 4
#DUMMY GPIO CLASS
if COMPAT==True:
    class GPIO:
        LOW = 0
        HIGH = 1
        def __init__(self):
            pass
        def output(a,b):
            pass
        def cleanup():
            pass

class CameraLED:
    def __init__(self,led_type):
        GPIO.setmode(GPIO.BCM)
        self.on = False
        self.mode = 0
        
        if(led_type == LED_SINGLE_CHANNEL):
            self.type = LED_SINGLE_CHANNEL
            self.color_pin = 0
        elif(led_type == LED_RGB):               
            self.type = LED_RGB
            self.red_pin = 0
            self.green_pin = 0
            self.blue_pin = 0
        else:
            print("Error #1. Initializing cameraLED failed - Unknown LED type")
    def CleanUp(self):
        pass
    def Bind_SINGLE_CHANNEL(self,plus):
        self.color_pin = plus
        print(self.type,"  is bound")
        
    def Bind_RGB(self,r,g,b):
        self.red_pin = r
        self.green_pin = g
        self.blue_pin = b
        print(self.type,"  is bound outaside")
        
    def Bind(self,r,g=0,b=0):
        if(self.type == LED_SINGLE_CHANNEL):
            self.Bind_SINGLE_CHANNEL(r)
        elif(self.type == LED_RGB):
            self.Bind_RGB(r,g,b)
        else:
            print("Error #3 Function Bind() does not accept given argument!")
    def On(self, mode):
        if(mode == 1):
            GPIO.output(self.color_pin,GPIO.HIGH)
        elif(mode == 2):
            GPIO.output(self.red_pin,GPIO.HIGH)
            print("Red Channel on")
        elif(mode == 3):
            GPIO.output(self.green_pin,GPIO.HIGH)
        elif(mode == 4):
            GPIO.output(self.blue_pin,GPIO.HIGH)
        else:
            print("Error #2 Function On() does not accept given argument")

    def Off(self, mode):
        if(mode == 1):
            GPIO.output(self.color_pin,GPIO.LOW)
        elif(mode == 2):
            GPIO.output(self.red_pin,GPIO.LOW)
            print("Red Channel off")
        elif(mode == 3):
            GPIO.output(self.green_pin,GPIO.LOW)
            print("Green Channel off")
        elif(mode == 4):
            GPIO.output(self.blue_pin,GPIO.LOW)
            print("Blue Channel off")
        else:
            print("Error #4 Function Off() does not accept given argument")

    def __del__(self):
        GPIO.cleanup()
        print("CameraLED object deleted")
    def Unbind(self):
        if(self.type == LED_SINGLE_CHANNEL):
            GPIO.output(self.color_pin,GPIO.LOW)
            del self.gnd, self.color_pin
        elif(self.type == LED_RGB):
            GPIO.output(self.red_pin,GPIO.LOW)
            GPIO.output(self.green_pin,GPIO.LOW)
            GPIO.output(self.blue_pin,GPIO.LOW)
            del self.gnd, self.red_pin, self.green_pin, self.blue_pin
        else:
            print("Error #5 Function Unbind() does not accept given argument!")
        

led = CameraLED(LED_RGB)
led.Bind(20,20)
led.On(RED)
led.Unbind()
led.CleanUp()
del led

