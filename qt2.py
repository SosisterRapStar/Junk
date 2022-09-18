# односвязный список
class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        if isinstance(next, StackObj):
            self.__next = next
        else:
            self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            node = self.top
            while node.next is not None:
                node = node.next
            node.next = obj

    def pop(self):
        if self.top is not None:
            if self.top.next is None:
                r = self.top
                self.top = self.top.next
                return r

            node = self.top
            node_prev = self.top
            while node.next is not None:
                node_prev = node
                node = node.next
            node_prev.next = None
            return node

    def get_data(self):
        if self.top is None:
            return []
        output_list = []
        node = self.top
        while node.next is not None:
            output_list.append(node.data)
            node = node.next
        output_list.append(node.data)
        return output_list


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj1"))
st.push(StackObj("obj1"))

print(st.pop())
res = st.get_data()    # ['obj1', 'obj2']
print(res)
