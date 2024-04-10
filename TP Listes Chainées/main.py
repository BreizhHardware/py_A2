from listechainee import ListeChainee, polyCreux, nodeMonome


def main():
    # test_listechainee()
    test_polycreux()


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

def test_polycreux():
    pc = polyCreux(nodeMonome(6, 125))
    pc.add(nodeMonome(4, 125))
    pc.add(nodeMonome(4, 126))
    pc.add(nodeMonome(7, 3))
    pc.add(nodeMonome(9, 1))
    pc.add(nodeMonome(10, 0))
    pc.add(nodeMonome(44, 100))

    pc3 = polyCreux(nodeMonome(6, 2))
    pc3.add(nodeMonome(4, 1))
    pc3.add(nodeMonome(2, 0))
    e = pc.evaluate(1)
    print(e)
    e = pc.evaluate(-1)
    print(e)
    e = pc3.evaluate(1)
    print(e)
    e = pc3.evaluate(-1)
    print(e)

    pc.afficher()
    pc.multiply(3)
    pc.afficher()
    pc.delete_from_degre(125)
    pc.afficher()

    pc2 = polyCreux()
    pc2.add(nodeMonome(2, 125))
    pc2.add(nodeMonome(4, 101))
    pc2.add(nodeMonome(4, 1))
    pc2.add(nodeMonome(7, 0))
    print("affichage PC2")
    pc2.afficher()
    pc = pc - pc2
    print("affichage pc somme")
    pc.afficher()

    e = pc3(1)
    print(e)
    print(pc(1) + pc(0))

if __name__ == "__main__":
    main()
