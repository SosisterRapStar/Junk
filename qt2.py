
class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        if x[0] == 1:
            root = root.left
        else:
            root = root.right
        if x[root.indx] == 0:
            root = root.right
        else:
            root = root.left
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node != None:
            if left == True:
                node.left = obj

            else:
                node.right = obj
        return obj


# описание класса узла
class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx  # индекс закрепленный за деревом
        self.value = value  # строка
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left  # где значение - сслыка на объект

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)
