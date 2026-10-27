Run tests
=========

Unit tests can be run with `pytest <https://pytest.org>`_:

.. code-block:: bash

    pip install -e .[test]                       # Install test requirements

We provide a mock implementation that allows you to execute the tests for SFA3x without hardware.

.. code-block:: bash

    pytest                                       # Run all tests for SFA3x using a driver mock

To run the tests against real hardware, you must have your SFA3x sensor connected to a serial port of your
development machine. Pass the serial port used, e.g. COM1, as command line argument when running the tests:

.. code-block:: bash

    pytest --serial-port=COM1                    # Run all tests for SFA3x an the sensor attached to COM1

