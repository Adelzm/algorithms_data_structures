from data_structures.linked_list import *
from data_structures.doubly_linked_list import *

def main():
    my_doubly_linked_list = DoublyLinkedList(7)
    my_doubly_linked_list.prepend(8)
    my_doubly_linked_list.prepend(9)
    my_doubly_linked_list.insert(1, 5)
    my_doubly_linked_list.print_list()
    my_doubly_linked_list.remove(1)
    my_doubly_linked_list.print_list()

  



if __name__ == "__main__":
    main()

