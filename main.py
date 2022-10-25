


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
import RPi.GPIO as GPIO
import time
import src.capture as capture
import src.detect as detect


doorpin = {
    "plastic": 19,
    "paper": 13,
    "metal": 6,
    "glass": 5,
}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.IN)
# 1 is testing the AI detection
# 2 is testing the test mechanical to PLC
# 3 is deployment

mode = 1


print('\033[92m' + "Garbage detection is currently running......" + '\033[0m')
while True:
    if mode == 1:
        img_path = 'images/plastic_detected_works.png'
        print('\033[0;33m' + img_path + '\033[0m')
    if mode == 2:
        #garbage_type = "plastic"
        garbage_type = input("what type of garbage?: ")
        if garbage_type in ["plastic","paper","glass","metal"]:
            GPIO.output(doorpin[garbage_type], GPIO.HIGH)
            print("door opening")
            time.sleep(1)
            GPIO.output(doorpin[garbage_type], GPIO.LOW)
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
    time.sleep(2)


# img_path = '/Users/tinapatlimsila/Desktop/Screenshots/Screen Shot 2565-10-23 at 21.11.55.png'
