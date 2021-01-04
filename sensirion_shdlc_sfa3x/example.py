# -*- coding: utf-8 -*-
# (c) Copyright 2019 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sfa3x import Sfa3xShdlcDevice
import time

import logging
log = logging.getLogger(__name__)


def main():
    # Connect to the device with default settings:
    #  - baudrate:      115200
    #  - slave address: 0
    with ShdlcSerialPort(port='COM1', baudrate=115200) as port:
        device = Sfa3xShdlcDevice(ShdlcConnection(port), slave_address=0)
        print("Resetting device... ")
        device.device_reset()

        # Print device information
        print("Device Marking: {}".format(device.get_device_marking()))

        # Measure
        device.start_measurement()
        print("Measurement started... ")
        while True:
            time.sleep(10.)
            hcho, humidity, temperature = device.read_measured_values()
            # use default formatting for printing output:
            print("{}, {}, {}".format(hcho, humidity, temperature))
            # custom printing of attributes:
            print(". Formaldehyde concentration = {} ppb "
                  "(received int16 = {}) ".format(hcho.ppb, hcho.ticks))
            print(". Humidity = {:0.2f} %RH (received int16 = {})".format(
                humidity.percent_rh, humidity.ticks))
            print(". Temperature = {:0.2f} °C (received int16 = {})".format(
                temperature.degrees_celsius, temperature.ticks))


if __name__ == "__main__":
    main()
