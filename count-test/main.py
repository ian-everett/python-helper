
# Find out correct way of using constants in Python
MAX_ZONES = 64
USB_ZONES_PER_BLK = 16


for i in range(MAX_ZONES):
    # Print zone
    print("zone %d" % i, end='\t')

    # Get block number
    block = i / USB_ZONES_PER_BLK
    print("block %d" % block, end='\n')
