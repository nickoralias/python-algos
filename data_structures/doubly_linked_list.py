class Node:
    def __init__(self, data):
        self.data = str(data)
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if node.next:
            node.next.prev = node
        if not self.last:
            self.last = node

    def add_end(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.last = node
            return
        
        node.prev = self.last
        self.last.next = node
        self.last = node

    def add_at(self, data, index):
        node = Node(data)
        prev = None
        current = self.head

        while current:
            if index == 0:
                node.next = current
                if prev:
                    prev.next = node
                    node.prev = prev
                else:
                    self.head = node
                return True
            prev = current
            current = current.next
            index -= 1

        return False

    def delete_start(self):
        if self.head:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        prev = None
        current = self.head

        while current:
            prev = current
            current = current.next

        if prev:
            prev.next = None
        else:
            self.head = None

    def delete_at(self, index):
        prev = None
        current = self.head

        while current:
            if index == 0:
                if prev:
                    prev.next = current.next
                    current.next.prev = prev
                else:
                    self.head = current.next
                    self.head.prev = None
                return True
            prev = current
            current = current.next
            index -= 1

        return False

    def get(self, index):
        current = self.head

        while current:
            if index == 0:
                return current
            else:
                current = current.next
                index -= 1

        return None

    def index_of(self, data):
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def print(self, filename=None):
        current = self.head
        log = lambda str: print(str)

        if filename:
            file = open(filename, "w")
            log = lambda str: file.write(str)

        log("digraph BST {")

        while current and current.next:
            log("  " + current.data + " -> " + current.next.data)
            current = current.next

        if current:
            log("  " + current.data + " -> null")

        log("  null [shape=point]")
        log("}")

def main():
    arr = [9, 4, 2, 5, 8, 3, 1, 7, 6]
    lst = LinkedList()
    for i in arr:
        lst.add_start(i)
    lst.print()

if __name__ == "__main__":
    main()
