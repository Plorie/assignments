import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19
BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_sw1 = GPIO.input(SW1)
prev_sw2 = GPIO.input(SW2)
prev_sw3 = GPIO.input(SW3)
prev_sw4 = GPIO.input(SW4)
p = GPIO.PWM(BUZZER, 262)
try:
    while True:
        current_sw1 = GPIO.input(SW1)
        current_sw2 = GPIO.input(SW2)
        current_sw3 = GPIO.input(SW3)
        current_sw4 = GPIO.input(SW4)

        if prev_sw1 == 0 and current_sw1 == 1:
            print("click 1")
            p.start(50)
            p.ChangeFrequency(262)
            time.sleep(0.6)
            p.stop()
        prev_sw1 = current_sw1
        time.sleep(0.05)
                
        if prev_sw2 == 0 and current_sw2 == 1:
            print("click 2")
            p.start(50)
            p.ChangeFrequency(394)
            time.sleep(0.6)
            p.stop()
        prev_sw2 = current_sw2
        time.sleep(0.05) 
                        
        if prev_sw3 == 0 and current_sw3 == 1:
            print("click 3")
            p.start(50)
            p.ChangeFrequency(440)
            time.sleep(0.6)
            p.stop()
        prev_sw3 = current_sw3
        time.sleep(0.05) 
                        
        if prev_sw4 == 0 and current_sw4 == 1:
            print("click 4")
            p.start(50)
            p.ChangeFrequency(550)
            time.sleep(0.6)
            p.stop()
        prev_sw4 = current_sw4
        time.sleep(0.05) 
 



except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()