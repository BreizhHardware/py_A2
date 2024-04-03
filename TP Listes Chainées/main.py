from listechainee import ListeChainee


def main():
    test_listechainee()


def test_listechainee():
    LC = ListeChainee()
    LC.add_first(1)
    LC.add_first(2)
    LC.add_first(3)
    LC.add_last(35)
    LC.printLinkedList()
    LC.remove(2)
    LC.printLinkedList()
    print(LC.find(35))
    print(LC.size())
    print(LC.isEmpy())
    print(LC.find(2))
    LC.empty()
    print(LC.isEmpy())
    LC.printLinkedList()
    LC.add_first(35)
    LC.add_last(44)
    LC.printLinkedList()
    print(LC.number_of_occurrences(2))
    LC2 = ListeChainee()
    LC2.add_first(84)
    LC2.add_first(8463)
    LC2.printLinkedList()
    LC3 = LC + LC2
    LC3.printLinkedList()
    LC4 = ListeChainee()
    LC4.add_first(1)
    LC4.add_first(1)
    LC4.add_first(1)
    LC4.add_first(1)
    LC5 = LC3 + LC4
    LC5.printLinkedList()


if __name__ == "__main__":
    main()
