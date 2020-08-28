class Solution1528 {
    public String restoreString(String s, int[] indices) {
    char[] res = new char[s.length()];
    for (int i : indices){
        res[indices[i]] = s.charAt(i);
    }
    return new String(res);
    }
}