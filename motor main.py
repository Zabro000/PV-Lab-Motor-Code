#libraries needed
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.Stepper import *
import time
import math



voltage_right_now = None
angle_right_now = None
motor_resoultion = None
max_current = 0.35 
test_current = 0.2
rated_voltage = 12
test_voltage = 10
step_angle = None

def step_angle_finder() ->float:
    return 360 / 200

step_angle = step_angle_finder()

def angle_to_steps(angle, step_per_angle) ->float:
    return angle/step_per_angle




def motor_test(angle_per_step, max_current = None) -> None:
    if max_current == None:
        max_current = 0.2
    test_stepper = Stepper()
    test_stepper.setCurrentLimit(0.2)
    test_stepper.openWaitForAttachment(5000)
    test_stepper.setAcceleration(1000)
    test_stepper.setTargetPosition(angle_to_steps(120,angle_per_step))
    test_stepper.setEngaged(True)
    test_stepper.close()



def motor_calibrate(angle_right_now) ->float:
    ...




motor_test(step_angle)