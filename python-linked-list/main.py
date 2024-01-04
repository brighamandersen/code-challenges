from linked_list import LinkedList


def main():
    linked_list = LinkedList()
    linked_list.insert_at_head(20)
    print(linked_list)
    linked_list.insert_at_tail(5)
    print(linked_list)
    linked_list.clear()
    print(linked_list)
    linked_list.insert_at_head(10)
    print(linked_list)
    linked_list.insert_at_tail(35)
    print(linked_list)
    linked_list.delete_head()
    print(linked_list)
    linked_list.delete_tail()
    print(linked_list)


if __name__ == '__main__':
    main()
