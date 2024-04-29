#libraries needed
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.Stepper import * ## make sure that the stepper driver is installed
import time
import math
import pygame




voltage_right_now = None
angle_right_now = None
motor_resoultion = None
max_current = 0.35 
test_current = 0.2
rated_voltage = 12
test_voltage = 10
step_angle = None
FPS = 60 
clock = pygame.time.Clock()


def step_angle_finder() ->float:
    return 360 / 200

step_angle = step_angle_finder()

def angle_to_steps(angle, step_per_angle) ->float:
    return angle/step_per_angle


def motor_test(angle_per_step, max_current = None) -> None:
    print("here")
    if max_current == None:
        max_current = 0.2

    test_stepper = Stepper()
    test_stepper.openWaitForAttachment(5000)
    test_stepper.setAcceleration(1000)
    test_stepper.setTargetPosition(60)
    test_stepper.setEngaged(True)

    while test_stepper.getIsMoving() == True:
        pass
	
    test_stepper.close()



def motor_calibrate(angle_right_now = 0.0) ->None:
    print("Type any number for the steps you want it to move and type, done, to stop the this loop.", '\n')
    
    
    try:
        stepper = Stepper()
        stepper.setAcceleration(1000)
        stepper.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
        factor = (1/16) * (1.8/1)
        stepper.setRescaleFactor(factor)
        forwards_velocity = 1000
        backwards_velocity = -1000
        stepper.openWaitForAttachment(5000)
        stepper.setEngaged(True)
    except PhidgetException:
        print("The motor controller is not connected... There error is: ", PhidgetException)
        return
    

    while True:
        print("Input a value:", '\n')
        temp_value = input()
        print('\n')
        temp_value = temp_value.lower()

        if temp_value == "done":
            stepper.close()
            break

        try:
            temp_value = float(temp_value)
        except:
            print("Not a number...", '\n')
            pass
        else:
            stepper.setTargetPosition(temp_value)
            while stepper.getIsMoving() == True:
                pass

    stepper.close()




### use outside code, this will run an incriment then stop and it will run the same incriment each time should be used in a for loop or something, will not stop the stepper
def motor_run(starting_angle = 0.0, starting_steps = 0.0, current_position = None, increment = None) -> None:
    
    try:
        stepper = Stepper()
        stepper.setAcceleration(1000)
        stepper.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
        factor = (1/16) * (1.8/1)
        stepper.setRescaleFactor(factor)
        forwards_velocity = 1000
        backwards_velocity = -1000
        stepper.openWaitForAttachment(5000)
        stepper.setEngaged(True)
    except PhidgetException:
        print("The motor controller is not connected... There error is: ", PhidgetException)
        return
    
    if increment == None:
        increment = 10
    
    if current_position == None:
        current_position = 0
    
    stepper.setTargetPosition(increment)
    current_position += increment

    while stepper.getIsMoving() == True:
        pass

    print("Stepper is done!")





print(step_angle_finder())


motor_calibrate()
motor_run()
#motor_test(step_angle)

