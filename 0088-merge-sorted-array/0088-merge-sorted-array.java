class Solution {
    public void bubblesort(int nums1[],int m){
        for(int i =0 ;i < m;i++){
            for(int j = 0;j < m-i-1;j++){
                if(nums1[j+1] < nums1[j]){
                    int temp;
                    temp = nums1[j+1];
                    nums1[j+1] = nums1[j];
                    nums1[j] = temp;
                }
                
            }

        }
    }
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i =m ; i < m+n ;i++){
            nums1[i] = nums2[i-m];
        }
        bubblesort(nums1,m+n);
        
    }
}