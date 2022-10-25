import numpy as np
import cv2
from yaml import load, dump
from yaml.loader import SafeLoader
SAVING_DIRECTORY = "../images/"
def Capture_Image():
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('`'):
    #     break 
    with open("config.yml") as f:
        data = load(f, Loader=SafeLoader)
        data['image_counter'] += 1
        outputName = f"images/testing{data['image_counter']}.png"
        print(outputName)
        print(data)
    with open("config.yml", "w") as f:
        dump(data, f)
        cv2.imwrite(outputName,frame)
        cv2.destroyAllWindows() 
    cap.release()
    cv2.destroyAllWindows()
    return outputName

def ContinousCapture():
    import cv2

    [CAMERA_PORT,X_RESOLUTION, Y_RESOLUTION, VIDEO_FPS] = [0, 1280, 720, 30]
    cap = cv2.VideoCapture(CAMERA_PORT)  # ! change the webcam device
    cap.set(3, X_RESOLUTION)
    cap.set(4, Y_RESOLUTION)
    cap.set(5, VIDEO_FPS)
    # cap.set(3, 600)
    # cap.set(4, 600)

    print('\033[92m' + "ContinousCapture is currently running......" + '\033[0m')
    while True:
        success, img = cap.read()
        # img = cv2.flip(img, 1)
        cv2.imshow("Image", img)
        pressedKey = cv2.waitKey(1) & 0xFF
        if pressedKey == ord(' '):
            with open("config.yml") as f:
                data = load(f, Loader=SafeLoader)
                data['image_counter'] += 1
                outputName = f"images_{RUN}/testing{data['image_counter']}.png"
                print(outputName)
                print(data)
            with open("config.yml", "w") as f:
                dump(data, f)
                cv2.imwrite(outputName,img)
                cv2.destroyAllWindows() 
        elif pressedKey == ord('q'):
            print('\033[92m' + "ContinousCapture is quitting......" + '\033[0m')
            break

    cap.release()
    cv2.destroyAllWindows()

mode = 2
RUN = "25OCT"
if __name__ == "__main__":
    if mode == 1:
        Capture_Image()
    elif mode == 2:
        ContinousCapture()
""" 
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('`'):
    #     break 
    if cv2.waitKey(1) & 0xFF == ord('y'):
        with open("config.yml") as f:
            data = load(f, Loader=SafeLoader)
            outputName = f"images/testimg{data['image_counter']}.png"
            print(outputName)
            data['image_counter'] += 1
            print(data)
        with open("config.yml", "w") as f:
            dump(data, f)
            


        cv2.imwrite(outputName,frame)
        cv2.destroyAllWindows()
        break

    
cap.release()
cv2.destroyAllWindows()
quit()
 """