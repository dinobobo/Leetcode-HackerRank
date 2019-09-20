#use stack next time
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ""
        i = 0
        while i < len(S):
            left_p = 1
            right_p = 0
            j = i
            while left_p != right_p:
                j += 1
                if S[j] == "(":
                    left_p += 1
                else:
                    right_p += 1
            ans += S[i+1 : j]
            i = j + 1
        return ans