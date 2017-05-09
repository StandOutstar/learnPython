#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue:
    def __init__(self,size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def full(self):
        if self.tail - self.head == self.size:
            return True
        else:
            return False

    def empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def inqueue(self, content):
        if self.full():
            print("queue is full!")
        else:
            self.queue.append(content)
            print("inQueue: ", content)
            self.tail += 1
            print("now head = ", self.tail)

    def outqueue(self):
        if self.empty():
            print("queue is empty!")
        else:
            print("outQueue: ", self.queue.pop(0))
            self.tail -= 1

if __name__ == '__main__':
    q = Queue(5)
    q.inqueue(1)
    q.inqueue(2)
    q.inqueue(3)
    q.inqueue(4)
    q.inqueue(5)
    q.outqueue()
    q.inqueue(6)

    q.outqueue()
    q.outqueue()
    q.outqueue()
    q.outqueue()
    q.outqueue()
    q.outqueue()
