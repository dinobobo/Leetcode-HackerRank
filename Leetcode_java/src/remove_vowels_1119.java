import java.util.*;
class Solution1119 {
    public static void main(String[] args) {
        String ans = removeVowels("xyzii");
        System.out.println(ans);
    }
    public static String removeVowels(String S) {
        HashSet<Character> h = new HashSet<>();
        h.add('a');
        h.add('e');
        h.add('i');
        h.add('o');
        h.add('u');;
        for(char c: S.toCharArray()){
            if(h.contains(c)){
                S = S.replace(c + "", "");
            }
        }
        return S;
    }
}
