# Raspi-CameraTimeLapse
The camera time lapse module that I have made utilizes many functions of the raspi camera, and takes multiple pictures (specifically frames) that using basic windows 10 photos you can turn into a time lapse.  This module features many settings options for ease of use.
### Set-up
##### !Important! make sure that you enable camera in >Raspberry Pi Configuration>Interfaces
###### 1) Create a new folder and call it whatever you want
###### 2) Download the latest [Raspi-CameraTimeLapse.py](https://github.com/FerisJumbo/Raspi-CameraTimeLapse/releases) file
###### 3) Create an empty folder inside of your one that houses the .py file and call it Frames
###### 4) Launch the program inside of the terminal and navigate to >settings>change directory and set that directory to your Frames folder
###### 5) Start messing around with some of the settings and you can always view what the picture will look like by turning on the preview
----
## Raspi Camera V2.1
The [raspi camera](https://www.amazon.com/Raspberry-Camera-Module-Megapixels-Sensor/dp/B07L82XBNM/ref=asc_df_B07L82XBNM/?tag=hyprod-20&linkCode=df0&hvadid=343234125040&hvpos=1o1&hvnetw=g&hvrand=1389516921892586440&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019614&hvtargid=pla-717544328579&psc=1&tag=&ref=&adgrpid=68968886317&hvpone=&hvptwo=&hvadid=343234125040&hvpos=1o1&hvnetw=g&hvrand=1389516921892586440&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9019614&hvtargid=pla-717544328579) is a simple yet very thought out piece of technology that allows the user to take pictures or videos with.
The documentation that I found to work the best for me is [here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
### Methods inside of the camera
First you need to import the camera and initialize it.
```python
from picamera import PiCamera

camera = PiCamera()
```
In order to turn on and off the preview.
```python
camera.start_preview()

camera.stop_preview()
```
In order to take a picture you have to define a path and give it a name with a .jpg extension
```python
#               Name of picture to save as \/
fileDirectory = '/home/pi/Downloads/Frames/F1.jpg'

camera.capture(fileDirectory)
```
The camera has many more customizable attributes like resolution, effects, and annotated text.
The resoulution defaults to 1920 x 1080 but can be changed all the way up to 2592 x 1944
```python
camera.resolution = (2592, 1944)

# If camera is set to the max resolution you have to give it a frame rate of 15
camera.framerate = 15
```
You can also add text to your photos/videos with a sizes ranging from 6 to 160 default 32
```python
camera.annotate_text = 'Look at me!'

camera.annotate_text_size = 100
```
The text can also be colored diffrently
```python
from picamera import PiCamera, Color

camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
```

There are even more cool things that you can do with it that is better explained [here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8)
