import RPi.GPIO as GPIO
import time

BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 262)


try:

    p.start(50)
    time.sleep(1.0)
    p.ChangeFrequency(394)
    time.sleep(1.0)
    p.ChangeFrequency(330)
    time.sleep(1.0)
    p.ChangeFrequency(349)
    time.sleep(1.0)
    p.ChangeFrequency(292)
    time.sleep(1.0)
    p.ChangeFrequency(440)
    time.sleep(1.0)
    p.ChangeFrequency(494)
    time.sleep(1.0)
    p.ChangeFrequency(523)
    time.sleep(1.0)


except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()