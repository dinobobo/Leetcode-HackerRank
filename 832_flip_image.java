class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int len = A[0].length;
        for(int[] row : A){
            for(int i = 0; i<(len + 1)/2; i++){
                int temp = row[i];
                row[i] = ~row[len - i - 1] + 2;
                row[len - i - 1] = ~temp + 2;
            }
        }
        return A;        
    }
}