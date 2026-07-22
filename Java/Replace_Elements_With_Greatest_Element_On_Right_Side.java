public class Replace_Elements_With_Greatest_Element_On_Right_Side{
    public int[] replaceElements(int[] arr) {
        int greatest = arr[arr.length - 1];
        for (int i = arr.length - 2; i > -1; i--){
            int num = arr[i];
            arr[i] = greatest;
            if (num > greatest){
                greatest = num;
            }
        }
        arr[arr.length - 1] = -1;
        return arr;
    }
}