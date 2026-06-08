class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int n = nums.length;
        int high = n-1;
        int ans = Integer.MAX_VALUE;
        while(low <= high){
            int mid = (high+low)/2;
            if(nums[low] <= nums[mid]){//left half is sorted
                ans = Math.min(nums[low],ans);
                low = mid+1; //left half eliminate
            }
            else{
                ans = Math.min(nums[mid],ans);
                high = mid-1; //right half eliminate
            }
        }

       return ans; 
    }
}