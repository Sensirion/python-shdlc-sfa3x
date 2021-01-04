# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sfa3x import Sfa3xShdlcDevice
import pytest


def pytest_addoption(parser):
    """
    Register command line options
    """
    parser.addoption("--serial-port", action="store", type="string")


def _get_serial_port(config, validate=False):
    """
    Get the serial port to be used for the tests.
    """
    port = config.getoption("--serial-port")
    if (validate is True) and (port is None):
        raise ValueError("Please specify the serial port to be used with "
                         "the '--serial-port' argument.")
    return port


def pytest_report_header(config):
    """
    Add extra information to test report header
    """
    lines = []
    lines.append("serial port: " + str(_get_serial_port(config)))
    lines.append("serial bitrate: 115200")
    lines.append("slave address: 0")
    return '\n'.join(lines)


@pytest.fixture(scope="session")
def serial_port(request):
    """
    Fixture to get the serial port to be used for the tests.
    """
    return _get_serial_port(request.config, validate=True)


@pytest.fixture(scope="session")
def connection(serial_port, serial_bitrate=115200):
    with ShdlcSerialPort(serial_port, serial_bitrate) as port:
        connection = ShdlcConnection(port)
        yield connection


@pytest.fixture
def device(connection, slave_address=0):
    device = Sfa3xShdlcDevice(connection, slave_address)
    device.device_reset()

    yield device
