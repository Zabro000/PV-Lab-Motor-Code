#libraries needed
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.Stepper import * ## make sure that the stepper driver is installed
import time
import keyboard


voltage_right_now = None
angle_right_now = None
motor_resoultion = None
max_current = 0.35 
test_current = 0.2
rated_voltage = 12
test_voltage = 10
steps_per_angle_for_large_nputs = 8

wait_time = 6 #This should be longer

degree_increment = 10 #degrees for the incriment for the motor
steps_per_angle_for_small_inputs = 10 #steps per angle for small inputs 
for_loop_increments = 9 # nine for loop incriments
for_loop_measuring_increments = for_loop_increments + 1

csv_data_file_name = "Angle Voltage Current Energy Time Photons.csv"

def Steps_Convert(angle, steps_per_angle):
    return angle * steps_per_angle

def motor_test() -> None:
    test_stepper = Stepper()
    test_stepper.openWaitForAttachment(5000)
    test_stepper.setAcceleration(5000)
    steps = Steps_Convert(10, 10)
    test_stepper.setEngaged(True)


    for i in range(1,3):
        test_stepper.setTargetPosition(steps * i)
        test_stepper.setEngaged(True)

        while test_stepper.getIsMoving() == True:
            pass

    for i in range(1,3):
        test_stepper.setTargetPosition(-steps * i)
        test_stepper.setEngaged(True)

        while test_stepper.getIsMoving() == True:
            pass



    
    

def motor_run(starting_angle = 0.0, starting_steps = 0.0, current_position_angle = None, angle_increment = None, steps_per_angle = None) -> float:
    

    stepper = Stepper()
    stepper.openWaitForAttachment(5000)
    stepper.setAcceleration(500)
    stepper.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
    print(steps_per_angle)


    temp_steps = Steps_Convert(angle_increment, steps_per_angle)

    stepper.setTargetPosition(temp_steps)
    stepper.setEngaged(True)

    while stepper.getIsMoving() == True:
        pass

    print("Increment is done!")
    
    return temp_steps, angle_increment




total_angle = 0.0
total_steps = 0.0

angle_list = [total_angle]
voltage_list = []
current_list =[]


#######################################################################################################



print("THE LOOP IS STARTING")
input()


input("The tests are done so press another time to start the main loop")



stepper = Stepper()
stepper.openWaitForAttachment(5000)
stepper.setAcceleration(500)
stepper.setControlMode(StepperControlMode.CONTROL_MODE_STEP)


temp_steps = Steps_Convert(degree_increment, steps_per_angle_for_large_nputs)

stepper.setTargetPosition(temp_steps)
stepper.setEngaged(True)


starting_time = time.time()
print(starting_time)

right_now_time = time.time()
print(right_now_time)


# Right now they are the same, remeber this is in seconds

for index in range(1, for_loop_increments + 1):

    right_now_time = time.time()
    starting_time = time.time()

    # This is the loop for the voltage and current measruement
    while starting_time + 10 > right_now_time:
        print("wait")
        right_now_time = time.time()
    

    
    stepper.setTargetPosition(temp_steps * index)
    stepper.setEngaged(True)

    while stepper.getIsMoving() == True:
        pass

    total_angle += degree_increment 
    total_steps += temp_steps

    angle_list.append(total_angle)
        



print(angle_list)
print(total_steps)


raise OSError



for i in range(0, for_loop_increments):
    # Put the voltage code right here


    

    time.sleep(wait_time)
    temp_steps, temp_angle = motor_run(angle_increment= degree_increment, steps_per_angle= steps_per_angle_for_small_inputs)
    total_angle += temp_angle 
    total_steps += temp_steps

    angle_list.append(total_angle)



print(angle_list)



















