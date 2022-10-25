


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
#import src.capture as capture
#import src.detect as detect


doorpin = {
    "plastic": 19,
    "paper": 13,
    "metal": 6,
    "glass": 5,
}
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setwarnings(False)
TEST = True
TEST_MECH = True
# TEST = True


print('\033[92m' + "Garbage detection is currently running......" + '\033[0m')
while True:
    # if GPIO.input(16) == GPIO.HIGH:
    #if input("enter mf") == "":
    if True:
        time.sleep(2)
        #img_path = capture.Capture_Image()
        #print('\033[0;33m' + img_path + '\033[0m')
        if TEST == True:
            img_path = 'images/plastic_detected_works.png'
            # img_path = '/Users/tinapatlimsila/Desktop/Screenshots/Screen Shot 2565-10-23 at 21.11.55.png'
            #garbage_type = detect.run(source=img_path, weights="runs/train/results_3/weights/best.pt")
        else:
            if garbage_type:
                print('\033[0;33m' + garbage_type + '\033[0m')  
            else:
                print('\033[0;33m' + "no object detected" + '\033[0m')  
        if TEST_MECH:
            garbage_type = "plastic"
            garbage_type = input("what type of garbage?: ")
        GPIO.output(doorpin[garbage_type], GPIO.HIGH)
        print("door opening")
        time.sleep(1)
        GPIO.output(doorpin[garbage_type], GPIO.LOW)
    time.sleep(2)
