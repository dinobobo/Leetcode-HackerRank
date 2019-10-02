from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        #find the order of indices that will be revealled in the array, basically
        #simulate the process, anytime when we pop one index, assign the currents
        #smallese value in the array to it in the correspoding location.
        deck.sort()
        ans = [None]*len(deck)
        idx = deque(range(len(deck))) 
        for i in deck:
            ans[idx.popleft()] = i
            if idx:
                idx.append(idx.popleft())
        return ans