
# Find out correct way of using constants in Python
max_zones = 128
zones_per_module = 12
zones_per_block = 4

for i in range(max_zones):
    # Print zone
    print("zone %d" % i, end='\t')

    # Get module number
    module = (i / zones_per_module)
    print(" module %d" % module, end='\t')

    # Get block number
    block = (i % zones_per_module) / zones_per_block
    print("  block %d" % block, end='\n')

