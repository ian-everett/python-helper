'''
HotRunnerCard class
'''

class HotRunnerCard:
    '''
    HotRunnerCard message parser
    '''

    MODE_BITS = 0x1f

    def __init__(self, address, data):
        self.address = address
        self.message_length = data[0]
        self.actmode = self.parse_actmode(data[1])
        self.actual = self.parse_actual(data[2:4])
        self.actman = self.parse_actman(data[4])
        self.amps = self.parse_amps(data[5])

    def parse_actmode(self, data):
        ''' Parse actmode value from data stream'''
        val = data & HotRunnerCard.MODE_BITS
        if val > 15:
            val = 0
        return val

    def parse_actual(self, data):
        ''' Parse actual value from data stream'''
        val = data[0]
        val |= data[1] << 8
        return val

    def get_actual(self):
        ''' Returns the actual value '''
        return self.actual

    def parse_actman(self, data):
        ''' Parse the actman value from data stream '''
        return data / 2.5

    def parse_amps(self, data):
        ''' Parse the amps value from the data stream '''
        return data / 10.0

    def get_values(self):
        ''' output cards current values '''
        print("zone %d:" % self.address)
        if self.message_length:
            print('actual = %d' % self.actual)
            print('actmode = %d' % self.actmode)
            print('actman = %2.1f' % self.actman)
            print('amps = %2.1f' % self.amps)
        else:
            print('N/Z')

        print('')
