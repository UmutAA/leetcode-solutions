int maxArea(int* height, int heightSize) {
    int l = 0;
    int r = heightSize - 1;
    int maxA = 0;
    while (l < r){
        int A;
        if (height[l] < height[r]){
            A = (r - l) * height[l];
        }
        else {
            A = (r - l) * height[r];
        }
        if (maxA < A){
            maxA = A;
        }
        if (height[l] > height[r]) r--;
        else l++;
    }
    return maxA;
}