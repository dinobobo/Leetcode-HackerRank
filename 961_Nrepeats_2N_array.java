class Solution {
    public Integer repeatedNTimes(int[] A) {
        int k = 0;
        while((k + 3) < A.length){
            Integer ans = findRepeat(A, k, k+4);
            if(ans != null){
                return ans;
            }
            k +=4;
        }
        if (k < A.length){
            return findRepeat(A, k, A.length);
        } 
        return null;
    }
    
        
    public Integer findRepeat(int[] arr, int begin, int end){
        for(int i = begin; i < end - 1; i++){
            for(int j = i+1; j < end; j++){
                if(arr[i] == arr[j]){
                    return arr[i];
                }
            }
        }
        return null;        
    }
}