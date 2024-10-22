import RPi.GPIO as GPIO
import time

SW1 = 5
BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_sw1 = GPIO.input(SW1)
p = GPIO.PWM(BUZZER, 440)

try:
    while True:
        current_sw1 = GPIO.input(SW1)
        if prev_sw1 == 0 and current_sw1 == 1:
            print("click")
            p.start(50)
            time.sleep(0.6)
            p.ChangeFrequency(292)
            time.sleep(0.6)
            p.ChangeFrequency(440)
            time.sleep(0.6)
            p.ChangeFrequency(292)
            time.sleep(0.6)
            p.ChangeFrequency(440)
            time.sleep(0.6)
            p.ChangeFrequency(292)
            time.sleep(0.6)
            p.ChangeFrequency(292)
            time.sleep(0.6)
            p.ChangeFrequency(440)
            time.sleep(0.6)
            break
        prev_sw1 = current_sw1
        time.sleep(0.05) 



except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()