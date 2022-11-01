
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

# 19 == 4
# 13 == 3
# 6 == 2
# 5 == 1
FIRST = 5
SECOND = 6
THIRD = 13
FORTH = 19
GPIO_OUT = [FIRST,SECOND,THIRD,FORTH]

doorpin = {
    "plastic straw": THIRD,
    "plastic bottle": THIRD,
    "plastic other": THIRD,
    "paper": FORTH,
    "metal can": SECOND,
    "metal other": SECOND,
    "glass": FIRST,
}
GATE_SENSOR = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GATE_SENSOR, GPIO.IN)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.IN)
# 1 is testing the AI detection
# 2 is testing the test mechanical to PLC
# 3 is deployment
#  testing images are in the images folder

def allLOW():
    for pin in GPIO_OUT:
        GPIO.output(pin, GPIO.LOW)
        
def isInserted():
    if GPIO.input(16) == GPIO.HIGH:
        while GPIO.input(16) == GPIO.HIGH:
            sleep(0.1)
        return True
    return False
    pass

allLOW()
mode = 5
if mode == 4:
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("test/images") if isfile(join("test/images", f))]




print('\033[92m' + "Garbage detection is currently running......" + '\033[0m')
while True:
    allLOW()
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
        print("insert a object")
        if GPIO.input(16) == GPIO.HIGH:
        #['plastic straw', 'plastic bottle', 'plastic other', 'paper', 'metal can', 'metal other', 'glass']
            garbage_type = 'metal can'
            #garbage_type = input("what type of garbage?: ")
            if garbage_type in ['plastic straw', 'plastic bottle', 'plastic other', 'paper', 'metal can', 'metal other', 'glass']:
                GPIO.output(doorpin[garbage_type], GPIO.HIGH)
                print("door opening") 
                time.sleep(1)
                GPIO.output(doorpin[garbage_type], GPIO.LOW)
                print("signal off")
    if mode == 5:
        input("ternter mf")
        #['plastic straw', 'plastic bottle', 'plastic other', 'paper', 'metal can', 'metal other', 'glass']
        garbage_type = 'metal can'
            #garbage_type = input("what type of garbage?: ")
        if garbage_type in ['plastic straw', 'plastic bottle', 'plastic other', 'paper', 'metal can', 'metal other', 'glass']:
            GPIO.output(doorpin[garbage_type], GPIO.HIGH)
            print("door opening") 
            time.sleep(1)
            GPIO.output(doorpin[garbage_type], GPIO.LOW)
            print("signal off")
    if mode == 3:
        # if isInserted == True: replacing the next statement
        if GPIO.input(16) == GPIO.HIGH:
            time.sleep(2)
            img_path = capture.Capture_Image()
            garbage_type = detect.run(source=img_path, weights="runs/train/results_1/weights/best.pt") # change the model as you go
            print('\033[0;33m' + img_path + '\033[0m')
            if garbage_type:
                print('\033[0;33m' + garbage_type + '\033[0m')  
            else:
                print('\033[0;33m' + "no object detected" + '\033[0m')
            if garbage_type in ['plastic straw', 'plastic bottle', 'plastic other', 'paper', 'metal can', 'metal other', 'glass']:
                GPIO.output(doorpin[garbage_type], GPIO.HIGH)
                print("door opening")
                time.sleep(1)
                GPIO.output(doorpin[garbage_type], GPIO.LOW)
                print("signal off")
    
    if mode == 4:
        quit()

    #time.sleep(6)


# img_path = '/Users/tinapatlimsila/Desktop/Screenshots/Screen Shot 2565-10-23 at 21.11.55.png'
