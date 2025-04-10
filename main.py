#This will move the position of the servo to create tick mark each second
def move_servo(position_1, position_2, time_1, time_2): 
    pins.servo_write_pin(AnalogPin.P15, position_1)
    basic.pause(time_1)
    pins.servo_write_pin(AnalogPin.P15, position_2)
    basic.pause(time_2)

#This will decelerate the robot and leave a tick mark with each deceleration. 
def decelerate_movement(speed, decelerations): 
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, speed)
    for index in range(decelerations):
        move_servo(0, 180, 200, 800)
        speed -= 5
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, speed)
    Kitronik_Move_Motor.stop()

#The main function will decelerate the robot, starting at speed 40 for 6 decelerations,
#leaving a tick with each deceleration.
def main():
    decelerate_movement(40, 6)

input.on_logo_event(TouchButtonEvent.PRESSED, main)

