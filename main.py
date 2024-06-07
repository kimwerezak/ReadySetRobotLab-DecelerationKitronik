def move_servo(position_1, position_2, time_1, time_2): 
    pins.servo_write_pin(AnalogPin.P15, position_1)
    basic.pause(time_1)
    pins.servo_write_pin(AnalogPin.P15, position_2)
    basic.pause(time_2)
        
def deaccelerate_movement(speed, delay, deaccelerations): 
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, speed)
    for index in range(deaccelerations):
        move_servo(80,135,50,950)
        basic.pause(delay)
        speed -= 5
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, speed)
    Kitronik_Move_Motor.stop()

def main():
    deaccelerate_movement(55,500,9)

input.on_logo_event(TouchButtonEvent.PRESSED, main)

