# Just singly-linked

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        return self.head

    def __getitem__(self, node_idx):
        out_of_range = node_idx < 0 or node_idx >= self.length
        if out_of_range:
            raise IndexError("Index out of range")

        current_node = self.head
        for _ in range(node_idx):
            current_node = current_node.next

        return current_node

    def insert_at_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    def insert_at_tail(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.head = new_node
        else:
            tail_idx = self.length - 1
            tail_node = self[tail_idx]
            tail_node.next = new_node
        self.length += 1

    def delete_head(self):
        second_node = self[1]
        self.head = second_node
        self.length -= 1

    def delete_tail(self):
        if self.length <= 1:
            self.clear()
        else:
            second_to_last_node = self[self.length - 2]
            second_to_last_node.next = None
            self.length -= 1

    # Delete all nodes from linked list
    def clear(self):
        self.head = None
        self.length = 0

    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.is_empty():
            return '--'

        output = ''
        current_node = self.head
        while current_node:
            output += f'{current_node.value}'
            if current_node.next:
                output += ' -> '
            current_node = current_node.next
        return output


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return f'{self.value}'
