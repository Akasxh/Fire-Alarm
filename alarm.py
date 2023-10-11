#before using this, go to https://wokwi.com/projects/new/micropython-esp32
# It's a simulator instead of a hardware sensor
#run the code on the website; it will ring the alarm once the temperature is more than 57C

import dht
import time
import machine
from machine import Pin

led=Pin(15,Pin.OUT)
buz1=machine.PWM(Pin(2,Pin.OUT))
buz2=machine.PWM(Pin(4,Pin.OUT))
buz1.freq(1024)
buz2.freq(512)
d=dht.DHT22(Pin(13))
button=Pin(18,Pin.IN)

d.measure()
temp=d.temperature()
humid=d.humidity()

buz1.duty(0)
buz2.duty(0)
while True:
  time.sleep(5)
  print("Temperature in the room : ",str(temp)+"°C")
  print("Humidity in the room :    ",humid)
  if(temp>57):   #temperature in degree Celsius at which fire accidents occur mostly.
    print("**FIRE ALERT**\n")
    print("TO STOP ALARM : PRESS RED BUTTON")
    while True:
      led.on()
      time.sleep(0.4)
      led.off()
      buz1.duty(50)
      time.sleep(0.4)
      buz1.duty(0)
      buz2.duty(50)
      time.sleep(0.5)
      buz2.duty(0)
      if(button.value()==True):
        exit(0)    #Stops the alarm
buz1.deinit()
buz2.deinit()
