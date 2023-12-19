#!/usr/bin/python3
"""This module defines a node class representing a singly linked list."""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): Data stored within the Node.
        next_node (Node): Reference to the next Node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node with data and a reference to the next Node.

        Args:
            data (int): The data to be stored in the Node.
            next_node (Node, optional): The next Node in the linked list (default is None).
        Raises:
            TypeError: If data is not an integer or if next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data stored in the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the reference to the next Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the reference to the next Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""This module defines a singly linked list."""


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The first Node of the linked list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout, one node number per line."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
