#!/bin/env python3

import unittest

# Enter node data: 4
# Enter node data: 2
# Enter node data: 6
# Enter node data: -1
# Data: 4, Next: Node(data=2)
# Data: 2, Next: Node(data=6)
# Data: 6, Next: Node(data=-1)

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
        # self.info = None

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
        if not data:
            return self.head.next
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
        if not data:
            return self.head.next
        else:
            data = str(data)
            cur = self.head
            while cur.next and cur.data != self.tail_end:
                if cur.data == data:
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
            print("inserting node after %s" % self.node)
            tmp = self.node.next
            self.node.next = Node(data)
            self.node = self.node.next
            self.node.next = tmp

        return self.get_all_nodenames()


class Test(unittest.TestCase):
    '''
    Test Cases
    '''
    LL = LinkedList()

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
        assert self.LL.add_node(452, after=2) == ['43', '2', '452', '-1']
        assert self.LL.add_node(869, after=43) == ['43', '869', '2', '452', '-1']
        assert self.LL.add_node(99) == ['43', '869', '2', '452', '99', '-1']
        assert self.LL.add_node(3034, after=99) == ['43', '869', '2', '452', '99', '3034', '-1']
        assert self.LL.add_node(10, new_tail_end=True) == ['43', '869', '2', '452', '99', '3034', '-1', '10']

    def test_get_node(self):
        assert self.LL.get_node('2').next.data == '452'

    def test_get_next_node(self):
        assert self.LL.get_next('2').next.data == '99'

    def test_tail_end_invalid_char(self):
        LL = LinkedList(tail_end='99')
        self.assertRaises(AssertionError, LL.form_list, [43,2,-1])
        # # or this way:
        # with self.assertRaises(AssertionError):
        #     LL.form_list([43,2,-1])

if __name__ == '__main__':
    # add nodes automatically
    unittest.main()

    # get user to add nodes
    # LL = LinkedList()
    # LL.form_list()
    # LL.print_all_nodes()

# .inserting node after Node(data => '2')
# inserting node after Node(data => '43')
# inserting node after Node(data => '99')
# ....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s
#
# OK
