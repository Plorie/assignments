import RPi.GPIO as GPIO
import time

BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 440)

try:

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


except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()