#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x11-system_info.json
# Device ID:          0x11
# Device Name:        system_info
# Timestamp:          08/21/2019 @ 17:53:39.439326 (UTC)

from sphero_sdk.common.enums.system_info_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter


def get_main_application_version(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_main_application_version,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='major',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='minor',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='revision',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
        ]
    }


def get_bootloader_version(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_bootloader_version,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='major',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='minor',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='revision',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
        ]
    }


def get_board_revision(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_board_revision,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='revision',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_mac_address(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_mac_address,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='macAddress',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ]
    }


def get_stats_id(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_stats_id,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='statsId',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_processor_name(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_processor_name,
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


def get_boot_reason(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_boot_reason,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='bootReason',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_last_error_info(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_last_error_info,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='fileName',
                data_type='uint8_t',
                index=0,
                size=32,
            ),
            Parameter( 
                name='lineNumber',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='data',
                data_type='uint8_t',
                index=2,
                size=12,
            ),
        ]
    }


def get_sku(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_sku,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='sku',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ]
    }


def get_core_up_time_in_milliseconds(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_core_up_time_in_milliseconds,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='upTime',
                data_type='uint64_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_event_log_status(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_event_log_status,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='logCapacity',
                data_type='uint32_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='numberOfBytesUsed',
                data_type='uint32_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='numberOfEventsInLog',
                data_type='uint32_t',
                index=2,
                size=1,
            ),
        ]
    }


def get_event_log_data(offset, count, target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_event_log_data,
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='offset',
                data_type='uint32_t',
                index=0,
                value=offset,
                size=1
            ),
            Parameter( 
                name='count',
                data_type='uint32_t',
                index=1,
                value=count,
                size=1
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='logData',
                data_type='uint8_t',
                index=0,
                size=9999,
            ),
        ]
    }


def enable_sos_message_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.enable_sos_message_notify,
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_sos_message_notify(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.sos_message_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='sosMessage',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_sos_message(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.get_sos_message,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='sosMessage',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def clear_sos_message(target, timeout): 
    return { 
        'did': DevicesEnum.system_info,
        'cid': CommandsEnum.clear_sos_message,
        'target': target,
        'timeout': timeout,
    }
