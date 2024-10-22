import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24
PWMB = 23

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_sw1 = GPIO.input(SW1)
prev_sw2 = GPIO.input(SW2)
prev_sw3 = GPIO.input(SW3)
prev_sw4 = GPIO.input(SW4)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:

        current_sw1 = GPIO.input(SW1)
        current_sw2 = GPIO.input(SW2)
        current_sw3 = GPIO.input(SW3)
        current_sw4 = GPIO.input(SW4)

        if prev_sw1 == 0 and current_sw1 == 1:
            print("SW1 : front")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            L_Motor.ChangeDutyCycle(100)
            R_Motor.ChangeDutyCycle(100)
            time.sleep(1.0)

            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
        prev_sw1 = current_sw1
        time.sleep(0.05)
                
        if prev_sw2 == 0 and current_sw2 == 1:
            print("SW2 : right")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            L_Motor.ChangeDutyCycle(100)
            R_Motor.ChangeDutyCycle(30)
            time.sleep(1.0)

            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
        prev_sw2 = current_sw2
        time.sleep(0.05) 
                        
        if prev_sw3 == 0 and current_sw3 == 1:
            print("SW3 : left")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            L_Motor.ChangeDutyCycle(30)
            R_Motor.ChangeDutyCycle(100)
            time.sleep(1.0)

            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
        prev_sw3 = current_sw3
        time.sleep(0.05) 
                        
        if prev_sw4 == 0 and current_sw4 == 1:
            print("SW4 : reverse")
            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            GPIO.output(BIN1, 1)
            GPIO.output(BIN2, 0)
            L_Motor.ChangeDutyCycle(100)
            R_Motor.ChangeDutyCycle(100)
            time.sleep(1.0)

            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            GPIO.output(BIN1, 1)
            GPIO.output(BIN2, 0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
        prev_sw4 = current_sw4
        time.sleep(0.05) 

except KeyboardInterrupt:
    pass

GPIO.cleanup()