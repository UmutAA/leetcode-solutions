public class Remove_Duplicates_from_Sorted_Array {
    int removeDuplicates(int[] nums)
    {
        int length = nums.length;
        int i = 0, j = 1;
        while (j < length)
        {
            if (nums[j] != nums[i])
            {
                i++;
                nums[i] = nums[j];
            }
            j++;
        }
        return i + 1;
    }
}
