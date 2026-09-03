class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def delete(self, key):
        prev, current = None, self.head
        if current and current.data == key:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    tail = last_node = (self)
                    self._head = current.next
                    tail.next = self.head
                return
        prev = current
        current = current.next

    def iterate(self):
        if not self.head:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break
    def display(self):
        if not self.head:
            print("Circular linked list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

cll = CircularLinkedList()

cll.append(1)
cll.append(2)
cll.append(3)
cll.display()