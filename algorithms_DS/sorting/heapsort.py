#!/usr/bin/env python3

class HeapSort(object):
    """
    perform heap sort operation.
    """
    def __init__(self, ip):
        self.heap = ip
        self.size = len(ip)
        
    def __get_parent(self, ix):
        return (ix-1)//2

    def __get_children(self, ix):
        return 2*ix+1, 2*ix+2

    def _delete_element(self):
        pass

    def _add_element(self):
        pass

    def _check_nodes_children(self, x, y):
        if self.heap[x] < self.heap[y]:
            self.heap[x], self.heap[y] = self.heap[y], \
                                         self.heap[x]
    
    def _check_nodes_parent_child(self, i, x, y, single=False):
        if single:
            if self.heap[i] < self.heap[x]:
                self.heap[i], self.heap[x] = self.heap[x], \
                                             self.heap[i]
        else:
            self._check_nodes_children(x, y)
            if self.heap[i] < self.heap[x]:
                self.heap[i], self.heap[x] = self.heap[x], \
                                             self.heap[i]
            else:
                self.heap[i], self.heap[y] = self.heap[y], \
                                             self.heap[i]
            self._check_nodes_children(x, y)
        
    def sort_heap(self):
        for i in range(self.size):
            x,y = self.__get_children(i)
            if x >= self.size:
                break
            elif y >= self.size:
                self._check_nodes_parent_child(i, x, y,
                                               single=True)
                break
            else:
                self._check_nodes_parent_child(i, x, y)
        return self.heap


if __name__=='__main__':
    # ip = input("enter list of integers separated by space: ")
    # ip = [int(i) for i in ip.split()]
    ip = [3, 19, 1, 14, 8, 7]
    HS = HeapSort(ip)
    X = HS.sort_heap()
    print("sorted: %s" % X)
    X = HS.sort_heap()
    print("sorted: %s" % X)
    X = HS.sort_heap()
    print("sorted: %s" % X)
    X = HS.sort_heap()
    print("sorted: %s" % X)
    X = HS.sort_heap()
    print("sorted: %s" % X)
    X = HS.sort_heap()
    print("sorted: %s" % X)    
