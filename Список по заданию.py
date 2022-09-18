class Node:
    def __init__(self, element, next_node=None, prev_node=None):
        self.element = element
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList: # Интерфейс управления списками
    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head
        self.count = 0
        print("Вы создали пустой список")

    def add(self, element):
        self.count += 1
        if self.head == None:
            self.head = Node(element)
            print('Выполнение головы списка...')
            return ...
        elif self.tail == None:
            self.tail = Node(element, None, self.head)
            self.head.next_node = self.tail
            print('Выполнение хвоста списка...')
            return ...
        self.tail = Node(element, None, self.tail)
        self.tail.prev_node.next_node = self.tail

    def paste(self, element, index):
        i = 0
        node = self.head
        while i < index - 1:
            node = node.next_node
            i += 1

        node.next_node = Node(element, node.next_node, node)

    def out(self):
        node = self.head
        while node:
            print(node.element)
            node = node.next_node


lk = LinkedList()
lk.add(21)
lk.add(43)
lk.add(3232)
lk.add('dfdf')
lk.add(232)
lk.add(2112)
lk.add(98)
lk.paste(0, 2)
lk.paste(0, 1)
lk.paste(0, 4)
lk.out()
