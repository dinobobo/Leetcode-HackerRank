import static java.lang.Math.abs;
class Solution977 {
    public int[] sortedSquares(int[] A) {
        int[] ans = new int[A.length];
        int i = 0;
        int k = 0;
        while (i < A.length && A[i] < 0){i++;}
        int j = i - 1;
        while(j >= 0 && i < A.length){
            if(abs(A[j]) > abs(A[i])){
                ans[k] = A[i]*A[i];
                i++;
            }else{
                ans[k] = A[j]*A[j];
                j--;
            } 
            k++;
        }
        while(j >= 0){
            ans[k] = A[j]*A[j];
            k++;
            j--;
        }
        while(i < A.length){
            ans[k] = A[i]*A[i];
            k++;
            i++;
        }
        return ans;
    }
}