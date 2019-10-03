# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 07:13:47 2019

@author: kenzo
"""

from collections import defaultdict
from heapq import heappop, heappush
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_dic = defaultdict(int)
        self.msg_heap = []
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if len(self.msg_dic) > 10:
            del self.msg_dic[heappop(self.msg_heap)[1]]
        if message not in self.msg_dic.keys():
            self.msg_dic[message] = timestamp
            heappush(self.msg_heap, [timestamp, message])
            return True
        else:
            if timestamp - self.msg_dic[message] >= 10:
                self.msg_dic[message] = timestamp
                return True
            else:
                return False