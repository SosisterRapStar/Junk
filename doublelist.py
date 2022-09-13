

class ObjList:
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
        elif self.tail == None:
            self.tail = obj
            self.head.set_next(self.tail)
            self.tail.set_prev(self.head)
        else:
            t_obj = self.tail
            self.tail = obj
            t_obj.set_next(self.tail)
            self.tail.set_prev(t_obj)

    def get_data(self):
        t = []
        ob = self.head
        if self.head.get_next() != None:
            while ob:
                t += [ob.get_data()]
                ob = ob.get_next()
            return t

    def remove_obj(self):
        self.tail = self.tail.get_prev()
        d = self.tail.get_next()
        self.tail.set_next(None)
        del d


ob = ObjList("данные 1")
lst = LinkedList()

lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
print(lst.get_data())
lst.remove_obj()
print(lst.get_data())
