#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x19-peer_connection.json
# Device ID:          0x19
# Device Name:        connection
# Timestamp:          08/21/2019 @ 17:53:39.438882 (UTC)

from sphero_sdk.common.enums.connection_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter


def set_bluetooth_device_name(name, target, timeout): 
    return { 
        'did': DevicesEnum.connection,
        'cid': CommandsEnum.set_bluetooth_device_name,
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='name',
                data_type='std::string',
                index=0,
                value=name,
                size=1
            ),
        ],
    }


def get_bluetooth_device_name(target, timeout): 
    return { 
        'did': DevicesEnum.connection,
        'cid': CommandsEnum.get_bluetooth_device_name,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='name',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ]
    }


def get_bluetooth_advertising_name(target, timeout): 
    return { 
        'did': DevicesEnum.connection,
        'cid': CommandsEnum.get_bluetooth_advertising_name,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='name',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ]
    }
