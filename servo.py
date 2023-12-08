# программа поворота сервопривода по терминалу
# принимает 3 параметра:
# 	пин сервака
# 	угол на который нужно повернуть
# Пример: python3 servo.py 12 90 0.3 (не обязательный аргумент по умолчанию 0.3)
# где 12 - пин
#     90 - градус
# 	  0,3 - задержка после импульса, чем выше, тем дольше будет задержка между 
#			заданными углами, это самая быстрая скорость

# 180 градусов - крайнее правое положение камеры
# 0 градусов - крайнее левое положение камеры

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setServoAngle(servo, angle, delay):
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(delay)
	pwm.stop()

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 2: 
		delay = 0.3
	elif len(sys.argv) == 3:
		delay = sys.argv[3]
	
	servo = int(sys.argv[1])
	GPIO.setup(servo, GPIO.OUT)
	setServoAngle(servo, int(sys.argv[2]), delay)
	GPIO.cleanup()

