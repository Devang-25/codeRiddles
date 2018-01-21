#!/bin/env python3


class Node(object):
    def __init__(self, data, _nextIdx=None):
        self.data = data
        self.next = _nextIdx

    def __str__(self):
        return "Node(data => '%s')" % self.data


class LinkedList(object):
    '''
    trigger a function python everytime attribute is accessed
    '''
    def __init__(self, tail_end='-1'):
        self.length = 0
        self.tail_end = tail_end
        # self.is_empty = self.is_empty()
        # self.info = None

    @property
    def is_empty(self):
        if self.length == 0:
            return True
        return False


    def form_list(self, data_points=[]):
        head = None
        current = None
        if not data_points:
            data = input("Enter node data: ")
            current = head = Node(data)
            while data != self.tail_end:
                data = input("Enter node data: ")
                current.next = Node(data)
                current = current.next
        else:
            data_points = [str(i) for i in data_points]
            assert data_points[-1] == self.tail_end
            assert len(data_points) > 1
            current = head = Node(data_points[0])
            for data in data_points[1:]:
                current.next = Node(data)
                current = current.next
        # yield head
        self.head = head
        self.tail = current
        self.length += len(data_points)
        
# How to make object attribute refer call a method
# https://stackoverflow.com/questions/3166773/python-how-to-make-object-attribute-refer-call-a-method

LL = LinkedList()
print(LL.is_empty)
LL.form_list([43,2,-1]);
print(LL.is_empty)

