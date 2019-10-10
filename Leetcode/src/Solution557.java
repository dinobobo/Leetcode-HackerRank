import java.util.*;
import java.lang.StringBuilder;
import java.lang.String;
public class Solution557 {
    public String reverseWords(String s) {
        String[] words = s.split("\\s+");
        for(int i = 0; i < words.length; i++){
            StringBuilder si = new StringBuilder();
            si.append(words[i]);
            words[i] = String.valueOf(si.reverse());
        }
        return String.join("",words);
    }
}