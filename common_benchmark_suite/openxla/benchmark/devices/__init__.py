# Copyright 2023 The OpenXLA Authors
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from . import gcp_devices, host_devices

# All defined device specs.
ALL_DEVICES = gcp_devices.ALL_DEVICES + host_devices.ALL_DEVICES
