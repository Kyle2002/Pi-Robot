import gpiozero
import cwiid

robot = gpiozero.Robot(left=(17,18), right=(27,22))

print("Press and hold the 1+2 buttons on your Wiimote simultaneously");
wii = cwiid.Wiimote()

print("Connection established")

wii.rpt_mode = cwiid.RPT_BTN

while True:
        buttons = wii.state["buttons"]
        if (buttons& cwiid.BTN_LEFT):
                print('left\n')
                robot.left()
        if (buttons & cwiid.BTN_RIGHT):
                print('right\n')
                robot.right()
        if (buttons & cwiid.BTN_UP):
                print('up\n')
                robot.forward()
        if (buttons & cwiid.BTN_DOWN):
                print('down\n')
                robot.backward()
        if (buttons & cwiid.BTN_B):
                print('Button B\n')
                robot.stop()


