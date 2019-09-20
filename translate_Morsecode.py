import string
from collections import defaultdict
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uniq_num = 0
        translate_dict = set()
        Morse_dict = self.Morse_dict()
        for i in words:
            translate = ""
            for j in i:
                translate += Morse_dict[j]
            translate_dict.add(translate)
        return len(translate_dict)
        
        
    def Morse_dict(self):
        Morse_dict = defaultdict(str)
        Morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for a, c in zip(string.ascii_lowercase, Morse_code):
            Morse_dict[a] = c
        return Morse_dict
