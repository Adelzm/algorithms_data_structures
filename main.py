from data_structures.linked_list import *
from data_structures.doubly_linked_list import *

def main():
    my_doubly_linked_list = DoublyLinkedList(7)
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.append(5)

    my_doubly_linked_list.print_list()


if __name__ == "__main__":
    main()

