void moveZeroes(int* nums, int numsSize)
{
    int non_zero = 0;

    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != 0)
        {
            int temp = nums[i];
            nums[i] = nums[non_zero];
            nums[non_zero] = temp;
            non_zero++;
        }
    }
}