'''
Defines a rectangle class
'''
class Rectangle:
    '''
    Rectangle Class
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        '''
        return the area
        '''
        return self.width * self.height
    