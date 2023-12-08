from picamera import PiCamera
from time import sleep
from sender import send
import random

imgpath = "~/"
letters = "abcdefghijklmnopqrstuvwxyz"

camera = PiCamera()

def capture():
    camera.start_preview()
    sleep(2)
    name = ''.join(random.choice(letters) for _ in range(7))
    camera.capture(imgpath+name+'.jpg')
    camera.stop_preview()
    send(imgpath+name+'.jpg')
    return imgpath+name 

if __name__ == "__main__":
    print("я вас сфотал, она хранится тут: "+capture()+'.jpg')

