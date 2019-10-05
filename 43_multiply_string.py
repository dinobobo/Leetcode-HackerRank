# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:28:21 2019

@author: kenzo
"""
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        ans = "0"
        j = len(num1) - 1
        k = 0
        while j >= 0:
            ans = self.add(ans, self.single_multi(num2 , num1[j]) + '0' * k) 
            k += 1
            j -= 1
        return ans
    def single_multi(self, single, num):
        j = len(num) - 1
        ans = ""
        carry = 0
        while j >= 0:
            carry, remain = divmod(int(single) * int(num[j]) + carry, 10)
            ans = str(remain) + ans
            j -= 1
        if carry:
            return str(carry) + ans
        else:
            return ans
        
    def add(self, num1, num2):
        if len(num1) < len(num2):
            s, l = num1, num2
        else:
            l, s = num1, num2
        s = '0'*(len(l) - len(s)) + s
        ans = ""
        carry = 0
        j = len(l) - 1
        while j >= 0:
            _sum = carry + int(s[j]) + int(l[j])
            if _sum >= 10:
                remain = _sum - 10
                carry = 1
            else:
                remain = _sum
                carry = 0
            ans = str(remain) + ans
            j -= 1
        if carry == 1:
            return "1" + ans
        else:
            return ans
'''

class Solution(object):
    def multiply(self, num1, num2):
        ans = [0 for _ in range(len(num1) + len(num2) + 1)]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                carry, remain = divmod(int(num1[i]) * int(num2[j]), 10)
                ans[i + j] += remain
                ans[i + j + 1] += carry
        for k in range(len(ans) - 1):
            carry, remain = divmod(ans[k], 10)
            if carry > 0:
                ans[k + 1] += carry
                ans[k] = remain
        n = len(ans) - 1
        while ans[n] == 0 and n >= 1:
            n -= 1
        res = ""
        for char in ans[:n+1]:
            res = str(char) + res
        return res

    
x = Solution().multiply('223', '22')