import gpiozero
import cwiid
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))

print("Press and hold the 1+2 buttons on your Wiimote simultaneously");
wii = cwiid.Wiimote()

print("Connection established")

wii.rumble = 1
time.sleep(.5)
wii.rumble = 0

wii.rpt_mode = cwiid.RPT_BTN

while True:
        buttons = wii.state["buttons"]
        button_pressed = False
        speed = 0.6
        
        if (buttons & cwiid.BTN_B):
                speed = 1.0
                

        if (buttons& cwiid.BTN_LEFT):
                #print('left\n')
                robot.left(speed)
                button_pressed = True
        if (buttons & cwiid.BTN_RIGHT):
                #print('right\n')
                robot.right(speed)
                button_pressed = True
        if (buttons & cwiid.BTN_UP):
                #print('up\n')
                robot.forward(speed)
                button_pressed = True
        if (buttons & cwiid.BTN_DOWN):
                #print('down\n')
                robot.backward(speed)
                button_pressed = True
        if not button_pressed:
                #print ('Stop\n')
                robot.stop()
        time.sleep(0.02)


