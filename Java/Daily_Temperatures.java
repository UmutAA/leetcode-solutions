import java.util.ArrayDeque;
import java.util.Deque;

public class Daily_Temperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        int length = temperatures.length;
        int answers[] = new int[length];

        Deque<Integer> stack = new ArrayDeque<>();
        for (int current = 0; current < length; current++)
        {
            while (!stack.isEmpty() && temperatures[current] > temperatures[stack.peek()])
            {
                int days = current - stack.peek();
                answers[stack.pop()] = days; 
            }

            stack.push(current);
        }
        return answers;
    }
}
