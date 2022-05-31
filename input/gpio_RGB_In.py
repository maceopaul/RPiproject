import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

Red= 11
Green= 13
Blue= 15
Switch= 37

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)

def RGB_clear():
    GPIO.output(Red , GPIO.LOW)
    GPIO.output(Green , GPIO.LOW)
    GPIO.output(Blue, GPIO.LOW)

count= 0
while True: 
    # GPIO.input(Switch)와 GPIO.HIGH를 AND 연산으로 변경 가능
    if (GPIO.input(Switch) == GPIO.LOW and count== 0):
        print("Red LED is On!")
        RGB_clear()
        GPIO.output(Red, GPIO.HIGH)
        count+=1
        print(count)
    elif(GPIO.input(Switch) == GPIO.LOW and count== 1):
        print("Green LED is ON!")        
        RGB_clear()
        GPIO.output(Green, GPIO.HIGH)
        count+=1
        print(count)
    elif(GPIO.input(Switch) == GPIO.LOW and count== 2):
        print("Blue LED is ON!")
        RGB_clear()
        GPIO.output(Blue, GPIO.HIGH)
        count+= 1
        print(count)
    elif(GPIO.input(Switch) == GPIO.LOW and count== 3):
        RGB_clear()
        count= 0
        print(count)
    time.sleep(1)
