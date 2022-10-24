import numpy as np
import cv2
from yaml import load, dump
from yaml.loader import SafeLoader
SAVING_DIRECTORY = "../images/"
def Capture_Image():
    cap = cv2.VideoCapture(0)
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

if __name__ == "__main__":
    Capture_Image()
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