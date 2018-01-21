#!/bin/env python3

# Enter node data: 4
# Enter node data: 2
# Enter node data: 6
# Enter node data: -1
# Data: 4, Next: Node(data=2)
# Data: 2, Next: Node(data=6)
# Data: 6, Next: Node(data=-1)

import unittest


class Node(object):
    def __init__(self, data, _nextIdx=None):
        self.data = data
        self.next = _nextIdx

    def __str__(self):
        return "Node(data => '%s')" % self.data


class LinkedList(object):

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

    def get_if_next(self, data=''):
        if data:
            data = str(data)
            cur = self.head
            while cur.next and cur.data != self.tail_end:
                if cur.next.data == data:
                    return cur
                else:
                    cur = cur.next
        return None

    def get_next(self, data=''):
        # supports following input:
        # - of type str ..representing data part of a Node
        # - of type Node ..in case a Node is supplied as input
        if not data:
            return self.head.next
        else:
            if isinstance(data, Node):
                # data itself was a Node instance. so extract .data
                data = data.data
            else:
                data = str(data)
            cur = self.head
            while cur.next and cur.data != self.tail_end:
                if cur.data == data:
                    return cur.next
                else:
                    cur = cur.next
        return None

    def get_node(self, data=''):
        # supports following input:
        # - of type str ..representing data part of a Node
        if not data:
            return self.head.next
        else:
            if isinstance(data, Node):
                # data itself was a Node instance. so extract .data
                err = """ERROR: Input supplied [%s] is an instance of Node..
                .. while it should only represent data part of Node""" % (data)
                raise AttributeError(err)
            else:
                data = str(data)
            if data == self.tail.data:
                # print("asked for tail..")
                return self.tail
            cur = self.head
            while cur.next and cur.data != self.tail_end:
                if cur.data == data:
                    # print("\n.. found node with data %s" % data)
                    return cur
                else:
                    cur = cur.next
        return None

    def get_all_nodenames(self):
        nodes = []
        cur = self.head
        while cur.next and cur.data != self.tail_end:
            nodes.append(cur.data)
            cur = cur.next

        # append node with data == -1
        nodes.append(cur.data)
        return nodes

    def print_all_nodes(self):
        cur = self.head
        while cur.next and cur.data != self.tail_end:
            print("Data: %s, Next: %s" % (cur.data, cur.next))
            cur = cur.next

    def make_cycliic(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = self.head

    def remove_cycliic(self):
        cur = self.head
        while cur.next and cur.data != self.tail_end:
            cur = cur.next
        cur.next = None

    def add_node(self, data, after=None, new_tail_end=False):
        # todo: add support for before=''
        data = str(data)
        if not after:
            if not new_tail_end:
                # add it at the end, but just before tail with data = -1
                # save tail to temp var
                # from pdb import set_trace; set_trace()
                node_before_tail = self.get_if_next(self.tail_end)
                # insert new node at tail position
                node_before_tail.next = Node(data)
                # shift to tail (new node)
                new_node = node_before_tail.next
                # finally, update self.tail to refer to old tail again
                new_node.next = self.tail
                self.tail = new_node.next
            else:
                # # update LL termination char to 'data'
                # # add 1 reference to new node against old tail's next
                self.tail.next = Node(data)
                self.tail = self.tail.next
                self.tail_end = self.tail.data
        else:
            after = str(after)
            self.node = self.get_node(after)
            print("< insert after %s >" % self.node)
            tmp = self.node.next
            self.node.next = Node(data)
            self.node = self.node.next
            self.node.next = tmp

        self.length += 1
        return self.get_all_nodenames()

    def calculate_length_now(self, head=True, current=None):
        if self.is_empty:
            return 0
        else:
            if current is None and head is False:
                return 0
            else:
                if head is True:
                    current = self.head
                return 1 + self.calculate_length_now(head=False, current=current.next)


class Test(unittest.TestCase):
    '''
    Test Cases
    '''
    LL = LinkedList()

    def test_a_a_newlist_ops(self):
        assert self.LL.is_empty == True
        assert self.LL.length == 0
        assert self.LL.calculate_length_now() == 0

    def test_a_form_list(self):
        try:
            self.LL.form_list([43,2,-1])
        except Exception as e:
            self.fail("self.LL.form_list() raised %s unexpectedly!" % e)
        # if form_list() doesn't return anything,
        # This check would raise:
        # >> AssertionError: None != True
        # self.assertEquals(self.LL.form_list([43,2,-1]), True)

    def test_add_nodes(self):
        # after random element
        assert self.LL.add_node(452, after=2) == ['43', '2', '452', '-1']
        # after head
        assert self.LL.add_node(869, after=43) == ['43', '869', '2', '452', '-1']
        # just before tail, without any after= param
        assert self.LL.add_node(99) == ['43', '869', '2', '452', '99', '-1']
        # just before tail, but with after= param
        assert self.LL.add_node(3034, after=99) == ['43', '869', '2', '452', '99', '3034', '-1']
        # after tail, and assign a new tail_end
        assert self.LL.add_node(10, new_tail_end=True) == ['43', '869', '2', '452', '99', '3034', '-1', '10']

    def test_get_node(self):
        # get a particular node. test that the next node's data is as expected
        assert self.LL.get_node('2').next.data == '452'
        # get_node() with tail's data returns tail node instance itself
        tail_data = self.LL.tail.data
        assert self.LL.get_node(tail_data) == self.LL.tail
        # get_node doesn't accept Node instance. Only strings that represent data
        self.assertRaises(AttributeError, self.LL.get_node, self.LL.tail)
        # with self.assertRaises(AttributeError):
        #     self.LL.get_node(self.LL.tail)

    def test_get_next_node(self):
        # get a node after specified node
        assert self.LL.get_next('2').next.data == '99'
        assert self.LL.get_next(self.LL.tail) == None

    def test_tail_end_invalid_char(self):
        '''
        change tail_end to new value (99) as opposed to the default (-1)
        then form a linked list without the new tail end to see if it fails
        '''
        LL = LinkedList(tail_end='99')
        self.assertRaises(AssertionError, LL.form_list, [43,2,-1])
        # or this way:
        # with self.assertRaises(AssertionError):
        #     LL.form_list([43,2,-1])

    def test_z_length_ops(self):
        # after populating the LL, test the length and is_empty properties
        assert self.LL.is_empty == False
        assert self.LL.length == self.LL.calculate_length_now()


if __name__ == '__main__':
    # # get user to add nodes
    # LL = LinkedList()
    # LL.form_list()
    # LL.print_all_nodes()

    # add nodes automatically
    unittest.main()
