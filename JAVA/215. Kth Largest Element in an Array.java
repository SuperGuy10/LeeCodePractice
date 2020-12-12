/**
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

**/

class Solution {
    //Quick sort
    public int findKthLargest(int[] nums, int k) {
        int start = 0; 
        int end = nums.length-1;
        quickSort(nums, start, end);
        
        
        System.out.println(Arrays.toString(nums));
        return nums[nums.length-k];
    }
    
    
    public int findPivot(int[]nums, int start, int end){
        int pivot = nums[end];
        int i = start-1;
        for(int j = start; j<end; j++){
            if(nums[j]<pivot){
                i++;
                int tmp = nums[j];
                nums[j] = nums[i];
                nums[i] = tmp;
            }
        }
        int tmp = nums[i+1];
        nums[i+1] = pivot;
        nums[end] = tmp;
        return i+1;
    }
    
    public void quickSort(int[]nums, int start, int end){
        if(start<end){
            int p = findPivot(nums, start, end);
            
            quickSort(nums, start, p-1);
            quickSort(nums, p+1, end);
        }
    }
        
        
//     //Merge sort
//     public int findKthLargest(int[] nums, int k) {
//         int start = 0; 
//         int end = nums.length-1;
//         divide(nums, start, end);
        
//         System.out.println(Arrays.toString(nums));
//         return nums[nums.length-k];
//     }
    
//     public void divide(int[]nums, int start, int end){
//         if(start<end){
//             int mid = (start+end)>>>1;
//             divide(nums, start, mid);
//             divide(nums, mid+1, end);
//             combine(nums, start, end, mid);
//         }
//     }
    
//     public void combine(int[]nums, int start, int end, int mid){
//         int n1 = mid-start+1;
//         int n2 = end-mid;
//         int[]num1 = new int [n1];
//         int[]num2 = new int [n2];
        
//         for(int i = 0; i<n1; i++){
//             num1[i] = nums[start+i];
//         }
//         for(int j = 0; j<n2; j++){
//             num2[j] = nums[mid+j+1];
//         }
        
//         int i = 0, j=0, k = start;
//         while(i<n1 && j <n2){
//             if(num1[i]<num2[j]){
//                 nums[k++] = num1[i++];
//             }else{
//                 nums[k++] = num2[j++];
//             }
//         }
        
//         while(i<n1){
//             nums[k++] = num1[i++];
//         }
        
//         while(j<n2){
//             nums[k++] = num2[j++];
//         }
        
//     }

    
    
    // //Selection sort
    // public int findKthLargest(int[] nums, int k) {
    //     for(int i = 0; i<nums.length; i++){
    //         int j = i+1;
    //         int min = nums[i];
    //         while(j<nums.length){
    //             if(nums[j]<min){
    //                 int tmp = nums[i];
    //                 nums[i] = nums[j];
    //                 nums[j] = tmp;
    //                 min = nums[i];
    //             }
    //             j++;
    //         }
    //     }
    //     //System.out.println(Arrays.toString(nums));
    //     return nums[nums.length-k];
    // }
//     public int findKthLargest(int[] nums, int k) {
//         for(int i = nums.length; i>=0; i--){
//             int l = 0, r = l+1;
//             while(r<i){
//                 if(nums[r]<nums[l]){
//                     int tmp = nums[r];
//                     nums[r] = nums[l];
//                     nums[l] = tmp;
//                 }
//                 l = r;
//                 r = l+1;
              
//             }
//         }
//         //System.out.println(Arrays.toString(nums));
//         return nums[nums.length-k];
//     }
}
