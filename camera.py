import picamera as picamera
from subprocess import call
from time import ctime, sleep

DEBUG=False

class Camera:
    def __init__(self):
       self.camera = picamera.PiCamera()
    def Framerate(self,frames):
        pass
        #for the future...
    def Resolution(self,x,y):
        self.camera.resolution = (x,y)
    def Rotate(self,deg):
        self.camera.rotation = deg
    def Record(self,filepath,s):
        self.camera.start_recording(filepath)
        print("Started recording - DO NOT CLOSE PROGRAM")
        print("Recording started at: ",ctime())
        sleep(s-0.01)
        self.camera.stop_recording()
        print("RECORDING STOPPED at ",ctime())
    def ConvertVideo(self,file,file_to):
        conversion_command = "MP4Box -add %s %s"
        print("Converting video...")
        call([conversion_command % (file,file_to) ], shell=True)

#debug testing:
if DEBUG==True:
    doodoo = Camera()
    doodoo.Resolution(1280,720)
    doodoo.Rotate(180)
    doodoo.Record("test.h264",0.21)
    doodoo.ConvertVideo("test.h264","converted.mp4")
    print("No errors!")
