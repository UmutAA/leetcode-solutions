class Remove_Element{
    public int removeElement(int[] nums, int val) {
        int cur = 0;
        int pos = nums.length - 1;
        
        while (cur <= pos) {
            if (nums[cur] == val) {
                nums[cur] = nums[pos];
                pos--;
            } else cur++;
        }
        return cur;
    }
}