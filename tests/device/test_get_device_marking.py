# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
import pytest


@pytest.mark.needs_device
def test(device):
    """
    Test if get_device_marking() returns the expected value.
    """
    device_marking = device.get_device_marking()
    assert type(device_marking) is str
