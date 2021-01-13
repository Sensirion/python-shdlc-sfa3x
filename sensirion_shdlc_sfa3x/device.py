# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver import ShdlcDeviceBase
from .device_errors import SFA3X_DEVICE_ERROR_LIST
from .commands import \
    Sfa3xCmdStartContinuousMeasurement, \
    Sfa3xCmdStopMeasurement, \
    Sfa3xCmdReadMeasuredValuesOutputFormat2, \
    Sfa3xCmdGetDeviceMarking, \
    Sfa3xCmdDeviceReset
from .response_types import FormaldehydeConcentration, Humidity, Temperature


import logging
log = logging.getLogger(__name__)


class Sfa3xShdlcDevice(ShdlcDeviceBase):
    """
    SFA3x device.

    This is a low-level driver which just provides all SHDLC commands as Python
    methods. Typically, calling a method sends one SHDLC request to the device
    and interprets its response. There is no higher level functionality
    available, please look for other drivers if you need a higher level
    interface.

    There is no (or very few) caching functionality in this driver. For example
    if you call :func:`get_device_marking` 100 times, it will send the command
    100 times over the SHDLC interface to the device. This makes the driver
    (nearly) stateless.
    """

    def __init__(self, connection, slave_address):
        """
        Create a SFA3x device instance on an SHDLC connection.

        .. note:: This constructor does not communicate with the device, so
                  it's possible to instantiate an object even if the device is
                  not connected or powered yet.

        :param ~sensirion_shdlc_driver.connection.ShdlcConnection connection:
            The connection used for the communication.
        :param byte slave_address:
            The address of the device. The default address of the SFA3x is 0.
        """
        super(Sfa3xShdlcDevice, self).__init__(connection, slave_address)
        self._register_device_errors(SFA3X_DEVICE_ERROR_LIST)

    def get_device_marking(self):
        """
        Gets the device marking from the device.

        :return: The device marking as an ASCII string.
        :rtype: string
        """
        return self.execute(Sfa3xCmdGetDeviceMarking())

    def device_reset(self):
        """
        Execute a device reset (reboot firmware, similar to power cycle).
        """
        self.execute(Sfa3xCmdDeviceReset())

    def start_measurement(self):
        """
        Starts continuous measurement in polling mode.

        .. note:: This command is only available in idle mode.
        """
        self.execute(Sfa3xCmdStartContinuousMeasurement())

    def stop_measurement(self):
        """
        Leaves the measurement mode and returns to the idle mode.

        .. note:: This command is only available in measurement mode.
        """
        self.execute(Sfa3xCmdStopMeasurement())

    def read_measured_values(self):
        """
        Returns the new measurement results.

        :return:
            The measured formaldehyde concentration, humidity and temperature.

            - hcho (:py:class:`~sensirion_shdlc_sfa3x.response_types.FormaldehydeConcentration`) -
              Formaldehyde concentration response object.
            - humidity (:py:class:`~sensirion_shdlc_sfa3x.response_types.Humidity`) -
              Humidity response object.
            - temperature (:py:class:`~sensirion_shdlc_sfa3x.response_types.Temperature`) -
              Temperature response object.
        :rtype:
            tuple
        :raises ~sensirion_shdlc_sfa3x.device_errors.Sfa3xNoMeasurementDataAvailable:
            If the measure mode was not started, or it was started but no
            measurement results are available yet. After starting the
            measurement, you have to wait at least 1 Second before reading
            any results.
        """  # noqa: E501
        hcho, rh, t = self.execute(Sfa3xCmdReadMeasuredValuesOutputFormat2())
        return FormaldehydeConcentration(hcho), Humidity(rh), Temperature(t)
