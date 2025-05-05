# import modules
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
 
# define the pin we will attach to
GPIO_PIN = 18
GPIO.setup(GPIO_PIN, GPIO.OUT)

# start at 50 hertz 
GPFrequency = 50 
pwm = GPIO.PWM(GPIO_PIN, GPFrequency)
pwm.start(50)

    while(True):
    for GPFrequency in range(5000):
        pwm.ChangeFrequency(GPFrequency)