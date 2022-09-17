class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if (isinstance(x, float) or isinstance(x, int)) and (self.MIN_COORD <= x <= self.MAX_COORD):
            self.__x = x
        else:
            self.__x = 0
        if (isinstance(y, float) or isinstance(y, int)) and (self.MIN_COORD <= y <= self.MAX_COORD):
            self.__y = y
        else:
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, number):
        if isinstance(number, float) or isinstance(number, int):
            if self.MIN_COORD < number < self.MAX_COORD:
                self.__x = number

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, number):
        if isinstance(number, float) or isinstance(number, int):
            if self.MIN_COORD < number < self.MAX_COORD:
                self.__y = number

    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2


r = RadiusVector2D(-101, 1025)
print(r.x)
