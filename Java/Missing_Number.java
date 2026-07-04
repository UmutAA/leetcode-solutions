public class Missing_Number {
    public int missingNumber(int[] nums) {
        // sum of all elements should be n(n+1)/2
        int expectedSum = nums.length * (nums.length + 1) / 2;
        int sum = 0;
        for (int i = 0; i < nums.length; i++){
            sum += nums[i];
        }
        return expectedSum - sum;
    }
}
