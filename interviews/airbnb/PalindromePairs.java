package airbnb;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

public class PalindromePairs {
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> pairs = new ArrayList<>();
        if (words == null || words.length < 2) return pairs;

        for (int i = 0; i < words.length - 1; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (isPalindrome(words[i] + words[j])) pairs.add(Arrays.asList(i, j));
                if (isPalindrome(words[j] + words[i])) pairs.add(Arrays.asList(j, i));
            }
        }
        return pairs;
    }

    private boolean isPalindrome(String merged) { // O(m)
        if (merged.isBlank() || merged.length() < 1) return true;

        for (int left = 0, right = merged.length() - 1; left < right; left++, right--) {
            if (merged.charAt(left) != merged.charAt(right)) return false;
        }
        return true;
    }

    public List<List<Integer>> palindromePairs2(String[] words) {
        List<List<Integer>> pairs = new LinkedList<>();
        if (words == null) return pairs;

        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; ++i) map.put(words[i], i); // Map<word, index>

        for (int i = 0; i < words.length; ++i) { // O(n)
            int l = 0, r = 0;
            while (l <= r) { // O(n)
                String s = words[i].substring(l, r);
                Integer j = map.get(new StringBuilder(s).reverse().toString());

                if (j != null && i != j && isPalindrome(words[i].substring(l == 0 ? r : 0, l == 0 ? words[i].length() : l)))
                    pairs.add(Arrays.asList(l == 0 ? new Integer[]{i, j} : new Integer[]{j, i}));

                if (r < words[i].length()) ++r;
                else ++l;
            }
        }
        return pairs;
    }
}