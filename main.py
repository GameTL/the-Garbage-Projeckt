
""" 
import capture 
import detect 

loop checking the light gate
    if light gate is triggered
        wait 2 second
        take a picture of the object
        detect(image , model, ) returns the type of garbage
        GPIO[garbage] = HIGH
        wait 5 seconds
"""

print('\033[0;33m' + "importing libraries" + '\033[0m')
# import RPi.GPIO as GPIO
import time
import src.capture as capture
import src.detect as detect


doorpin = {
    "plastic straw": 19,
    "plastic bottle": 19,
    "plastic other": 19,
    "paper": 13,
    "metal can": 6,
    "metal other": 6,
    "glass": 5,
}
""" GATE_SENSOR = 16
LED_LIGHT = 20
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.IN) """
# 1 is testing the AI detection
# 2 is testing the test mechanical to PLC
# 3 is deployment
# 3 testing images are in the images folder

mode = 4
if mode == 4:
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("test/images") if isfile(join("test/images", f))]




print('\033[92m' + "Garbage detection is currently running......" + '\033[0m')
while True:
    if mode == 4:
        for img_path in onlyfiles:
            print(f"test/images/{img_path}")
            garbage_type = detect.run(source=f"test/images/{img_path}", weights="runs/train/results_1/weights/best.pt", name="motherfucker") # change the model as you go
            print('\033[0;33m' + img_path + '\033[0m')
            if garbage_type:
                print('\033[0;33m' + garbage_type + '\033[0m')  
            else:
                print('\033[0;33m' + "no object detected" + '\033[0m') 

    if mode == 1:
        img_path = 'images/plastic_detected_works.png'
        print('\033[0;33m' + img_path + '\033[0m')
    if mode == 2:
        #garbage_type = "plastic"
        garbage_type = input("what type of garbage?: ")
        if garbage_type in ["plastic","paper","glass","metal"]:
            """ GPIO.output(doorpin[garbage_type], GPIO.HIGH)
            print("door opening")
            time.sleep(1)
            GPIO.output(doorpin[garbage_type], GPIO.LOW) """
    if mode == 3:
        if GPIO.input(16) == GPIO.HIGH:
            time.sleep(2)
            img_path = capture.Capture_Image()
            garbage_type = detect.run(source=img_path, weights="runs/train/results_3/weights/best.pt") # change the model as you go
            print('\033[0;33m' + img_path + '\033[0m')
            if garbage_type:
                print('\033[0;33m' + garbage_type + '\033[0m')  
            else:
                print('\033[0;33m' + "no object detected" + '\033[0m') 
    
    if mode == 4:
        quit()

    time.sleep(2)


# img_path = '/Users/tinapatlimsila/Desktop/Screenshots/Screen Shot 2565-10-23 at 21.11.55.png'
