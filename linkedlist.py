# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 08:29:25 2018

@author: DinoBob
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class LinkedList(Node):
    def __init__(self):
        self.headval = None
    def printlist(self):
        printnode = self.headval
        while printnode != None:
            print(printnode.val)
            printnode = printnode.next
    def newhead(self, node):
        newnode = Node(node)
        newnode.next = self.headval
        self.headval = newnode
    def insert(self, node):
        
        
            
            
if __name__ == '__main__':
    test = LinkedList()
    x = Node('Hello')
    x.next = Node('World')
    test.headval = x
    test.newhead('whats up')
    test.printlist()
        