class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)

        self.tail = new_node
        self.length += 1
    
    def remove_head(self):
        if self.head is None:
            return None
        current_val = self.head.get_value()
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.get_next()

        self.length -= 1
        return current_val

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            current_value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return current_value

        else:
            current_node = self.head
            while current_node.get_next() is not self.tail:
                current_node = current_node.get_next()
            current_value = self.tail.get_value()
            self.tail = current_node
            self.tail.set_next(None)
            self.length -= 1
            return current_value

    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        
        current_node = self.head
        current_max = self.head.get_value()

        while current_node is not None:
            if current_max <= current_node.get_value():
                current_max = current_node.get_value()
            current_node = current_node.get_next()

        return current_max

    def contains(self, value):
        if self.head is None:
            return False
        
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next()

        return False