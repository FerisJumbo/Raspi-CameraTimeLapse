from picamera import PiCamera
from time import sleep
from os import system
from tqdm import tqdm

camera = PiCamera()

class Vars:
    framesDirectory = '/home/pi/Desktop/Raspi-CameraTimeLapse-master/Frames'
    currentFrame = 1
    frameSpeed = 5 #Default
    
    currentRotation = 0
    rotatingAngles = [0, 90, 180, 270]
    
    imageEffect = 'none'
    imageEffects = []
    
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
        
        print('Press Enter to end Preview')
        sleep(3)
        camera.start_preview()
        raw_input('> ')
        
        camera.stop_preview()
        
        settings.settingsMenu()
    
    @staticmethod
    def rotateImage():
        system('clear')
        print('Current Rotation : %d' % (vars.currentRotation))
        for i in range(len(vars.rotatingAngles)):
            print('[%d] : %d Degrees' % (i + 1, vars.rotatingAngles[i]))
        nav = int(raw_input('> '))
        vars.currentRotation = vars.rotatingAngles[nav - 1]
        settings.settingsMenu()
        
    @staticmethod
    def changeImageEffect():
        system("clear")
        print("Current Effect : " + vars.imageEffect)
        for i in range(len(vars.imageEffects)):
            print("[%d] : %s" % (i + 1, vars.imageEffects[i]))
        nav = int(raw_input('> '))
        vars.imageEffect = vars.imageEffects[nav - 1]
        settings.settingsMenu()
        
    @staticmethod
    def settingsMenu():
        camera.resolution = (vars.resBottomPX, vars.resHeightPX)
        camera.rotation = vars.currentRotation
        camera.image_effect = vars.imageEffect
        system('clear')
        print("Settings")
        print("\n--------")
        print("""
Resolution         | %s x %s
Rotation           | %d Degrees
Image Effect       | %s
Frame Speed        | %d
Frame Directory    | %s
""" % (vars.resBottomPX, vars.resHeightPX, vars.currentRotation, vars.imageEffect, vars.frameSpeed, vars.framesDirectory))
        print("--------")
        print("""
[1] : Change Frame Speed
[2] : Change Frame Directory
[3] : Change Image Effect
[4] : Rotate Image
[5] : Preview Window

[6] : Return to Main Menu
""")
        nav = int(raw_input("> "))
        if nav == 1:
            settings.changeFrameSpeed()
        elif nav == 2:
            settings.changeFramesDirectory()
        elif nav == 3:
            settings.changeImageEffect()
        elif nav == 4:
            settings.rotateImage()
        elif nav == 5:
            settings.changePreviewWindow()
        elif nav == 6:
            Main()
        else:
            settings.settingsMenu()
            
settings = Settings
    
    
def takePhoto():
    camera.capture(vars.framesDirectory + "/Frame" + str(vars.currentFrame) + ".jpg")
    vars.currentFrame = vars.currentFrame + 1
    
def startProgram():
    system('clear')
    camera.resolution = (vars.resBottomPX, vars.resHeightPX)
    camera.rotation = vars.currentRotation
    camera.image_effect = vars.imageEffect
    
    try:
        while True:
            system('clear')
            print("Ctrl + C to quit")
            print("Taking Frame : " + str(vars.currentFrame))
            for i in tqdm(range(vars.frameSpeed)):
                sleep(1)
            takePhoto()
    except:
        system('clear')
        print("Taken %d frames" % (vars.currentFrame - 1))
        vars.currentFrame = 1
        sleep(2)
        Main()

def Main():
    system('clear')
    print("--/Time Lapse Module\--")
    print("     __/V1.1\\__\n")
    print("---------------------")
    print("""
[1] : Settings
[2] : Start Program

[3] : Exit
""")
    nav = int(raw_input("> "))
    if nav == 1:
        settings.settingsMenu()
    elif nav == 2:
        startProgram()
    elif nav == 3:
        system('clear')
    else:
        Main()
        

for i in camera.IMAGE_EFFECTS:
    vars.imageEffects.append(i)
Main()
