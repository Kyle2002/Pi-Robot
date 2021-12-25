import gpiozero

button = gpiozero.Button(6)

while True:
    if button.is_pressed:
        print("pressed")
    else:
        print("Button is not pressed")
