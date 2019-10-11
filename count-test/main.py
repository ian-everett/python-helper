'''
How to use constants and enums
'''
from enum import Enum, unique

# Set some constants
MAX_ZONES = 64
USB_ZONES_PER_BLK = 16

for i in range(MAX_ZONES):
    # Print zone
    print("zone %d" % i, end='\t')

    # Get block number
    block = i / USB_ZONES_PER_BLK
    print("block %d" % block, end='\n')


# Setup a enum with unique numbers
@unique
class NetworkSetting(Enum):
    '''
    NetworkSettings constants
    '''
    IP_ADDRESS = 0
    NETMASK = 1


def set_settings():
    '''
    set_settings
    '''
    # There seems no gain doing things like this
    settings = {}
    settings[NetworkSetting.IP_ADDRESS] = '192.168.1.1'
    settings[NetworkSetting.NETMASK] = '255.255.255.1'

    # When this can be done
    settings2 = {}
    settings2['IP_ADDRESS'] = '192.168.1.1'
    settings2['NETMASK'] = '255.255.255.1'
