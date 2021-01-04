# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_sfa3x.device_errors import \
    Sfa3xCommandNotAllowedInCurrentState
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if start_measurement() and stop_measurement() work as expected.
    """

    # start continuous measurement and make sure it worked
    device.start_measurement()
    with pytest.raises(Sfa3xCommandNotAllowedInCurrentState):
        device.start_measurement()

    # stop and restart measurement
    device.stop_measurement()
    device.start_measurement()
