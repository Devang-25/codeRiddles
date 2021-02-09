#!/usr/bin/env python3

# import time
import threading
from random import shuffle

# https://leetcode.com/problems/print-in-order/

# Configure synchronous thread execution here
SYNC = False
# SYNC = True


def printFirst():
    print("first", end="")


def printSecond():
    print("second", end="")


def printThird():
    print("third", end="")


class Foo:
    def __init__(self):
        self.firstDone = False
        self.secondDone = False

    def first(self, printFirst) -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone = True

    def second(self, printSecond) -> None:

        if SYNC:
            while not self.firstDone:
                continue

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondDone = True

    def third(self, printThird) -> None:

        if SYNC:
            while not self.secondDone:
                continue

        # printThird() outputs "third". Do not change or remove this line.
        printThird()


FF = Foo()

# printFirst()
# printSecond()
# printThird()
#
# FF.first(printFirst)
# FF.second(printSecond)
# FF.third(printThird)

threads = [
    threading.Thread(target=FF.first, args=(printFirst,)),
    threading.Thread(target=FF.second, args=(printSecond,)),
    threading.Thread(target=FF.third, args=(printThird,)),
]

shuffle(threads)

[thread.start() for thread in threads]
[thread.join(timeout=3) for thread in threads]

print()

# time.sleep(0.2)
