class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
            return

        curr_node = self.root
        while curr_node:
            if data < curr_node.data:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(data)
                    break
            elif data > curr_node.data:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(data)
                    break
            else:
                # data is already in the tree
                break

 #Додамо до класу Tree методи пошуку мінімального і максимального значення елементів в бінарному дереві пошуку:              
    def add_list(self, data_list):
        for data in data_list:
            self.add_node(data)
            
    def find_min(self):
        if not self.root:
            return None

        curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left

        return curr_node.data

    def find_max(self):
        if not self.root:
            return None

        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right

        return curr_node.data
    

#Розширимо функціонал класу Tree, додавши в нього метод видалення елементів в бінарному дереві пошуку
    def remove(self, value):
        # Знайти елемент, який потрібно видалити, і його батьківський елемент
        node, parent = self._find_node_with_parent(value)

        if node is None:
            # Якщо елемент не знайдено, то повернути False
            return False

        if node.left is None and node.right is None:
            # Якщо елемент не має нащадків, то просто видалити його
            if parent is None:
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif node.left is not None and node.right is not None:
            # Якщо елемент має двох нащадків, то замінити його на його наступника
            successor = node.right
        while successor.left is not None:
            successor_parent = successor
            successor = successor.left
        if node.right == successor:
            successor.left = node.left
        else:
            successor_parent.left = successor.right
            successor.left = node.left
            successor.right = node.right
        if parent is None:
            self.root = successor
        elif parent.left == node:
            parent.left = successor
        else:
            parent.right = successor
    else:
            # Якщо елемент має одного нащадка, то замінити його на цього нащадка
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            if parent is None:
                self.root = child
            elif parent.left == node:
                parent.left = child
            else:
                parent.right = child

        return True

    def _find_node_with_parent(self, value):
        node = self.root
        parent = None

        while node is not None:
            if node.value == value:
                return node, parent
            elif value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        return None, None
