import java.util.*;
class Solution {
    public String reverseVowels(String s) {
        int i = 0;
        int j = s.length() - 1;
        String vowels = "aeiouAEIOU";
        char[] StArr = s.toCharArray();
        while(i < j){
            if(vowels.contains(StArr[i] + "")){
                ;
            }else{i++;}
            if(vowels.contains(StArr[j] + "")){
                ;
            }else{j--;}
            if(vowels.contains(StArr[i] + "") && vowels.contains(StArr[j] + "")){
                char temp = StArr[i];
                StArr[i++] = StArr[j];
                StArr[j--] = temp;
            }
        }
        String ans = new String(StArr);
        return ans;
    }
}
