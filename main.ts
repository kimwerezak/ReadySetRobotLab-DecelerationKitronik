// This will move the position of the servo to create tick mark each second
function move_servo(position_1: number, position_2: number, time_1: number, time_2: number) {
    pins.servoWritePin(AnalogPin.P15, position_1)
    basic.pause(time_1)
    pins.servoWritePin(AnalogPin.P15, position_2)
    basic.pause(time_2)
}

// This will decelerate the robot and leave a tick mark with each deceleration. 
function decelerate_movement(speed: number, decelerations: number) {
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, speed)
    for (let index = 0; index < decelerations; index++) {
        move_servo(0, 180, 200, 800)
        speed -= 5
        Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, speed)
    }
    Kitronik_Move_Motor.stop()
}

// The main function will decelerate the robot, starting at speed 40 for 6 decelerations,
// leaving a tick with each deceleration.
input.onLogoEvent(TouchButtonEvent.Pressed, function main() {
    decelerate_movement(40, 6)
})
