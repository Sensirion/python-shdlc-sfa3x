API Reference
=============

Sfa3xShdlcDevice
----------------

.. automodule:: sensirion_shdlc_sfa3x.device


Response Data Types
-------------------

Formaldehyde Concentration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfa3x.response_types.FormaldehydeConcentration

Humidity
^^^^^^^^

.. autoclass:: sensirion_shdlc_sfa3x.response_types.Humidity

Temperature
^^^^^^^^^^^

.. autoclass:: sensirion_shdlc_sfa3x.response_types.Temperature


Device Errors
-------------

.. automodule:: sensirion_shdlc_sfa3x.device_errors
    :exclude-members: __init__



Commands
--------
Start Continuous Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: sensirion_shdlc_sfa3x.commands.start_measurement.Sfa3xCmdStartContinuousMeasurement
    :exclude-members: __init__

Stop Continuous Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: sensirion_shdlc_sfa3x.commands.stop_measurement.Sfa3xCmdStopMeasurement
    :exclude-members: __init__

Read Measured Values
^^^^^^^^^^^^^^^^^^^^
.. autoclass:: sensirion_shdlc_sfa3x.commands.read_measured_values.Sfa3xCmdReadMeasuredValuesOutputFormat2
    :exclude-members: __init__

Get Device Marking
^^^^^^^^^^^^^^^^^^
.. autoclass:: sensirion_shdlc_sfa3x.commands.device_information.Sfa3xCmdGetDeviceMarking
    :exclude-members: __init__

Device Reset
^^^^^^^^^^^^
.. autoclass:: sensirion_shdlc_sfa3x.commands.device_reset.Sfa3xCmdDeviceReset
    :exclude-members: __init__
