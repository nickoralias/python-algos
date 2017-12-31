class Node:
    def __init__(self, data):
        self.data = str(data)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_end(self, data):
        node = Node(data)
        prev = None
        current = self.head

        while current:
            prev = current
            current = current.next

        if prev:
            prev.next = node
        else:
            self.head = node

    def add_at(self, data, index):
        node = Node(data)
        prev = None
        current = self.head

        while current:
            if index == 0:
                node.next = current
                if prev:
                    prev.next = node
                else:
                    self.head = node
                return True
            prev = current
            current = current.next
            index -= 1

        return False

    def delete_start(self):
        self.head = self.head.next if self.head else self.head

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
                else:
                    self.head = current.next
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
