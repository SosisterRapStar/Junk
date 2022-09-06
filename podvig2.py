class Clock:
    __max_time = 100_000
    __min_time = 0

    def __init__(self, tm=0):

        if self.__check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        if type(tm) == int and tm >= cls.__min_time and tm < cls.__max_time:
            return True
        return False


clock = Clock(4530)
print(clock.get_time())
