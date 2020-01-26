from picamera import PiCamera
from time import sleep
from os import system
from tqdm import tqdm

camera = PiCamera()

class Vars:
    framesDirectory = '/home/pi/Desktop/TimeLapse/Frames'
    currentFrame = 1
    frameSpeed = 5 #Default
    
    previewEnabled = False #Default
    previewAlpha = 200 #Default
    resBottomPX = 1920
    resHeightPX = 1080
    
vars = Vars

class Settings:
    @staticmethod
    def changeFrameSpeed():
        system('clear')
        print("Current Frame Speed | %d" % (vars.frameSpeed))
        print("Set frame speed from 2-540 (seconds)")
        Vars.frameSpeed = int(raw_input("> "))
        settings.settingsMenu()
    
    @staticmethod
    def changeFramesDirectory():
        system('clear')
        print("Current Frame Directory | %s" % (vars.framesDirectory))
        print("Set frame directory to")
        Vars.framesDirectory = str(raw_input('> '))
        settings.settingsMenu()
        
    @staticmethod
    def changePreviewWindow():
        system('clear')
        
        print("Preview Enabled | %s" % (vars.previewEnabled))
        boolean = raw_input('[T/F]> ')
        if boolean == 'T' or boolean == 't':
            vars.previewEnabled = True
        elif boolean == 'F' or boolean == 'f':
            vars.previewEnabled = False
        system('clear')
        
        print("Preview Alpha Level | %s" % (vars.previewAlpha))
        vars.previewAlpha = int(raw_input('[0-255]> '))
        system('clear')
        
        print("Current Resolution | %d x %d" % (vars.resBottomPX, vars.resHeightPX))
        vars.resBottomPX = int(raw_input('{Bottom PX}> '))
        vars.resHeightPX = int(raw_input('{Height PX}> '))
        system('clear')
        
        settings.settingsMenu()
        
    @staticmethod
    def settingsMenu():
        system('clear')
        print("Settings")
        print("--------")
        print("""
Preview Enabled    | %s
Preview Alpha      | %s
Preview Resolution | %s x %s
Frame Speed        | %d
Frame Directory    | %s
""" % (vars.previewEnabled, vars.previewAlpha, vars.resBottomPX, vars.resHeightPX, vars.frameSpeed, vars.framesDirectory))
        print("--------")
        print("""
[1] : Change Frame Speed
[2] : Change Frame Directory
[3] : Preview Window
[4] : Return to Main Menu
""")
        nav = int(raw_input("> "))
        if nav == 1:
            settings.changeFrameSpeed()
        elif nav == 2:
            settings.changeFramesDirectory()
        elif nav == 3:
            settings.changePreviewWindow()
        elif nav == 4:
            Main()
            
settings = Settings
    
    
def takePhoto():
    camera.capture(vars.framesDirectory + "/Frame" + str(vars.currentFrame) + ".jpg")
    vars.currentFrame = vars.currentFrame + 1
    
def startProgram():
    system('clear')
    camera.resolution = (vars.resBottomPX, vars.resHeightPX)
    if vars.previewEnabled:
        camera.start_preview(vars.previewAlpha)
    
    while True:
        system('clear')
        print("Ctrl + C to quit")
        print("Taking Frame : " + str(vars.currentFrame))
        for i in tqdm(range(vars.frameSpeed)):
            sleep(1)
        takePhoto()

def Main():
    system('clear')
    print("--Time Lapse Module--")
    print("V1.0\n")
    print("---------------------")
    print("""
[1] : Settings
[2] : Start Program
""")
    nav = int(raw_input("> "))
    if nav == 1:
        settings.settingsMenu()
    elif nav == 2:
        startProgram()
    else:
        Main()
        
Main()
