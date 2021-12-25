import gpiozero
import cwiid
import time
import threading

bt_connected = False
bt_failed = False
led = gpiozero.LED(16)

class LedThread(threading.Thread):

        def __init__(self):
                threading.Thread.__init__(self)
                
        def run(self):
                global bt_connected
                global bt_failed
                global led
                cnt = 0
                while not bt_connected and not bt_failed:
                        if cnt % 2 == 0:
                                led.on()
                        else:
                                led.off()
                        cnt = cnt + 1
                        time.sleep(0.5)

                if bt_failed:
                        led.off()
                        return

                led.on()

led_thread = LedThread()
print('start thread')
led_thread.start()
print('Create robot IO')
robot = gpiozero.Robot(left=(17,18), right=(27,22))

i = 0
wii = None
print("Press and hold the 1+2 buttons on your Wiimote simultaneously")

while not wii:
        
        try:
                wii = cwiid.Wiimote()
        except RuntimeError:
                if(i>20 and not wii):
                        bt_failed = True
                        print("Unable to connect to Wiimote")
                        led_thread.join()
                        sys.exit(-1)
                i = i + 1

bt_connected = True
led_thread.join()
print("Connection established")

wii.rumble = 1
time.sleep(.5)
wii.rumble = 0

wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC




while True:
        buttons = wii.state["buttons"]
        button_pressed = False
        speed = 1.0

        if buttons & cwiid.BTN_2:
                print("forward\n")
                move = robot.forward
                turn_right = robot.right
                turn_left = robot.left
        elif buttons & cwiid.BTN_1:
                print("backward\n")
                move = robot.backward
                turn_right = robot.left
                turn_left = robot.right
        else:
                robot.stop()
                time.sleep(0.02)
                continue
        
                
        y_val = wii.state['acc'][1]

        if y_val > 130:
                diff = y_val - 130
                if diff < 22:
                        diff = min(diff, 20)
                        print("curve left: " + str(diff/20.0) + "\n")
                        move(speed, curve_left=diff/20.0)
                else:
                        print("hard left\n")
                        turn_left(speed)
        elif y_val < 130:
                diff = 130 - y_val
                if diff < 22:
                        diff = min(diff, 20)
                        print("curve right: " + str(diff/20.0)+"\n")
                        move(speed, curve_right=diff/20.0)
                else:
                        print("hard right\n")
                        turn_right(speed)
        else:
                move(speed)
        '''
        if y_val > 130 + 18:
                robot.left(speed)
        elif y_val < 130 - 18:
                robot.right(speed)
                
        else:
                robot.forward(speed)
        '''
        
        """
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
        """
        time.sleep(0.02)


