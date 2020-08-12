#!/usr/bin/env python3

## Copyright (C) 2020 David Miguel Susano Pinto <carandraug@gmail.com>
##
## This file is part of Microscope.
##
## Microscope is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## Microscope is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Microscope.  If not, see <http://www.gnu.org/licenses/>.

"""This module is deprecated and only kept for backwards compatibility.
"""

from microscope import AxisLimits, Binning, ROI, TriggerMode, TriggerType

from microscope.abc import (
    DataDevice,
    DeformableMirror,
    Device,
    FloatingDeviceMixin,
    StageAxis,
    keep_acquiring,
)

from microscope.abc import (
    TRIGGER_AFTER,
    TRIGGER_BEFORE,
    TRIGGER_DURATION,
    TRIGGER_SOFT,
)

from microscope.abc import Camera as CameraDevice
from microscope.abc import Controller as ControllerDevice
from microscope.abc import FilterWheel as FilterWheelBase
from microscope.abc import Laser as LaserDevice
from microscope.abc import SerialDeviceMixin as SerialDeviceMixIn
from microscope.abc import Stage as StageDevice
from microscope.abc import TriggerTargetMixin as TriggerTargetMixIn

from microscope.device_server import device
