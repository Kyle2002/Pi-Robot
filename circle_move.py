import gpiozero
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))

for i in range(2000):
    robot.forward()
    time.sleep(0.01)
    robot.right()
    time.sleep(3.0)
    robot.left()
    time.sleep(3.0)

