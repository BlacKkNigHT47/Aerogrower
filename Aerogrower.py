import RPi.GPIO as GPIO
import time

input_channel = 26 # Input reading from humidistat
output_channel = 17 # Output to Relay
humidity_high_channel = 16 # Turns on Humdity Hig LED
# Humidifier on LED can use the same pin as humidifier
interval = 5

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(output_channel, GPIO.OUT)
    GPIO.setup(humidity_high_channel, GPIO.OUT)
    # Start with OFF
    GPIO.output(output_channel, GPIO.LOW)
    GPIO.output(humidity_high_channel, GPIO.LOW)
    
def set_mister(cmd):
    if (cmd):
        GPIO.output(output_channel, GPIO.HIGH)
    else:
        GPIO.output(output_channel, GPIO.LOW)
        
def humidity_high_LED(cmd):
    if (cmd):
        GPIO.output(humidity_high_channel, GPIO.HIGH)
    else:
        GPIO.output(humidity_high_channel, GPIO.LOW)
 
init()
last_on_count = 0
last_off_count = 0
while True:

    if (GPIO.input(input_channel)):
        if (last_on_count):
            print("Humidity is low. The mister has been on for " + str(interval * last_on_count) + " seconds")
        set_mister(True)
        humidity_high_LED(False)
        last_on_count += 1
        last_off_count = 0
    else:
        if (last_off_count):
            print("Humidity is high. The mister has been off for " + str(interval * last_off_count) + " seconds")
        set_mister(False)
        humidity_high_LED(True)
        last_on_count = 0
        last_off_count += 1
    time.sleep(interval)