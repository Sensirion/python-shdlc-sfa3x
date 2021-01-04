# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if device_reset() works as expected by changing a volatile setting,
    perform the reset, and then verifying that the setting was reset to its
    default value.
    """
    device.start_measurement()
    device.device_reset()

    # -> would throw an exception if called twice without a proper reset
    device.start_measurement()
