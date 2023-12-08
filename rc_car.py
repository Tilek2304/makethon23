import bluetooth
import time
import RPi.GPIO as GPIO

ml1=18
ml12 = 2
ml2=23
ml22 = 3
mr1=24
mr12 = 4
mr2=25
mr22 = 5

#____________________________________________________________________________________________________________________

def gpiosetup():
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(ml1, GPIO.OUT)
   GPIO.setup(ml2, GPIO.OUT)
   GPIO.setup(mr1, GPIO.OUT)
   GPIO.setup(mr2, GPIO.OUT)
   GPIO.setup(ml12, GPIO.OUT)
   GPIO.setup(ml22, GPIO.OUT)
   GPIO.setup(mr12, GPIO.OUT)
   GPIO.setup(mr22, GPIO.OUT)
   GPIO.output(ml1 , 0)
   GPIO.output(ml12 , 0)
   GPIO.output(mr1 , 0)
   GPIO.output(mr12 , 0)
   GPIO.output(ml2 , 0)
   GPIO.output(ml22 , 0)
   GPIO.output(mr2, 0)
   GPIO.output(mr22, 0)

#___________________________________________________________________________________________________________________________

def left_side_forward():
    print("FORWARD LEFT")
    GPIO.output(ml1 , 0)
    GPIO.output(ml2 , 1)
    GPIO.output(ml12 , 0)
    GPIO.output(ml22 , 1)
    GPIO.output(mr1 , 1)
    GPIO.output(mr2 , 0)
    GPIO.output(mr12 , 1)
    GPIO.output(mr22 , 0)

def right_side_forward():
    print("FORWARD RIGHT")
    GPIO.output(ml1 , 1)
    GPIO.output(ml2 , 0)
    GPIO.output(ml12 , 1)
    GPIO.output(ml22 , 0)
    GPIO.output(mr1 , 0)
    GPIO.output(mr2 , 1)
    GPIO.output(mr12 , 0)
    GPIO.output(mr22 , 1)

def forward():
    print("FORWARD")
    GPIO.output(ml1 , 1)
    GPIO.output(ml2 , 0)
    GPIO.output(ml12 , 1)
    GPIO.output(ml22 , 0)
    GPIO.output(mr1 , 1)
    GPIO.output(mr2 , 0)
    GPIO.output(mr12 , 1)
    GPIO.output(mr22 , 0)

def stop():
    print("STOP")
    GPIO.output(ml1 , 0)
    GPIO.output(ml2 , 0)
    GPIO.output(ml12 , 0)
    GPIO.output(ml22 , 0)
    GPIO.output(mr1 , 0)
    GPIO.output(mr2 , 0)
    GPIO.output(mr12 , 0)
    GPIO.output(mr22 , 0)

#_______________________________________________________________________________________________________-

if __name__ == "__main__":
   server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
   port = 1
   server_socket.bind(("",port))
   server_socket.listen(1)
   client_socket,address = server_socket.accept()
   print("Accepted connection from ",address)
   data=""

   gpiosetup()

   while 1:
      data= client_socket.recv(1024)
      print("Received: %s" % data)
      if (data == "F"):    
         forward()
      elif (data == "L"):    
         left_side_forward()
      elif (data == "R"):    
         right_side_forward()
      elif (data == "B"):    
         stop()
      elif (data == "Q"):
         print ("Quit")
      break


   client_socket.close()
   server_socket.close()
