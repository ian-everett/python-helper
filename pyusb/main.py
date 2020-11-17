'''
Using PyUSB

install pyusb with:-
pip install pyusb
'''
import usb.core
import usb.util
from hot_runner_card import HotRunnerCard

# STM USB vendor ID
USB_VENDOR_ID = 0x0483
# USB product ID for MoldMaster ComX card
USB_PRODUCT_ID = 0x5741
# Default endpoint address
USB_ENDPOINT_IN = (usb.util.ENDPOINT_IN | 1)
# Should be 2 but CHibios used 1, endpoint address
USB_ENDPOINT_OUT = (usb.util.ENDPOINT_OUT | 1)
# Connection timeout (in ms)
USB_TIMEOUT = 150
# PMS/MM message start { and end } for validation
MM_STX = 123
MM_ETX = 125
# Number of zones per data block
# Number of bytes per zone
USB_ZONES_PER_BLK = 16
USB_BYTES_PER_ZONE = 30


def detach_interfaces(dev, n_interfaces):
    '''
    Detach the kernel driver for each interface
    '''
    for i in range(n_interfaces):
        if dev.is_kernel_driver_active(i):
            dev.detach_kernel_driver(i)
            print("Detach interface %d" % i)

def check_for_valid_data(data):
    '''
    Check we look like the data is from a M3 Comms board
    '''
    # Data is always 512 and starts with { and ends with }
    if len(data) == 512 and data[0] == MM_STX and data[-1] == MM_ETX:
        return True
    return False

def parse_data(data):
    '''
    Extract the data from the raw data buffer
    '''
    block = data[1]
    print('Block %d' % block)

    # Extract zone data
    zone_data = data[2:(USB_ZONES_PER_BLK*USB_BYTES_PER_ZONE)+2]
    for i in range(0, len(zone_data), USB_BYTES_PER_ZONE):
        # Get each zones data
        zone = HotRunnerCard(i/USB_BYTES_PER_ZONE, zone_data[i:i+USB_BYTES_PER_ZONE])
        zone.get_values()

def main():
    '''
    Main entry point
    '''

    # Open M3 Comms board if present
    dev = usb.core.find(idVendor=USB_VENDOR_ID, idProduct=USB_PRODUCT_ID)
    if dev is None:
        raise ValueError('Device is not found')

    # Detach kernel driver from all interfaces if attached
    for config in dev:
        detach_interfaces(dev, config.bNumInterfaces)

    # set the active configuration. With no arguments, the first
    # configuration will be the active one
    dev.set_configuration()

    # send out some data
    n_bytes = dev.write(USB_ENDPOINT_OUT, '0', USB_TIMEOUT)
    print("%d bytes written" % n_bytes)

    # get data back
    data = dev.read(USB_ENDPOINT_IN, 512, USB_TIMEOUT)
    if check_for_valid_data(data):
        # Got valid data so parse into more meanigfull data
        parse_data(data)

    usb.util.dispose_resources(dev)

if __name__ == "__main__":
    main()
