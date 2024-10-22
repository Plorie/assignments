import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_sw1 = GPIO.input(SW1)
prev_sw2 = GPIO.input(SW2)
prev_sw3 = GPIO.input(SW3)
prev_sw4 = GPIO.input(SW4)
Alist = []
try:
    while True:
        current_sw1 = GPIO.input(SW1)
        current_sw2 = GPIO.input(SW2)
        current_sw3 = GPIO.input(SW3)
        current_sw4 = GPIO.input(SW4)

        if prev_sw1 == 0 and current_sw1 == 1:
            print('SW1 clicked', 1)
            Alist.append('SW1 0 -> 1 -> 0')
        if prev_sw2 == 0 and current_sw2 == 1:
            print('SW2 clicked', 2)
            Alist.append('SW2 0 -> 1 -> 0')
        if prev_sw3 == 0 and current_sw3 == 1:
            print('SW3 clicked', 3)
            Alist.append('SW3 0 -> 1 -> 0')
        if prev_sw4 == 0 and current_sw4 == 1:
            print('SW4 clicked', 4)
            Alist.append('SW4 0 -> 1 -> 0')

        prev_sw1 = current_sw1
        prev_sw2 = current_sw2
        prev_sw3 = current_sw3
        prev_sw4 = current_sw4

        time.sleep(0.05) 

except KeyboardInterrupt:
    pass

print(Alist)
GPIO.cleanup()