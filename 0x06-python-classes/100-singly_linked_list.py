#!/usr/bin/python3
"""Class that defines node of a singly linked list"""

 
class Node:
    """Represents a node"""

    def __init__(self, data, next_node=None):
        """initializes data"""
        self.__data = data
        if not type(data) is int:
            raise TypeError('data must be an integer')
        self.__next_node = next_node
        if next_node is not None:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """Retrieves data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the new data """
        if not type(data) is int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Retrieves node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets new next_node"""
        if value is not None or value != self.Node:
            raise TypeError('next_node must be a Node object')

"""class that defines singly linked list"""



class SinglyLinkedList:
    """Represents a singlylinked list"""

    def __init__(self):
        self.__head = None

    def print_list(head):
        """print linked list"""
        current = self.head
        while(current != None):
            print(current, end=" ")
            current = current.next

    def insertionSort(
