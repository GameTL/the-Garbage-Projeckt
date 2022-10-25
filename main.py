
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
    "plastic": 11,
    "paper": 12,
    "metal": 13,
    "glass": 15,
}
GATE_SENSOR = 16
LED_LIGHT = 20

TEST = False
# TEST = True


print('\033[92m' + "Garbage detection is currently running......" + '\033[0m')
while True:
    # if GPIO.input(GATE_SENSOR) == GPIO.HIGH:
    if input("enter to continue") == "": # for testing
        print("light gate triggered")
        # GPIO.output(LED_LIGHT, GPIO.HIGH)
        time.sleep(2)
        img_path = capture.Capture_Image()
        print('\033[0;33m' + img_path + '\033[0m')
        if TEST == True:
            img_path = 'images/plastic_detected_works.png'
            # img_path = '/Users/tinapatlimsila/Desktop/Screenshots/Screen Shot 2565-10-23 at 21.11.55.png'
        garbage_type = detect.run(source=img_path, weights="runs/train/results_3/weights/best.pt")
        if garbage_type:
            print('\033[0;33m' + garbage_type + '\033[0m')  
        else:
            print('\033[0;33m' + "no object detected" + '\033[0m')  

        # GPIO.output(doorpin[garbage_type], GPIO.HIGH)
        time.sleep(1)
        # GPIO.output(doorpin[garbage_type], GPIO.LOW)
    time.sleep(1)
