import bluetooth
import threading
import datetime
import random
import time
import json

# THE MODEL OF THE OPENXC THAT IS GOING TO BE CONNECTED TO THIS DEVICE
DEVICE_NAME = "OpenXC-VI-57E3"


class OpenXCDataThread(threading.Thread):

    engine_speed = None
    vehicle_speed = None
    transmission_gear_position = None
    accelerator_pedal_position = None
    steering_wheel_angle = None
    brake_pedal_status = None
    fuel_consumed = None
    fuel_level = None
    high_beam_status = None
    ignition_status = None
    latitude = None
    longitude = None
    odometer = None
    parking_brake_status = None
    torque_at_transmission = None

    message = "Starting up..."

    def __init__(self):
        threading.Thread.__init__(self)
        self.engine_speed = list()
        self.vehicle_speed = list()
        self.transmission_gear_position = list()
        self.accelerator_pedal_position = list()
        self.steering_wheel_angle = list()
        self.brake_pedal_status = list()
        self.fuel_consumed = list()
        self.fuel_level = list()
        self.high_beam_status = list()
        self.ignition_status = list()
        self.latitude = list()
        self.longitude = list()
        self.odometer = list()
        self.parking_brake_status = list()
        self.torque_at_transmission = list()

    def run(self):
        target_address = None

        self.message = "Searching for a paired device called \"" + DEVICE_NAME + "\"."
        nearby_devices = bluetooth.discover_devices()

        for bdaddr in nearby_devices:
            if DEVICE_NAME == bluetooth.lookup_name(bdaddr):
                target_address = bdaddr
                break
            else:
                print(bluetooth.lookup_name(bdaddr))

        target_found = True
        if target_address is not None:
            self.message = "Found target bluetooth device with address " + target_address

        else:
            self.message = "Could not find target bluetooth device nearby"

        if target_found:
            port = 1

            connected = False
            try_count = 1
            while not connected:
                self.message = "Trying to connect, try "+str(try_count)
                try_count += 1
                sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                try:
                    sock.connect((target_address, port))
                    connected = True
                except IOError:
                    print("Failed to connect")

            self.message = "Successfully accessed device, waiting for data."

            while True:
                data = ''
                char = ''
                while len(char) == 0 or chr(char[0]) != '}':
                    char = sock.recv(1)
                    if len(char) > 0 and char[0] != 0:
                        data += chr(char[0])

                decoded = False
                try:
                    jdata = json.loads(data)
                    decoded = True
                except:
                    print("Error decoding data. Does not appear to be JSON format.")

                if decoded:

                    if jdata['name'] == 'engine_speed':
                        self.engine_speed.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'vehicle_speed':
                        self.vehicle_speed.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'transmission_gear_position':
                        self.transmission_gear_position.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'accelerator_pedal_position':
                        self.accelerator_pedal_position.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'steering_wheel_angle':
                        self.steering_wheel_angle.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'brake_pedal_status':
                        self.brake_pedal_status.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'fuel_consumed':
                        self.fuel_consumed.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'fuel_level ':
                        self.fuel_level.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'fuel_consumed':
                        self.fuel_consumed.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'high_beam_status':
                        self.high_beam_status.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'ignition_status':
                        self.ignition_status.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'latitude':
                        self.latitude.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'longitude':
                        self.longitude.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'odometer':
                        self.odometer.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'parking_brake_status':
                        self.parking_brake_status.append(
                            (time.time() * 1000, jdata['value']))

                    elif jdata['name'] == 'torque_at_transmission':
                        self.torque_at_transmission.append(
                            (time.time() * 1000, jdata['value']))
