import gpiozero
import subprocess
import sys
import time

led = gpiozero.LED(26)

wiimote_button = gpiozero.Button(6)

led.on()
time.sleep(5)

# Wait for the button press to start the robot control
while True:
    if wiimote_button.is_pressed:
        subprocess.Popen(["python3", "/home/pi/robot/remote_control_accel.py"])
        sys.exit()
    time.sleep(.08)

