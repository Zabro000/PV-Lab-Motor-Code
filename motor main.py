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
clock = pygame.time.Clock


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



def motor_calibrate(angle_right_now) ->float:
    running = True
    FPS = 60
    stepper = Stepper()
    stepper.openWaitForAttachment(5000)
    stepper.setAcceleration(1000)
    stepper.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
    forwards_velocity = 1000
    backwards_velocity = -1000


    while running:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.K_w:
                stepper.setVelocityLimit(forwards_velocity)
                stepper.setEngaged(True)

            if event.type == pygame.K_s: 
                stepper.setVelocityLimit(backwards_velocity)
                stepper.setEngaged(True)
            
            stepper.setEngaged(False)

            if event.type == pygame.K_ESCAPE:
                stepper.close()
                running = False 


    




motor_test(step_angle)
