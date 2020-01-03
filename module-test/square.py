'''
Defines a square class
'''
from rectangle import Rectangle

class Square(Rectangle):
    '''
    Square Class
    '''
    def __init__(self, width):
        super().__init__(width, width)
