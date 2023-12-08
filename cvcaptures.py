from sender import send
import cv2
import random

cap = cv2.VideoCapture(0)

imgpath = "/mnt/c/Users/Taurus/Desktop/raspberrypi/"
letters = "abcdefghijklmnopqrstuvwxyz"

def capture():
    for i in range(30):
        cap.read()
    name = ''.join(random.choice(letters) for _ in range(7))
    ret, frame = cap.read()
    cv2.imwrite(imgpath+name+'.png', frame)   
    cap.release()
    send(imgpath+name+'.png')
    return imgpath+name+'.png'

if __name__ == "__main__":
    print('Ха ха я вас сфотал!!! Любуйтесь тут --> '+capture())
