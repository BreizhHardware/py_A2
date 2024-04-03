class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListeChainee:
    def __init__(self, noeud = None):
        self.tete = noeud

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.tete
        self.tete = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.tete is None:
            self.tete = new_node
            return
        current = self.tete
        while current.next:
            current = current.next
        current.next = new_node

    def printLinkedList(self):
        current = self.tete
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def find(self, e):
        current = self.tete
        while current:
            if current.value == e:
                return True
            current = current.next
        return False

    def remove(self, data):
        current = self.tete
        if current.value == data:
            self.tete = current.next
            return
        while current.next:
            if current.next.value == data:
                current.next = current.next.next
                return
            current = current.next

    def isEmpy(self):
        return self.tete is None

    def size(self):
        current = self.tete
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def number_of_occurrences(self, e):
        current = self.tete
        count = 0
        while current:
            if current.value == e:
                count += 1
            current = current.next
        return count

    def empty(self):
        self.tete = None

    def __add__(self, other):
        current1 = self.tete
        current2 = other.tete
        LC = ListeChainee()
        while current1 or current2:
            val1 = current1.value if current1 else 0
            val2 = current2.value if current2 else 0
            LC.add_last(val1 + val2)
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
        return LC
