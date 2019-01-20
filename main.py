import openxc_thread
import threading
import bluetooth
import datetime
import pygame
import time
import json
import os


# SETTING VARIABLES
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Window Size
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

# Time range of the graph
TIME_RANGE = 60
DATA_CAPTURE_FINISHED = False


# THE CLASS THAT HAS THE DATA
classdict = {}

classdict["accelerator_pedal_position"] = None
classdict["steering_wheel_angle"] = None
classdict["vehicle_speed"] = None
classdict["engine_speed"] = None
classdict["brake_pedal_status"] = None
classdict["fuel_consumed"] = None
classdict["fuel_level"] = None
classdict["high_beam_status"] = None
classdict["ignition_status"] = None
classdict["latitude"] = None
classdict["longitude"] = None
classdict["odometer"] = None
classdict["parking_brake_status"] = None
classdict["torque_at_transmission"] = None

options = ["accelerator_pedal_position", "steering_wheel_angle", "vehicle_speed",
           "brake_pedal_status", "fuel_consumed", "fuel_level", "high_beam_status", "ignition_status",
           "latitude", "longitude", "odometer", "parking_brake_status",
           "torque_at_transmission", "transmission_gear_position"]


column_title = False

# THE FILE THAT STORES ALL THE DATA
csvFile = open('data.csv', 'w')


# MENU FOR THE CONSOLE DATA SELECTION
print("-------------------------------------------------------------------------------------")
print("Choose the variables you want to measure and write the number, for multiple choices use a comma ','")
print("-------------------------------------------------------------------------------------\n\n")

for t in range(len(options)):
    print("> Do you want to measure "+options[t]+" ? [" + str(t) + "] \n")
answer = input("variables \n")


# WINDOW INIT
# Center the window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Title of the window
pygame.display.set_caption("OpenXC Data Grabber & Monitor")


clock = pygame.time.Clock()

data_thread = openxc_thread.OpenXCDataThread()
data_thread.start()

# Font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 27, False, False)


# DATA CAPTURE WHILE-LOOP
while not DATA_CAPTURE_FINISHED:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DATA_CAPTURE_FINISHED = True

    screen.fill(BLACK)

    # RESETS EMPTY LINE VALUE
    emptyLine = True
    line = ""

    if '0' in answer:
        if column_title:
            if len(data_thread.accelerator_pedal_position) != 0:
                line = line + \
                    str(data_thread.accelerator_pedal_position[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("accelerator_pedal_position" + ",")

    if '1' in answer:
        if column_title:
            if len(data_thread.steering_wheel_angle) != 0:
                line = line + \
                    str(data_thread.steering_wheel_angle[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("steering_wheel_angle" + ",")

    if '2' in answer:
        if column_title:
            if len(data_thread.vehicle_speed) != 0:
                line = line + \
                    str(data_thread.vehicle_speed[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("vehicle_speed" + ",")

    if '3' in answer:
        if column_title:
            if len(data_thread.engine_speed) != 0:
                line = line + \
                    str(data_thread.engine_speed[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("engine_speed" + ",")

    if '4' in answer:
        if column_title:
            if len(data_thread.brake_pedal_status) != 0:
                line = line + \
                    str(data_thread.brake_pedal_status[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("brake_pedal_status" + ",")

    if '5' in answer:
        if column_title:
            if len(data_thread.fuel_consumed) != 0:
                line = line + \
                    str(data_thread.fuel_consumed[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("fuel_consumed" + ",")

    if '6' in answer:
        if column_title:
            if len(data_thread.fuel_level) != 0:
                line = line + \
                    str(data_thread.fuel_level[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("fuel_level" + ",")

    if '7' in answer:
        if column_title:
            if len(data_thread.high_beam_status) != 0:
                line = line + \
                    str(data_thread.high_beam_status[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("high_beam_status" + ",")

    if '8' in answer:
        if column_title:
            if len(data_thread.ignition_status) != 0:
                line = line + \
                    str(data_thread.ignition_status[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("ignition_status" + ",")

    if '9' in answer:
        if column_title:
            if len(data_thread.latitude) != 0:
                line = line + \
                    str(data_thread.latitude[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("latitude" + ",")

    if '10' in answer:
        if column_title:
            if len(data_thread.longitude) != 0:
                line = line + \
                    str(data_thread.longitude[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("longitude" + ",")

    if '11' in answer:
        if column_title:
            if len(data_thread.odometer) != 0:
                line = line + \
                    str(data_thread.odometer[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("odometer" + ",")

    if '12' in answer:
        if column_title:
            if len(data_thread.parking_brake_status) != 0:
                line = line + \
                    str(data_thread.parking_brake_status[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("parking_brake_status" + ",")

    if '13' in answer:
        if column_title:
            if len(data_thread.torque_at_transmission) != 0:
                line = line + \
                    str(data_thread.torque_at_transmission[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("torque_at_transmission" + ",")

    if '14' in answer:
        if column_title:
            if len(data_thread.transmission_gear_position) != 0:
                line = line + \
                    str(data_thread.transmission_gear_position[-1][1]) + ","
                emptyLine = False
        else:
            csvFile.write("transmission_gear_position" + ",")

    # ENGINE SPEED
    if len(data_thread.engine_speed) == 0:
        text = font.render(data_thread.message, True, WHITE)
    else:
        text = font.render(
            "RPM (Revolutions Per Minute): "+str(data_thread.engine_speed[-1][1]), True, WHITE)

    screen.blit(text, [10, 10])

    # VEHICULE SPEED
    if len(data_thread.vehicle_speed) == 0:
        text = font.render("", True, RED)
    else:
        text = font.render("Vehicle Speed: {:.1f} kph".format(
            data_thread.vehicle_speed[-1][1]), True, GREEN)

    screen.blit(text, [10, 40])

    # GEAR POSITION
    if len(data_thread.transmission_gear_position) == 0:
        text = font.render("", True, RED)
    else:
        text = font.render(
            "Gear: "+str(data_thread.transmission_gear_position[-1][1]), True, YELLOW)

    screen.blit(text, [10, 70])

    # MAKE THE COLUMN NAMES
    if column_title:
        if not emptyLine:
            csvFile.write(line + "\n")
    else:
        csvFile.write("photo_name, \n")
        column_title = True

    for i in range(0, len(data_thread.engine_speed)):
        if i > 0:
            speed_data_1 = data_thread.engine_speed[i-1][1]
            speed_data_2 = data_thread.engine_speed[i][1]
            time_data_1 = data_thread.engine_speed[i-1][0]
            time_data_2 = data_thread.engine_speed[i][0]

            y1 = WINDOW_HEIGHT - (speed_data_1 / 15)
            y2 = WINDOW_HEIGHT - (speed_data_2 / 15)

            current_time = time.time() * 1000
            x1 = WINDOW_WIDTH - ((current_time - time_data_1) /
                                 (TIME_RANGE * 1000.) * WINDOW_WIDTH)
            x2 = WINDOW_WIDTH - ((current_time - time_data_2) /
                                 (TIME_RANGE * 1000.) * WINDOW_WIDTH)

            if x2 > 0:
                pygame.draw.line(screen, BLUE,
                                 [x1, y1],
                                 [x2, y2], 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
