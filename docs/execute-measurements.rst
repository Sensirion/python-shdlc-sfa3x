Install the SFA3x Driver
--------------------------

.. include:: driver-installation.rst

Run Usage-Example
-----------------

1. Connect the SFA3x sensor to your system with the serial USB cable.
2. Run the example script from the root of the repository.

   By default the script assumes the sensor is connected to COM1 serial port. If this is different on your system,
   pass the port in use with the :code:`--serial-port` parameter as outlined below.

   .. sourcecode:: bash

    python <example script>.py --serial-port <your COM port>

Example script
~~~~~~~~~~~~~~

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

