from gpiozero import MotionSensor

pir = MotionSensor (4)
while True:
    if pir.motion_detected:
        print("Fuck Yeah!")
    else:
        print("Fuck No!")
        
