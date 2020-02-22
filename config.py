import pickle
config_map = {
    'Camera Resolution (width)':640,
    'Camera Resolution (height)':480,
    'Camera Rotation': 0,
    'Camera Framerate toggle (yes/no)':'no',
    'Camera Framerate': 25,

    'Camera LED toggle (yes/no)': 'no',
    'Camera LED mode (LED_SINGLE_CHANNEL/LED_RGB)': 0,
    'Camera LED 1st pin': 0,
    'Camera LED 2nd pin': 0,
    'Camera LED 3rd pin': 0,
    
    'Tkinter beta graphics(yes/no)':'yes',
    'Configurated': 0
}
config = open('default.conf','rb')
f = pickle.load(config)
print(f)
print(dir(f))
config.close()
class Config:
    def __init__(self):
        pass
    def Create(self, directory, mode=0):
        pass
    def Open(self, directory):
        pass
    def Return(self):
        pass
    def Write(self,string):
        pass
    def Close(self):
        pass
    def __del__(self):
        pass
        
