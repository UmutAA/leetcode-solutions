public class Remove_Duplicates_from_Sorted_Array {
    int removeDuplicates(int[] nums)
    {
        int k = 1;
        int length = nums.length;
        int i = 0, j = 1;
        while (j < length)
        {
            if (nums[j] != nums[i])
            {
                i++;
                nums[i] = nums[j];
                k++;
            }
            j++;
        }
        return k;
    }
}
