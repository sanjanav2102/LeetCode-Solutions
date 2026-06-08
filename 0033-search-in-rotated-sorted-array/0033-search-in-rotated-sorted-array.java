class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int low =0 ; int high = n-1;
        while(low <= high){
            int mid = (low+high)/2;
            if(nums[mid] == target){
                return mid;
            }
            if(nums[low] <= nums[mid]){//left half is sorted
                if(nums[low] <= target && target <= nums[mid]){//left sort
                    high = mid-1;//eliminate right
                }
                else{//right is sorted
                    low = mid+1; //eliminate left
                }
            }
            else{//right is sorted
                if(nums[mid] <= target && target <= nums[high]){//right s
                    low = mid+1; //eliminate left
                }
                else{//left is sorted
                    high = mid-1; //eliminate right
                }
            }
           
        }
         return -1;
    }
}