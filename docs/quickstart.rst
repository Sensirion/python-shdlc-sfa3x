Quick Start
===========

Following example code shows how the driver is intended to be used:

.. sourcecode:: python

    import time
    from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
    from sensirion_shdlc_sfa3x import Sfa3xShdlcDevice

    # Connect to the device with default settings:
    #  - baudrate:      115200
    #  - slave address: 0
    with ShdlcSerialPort(port='COM1', baudrate=115200) as port:
        device = Sfa3xShdlcDevice(ShdlcConnection(port), slave_address=0)
        device.device_reset()

        # Print device information
        print("Device Marking: {}".format(device.get_device_marking()))

        # Start measurement
        device.start_measurement()
        print("Measurement started... ")
        while True:
            time.sleep(10.)
            hcho, humidity, temperature = device.read_measured_values()
            # use default formatting for printing output:
            print("{}, {}, {}".format(hcho, humidity, temperature))
