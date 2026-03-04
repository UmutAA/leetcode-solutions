import java.util.Arrays;

public class Longest_Common_Prefix
    {
        public String longestCommonPrefix(String[] strs)
        {
            String retVal = new String();
            retVal = "";
            Arrays.sort(strs);
            String firstWord = strs[0];
            String lastWord = strs[strs.length - 1];
            int length = Math.min(firstWord.length(), lastWord.length());
            for (int i = 0; i < length; i++)
            {
                if (firstWord.charAt(i) == lastWord.charAt(i))
                    retVal = retVal + firstWord.charAt(i);
                else
                    break;
            }
            return retVal;
        }
        
    }