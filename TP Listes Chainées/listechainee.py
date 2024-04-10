class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListeChainee:
    def __init__(self, noeud=None):
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


class nodeMonome:
    def __init__(self, coef, degre):
        self.coef = coef
        self.degre = degre
        self.next = None

    def get_coef(self):
        return self.coef

    def get_degre(self):
        return self.degre


class polyCreux:
    def __init__(self, monome=None):
        self.tete = monome

    def add(self, monome):
        if self.tete is None:
            self.tete = monome
            return
        if self.tete.degre < monome.degre:
            monome.next = self.tete
            self.tete = monome
            return
        current = self.tete
        while current:
            if current.degre == monome.degre:
                current.coef += monome.coef
                return
            if current.next is None or current.next.degre < monome.degre:
                monome.next = current.next
                current.next = monome
                return
            current = current.next

    def afficher(self):
        current = self.tete
        while current:
            if current.next is None:
                if current.degre == 0:
                    print(f"{current.coef}")
                    current = current.next
                elif current.degre == 1:
                    print(f"{current.coef}X")
                    current = current.next
                else:
                    print(f"{current.coef}X^{current.degre}")
                    current = current.next
            else:
                print(f"{current.coef}X^{current.degre}", end=" + ")
                current = current.next

    def evaluate(self, x):
        current = self.tete
        result = 0
        while current:
            result += current.coef * (x ** current.degre)
            current = current.next
        return result

    def multiply(self, scalar):
        current = self.tete
        while current:
            current.coef *= scalar
            current = current.next

    def delete_from_degre(self, degre):
        current = self.tete
        if current.degre == degre:
            self.tete = current.next
            return
        while current.next:
            if current.next.degre == degre:
                current.next = current.next.next
                return
            current = current.next

    def __add__(self, other):
        current1 = self.tete
        current2 = other.tete
        LC = polyCreux()
        while current1 or current2:
            degre1 = current1.degre if current1 else -1
            degre2 = current2.degre if current2 else -1
            if degre1 == degre2:
                LC.add(nodeMonome(current1.coef + current2.coef, degre1))
                current1 = current1.next
                current2 = current2.next
            elif degre1 > degre2:
                LC.add(nodeMonome(current1.coef, degre1))
                current1 = current1.next
            else:
                LC.add(nodeMonome(current2.coef, degre2))
                current2 = current2.next
        return LC

    def __sub__(self, other):
        current1 = self.tete
        current2 = other.tete
        LC = polyCreux()
        while current1 or current2:
            degre1 = current1.degre if current1 else -1
            degre2 = current2.degre if current2 else -1
            if degre1 == degre2:
                LC.add(nodeMonome(current1.coef - current2.coef, degre1))
                current1 = current1.next
                current2 = current2.next
            elif degre1 > degre2:
                LC.add(nodeMonome(current1.coef, degre1))
                current1 = current1.next
            else:
                LC.add(nodeMonome(-current2.coef, degre2))
                current2 = current2.next
        return LC
