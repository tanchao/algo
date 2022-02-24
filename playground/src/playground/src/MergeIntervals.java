package playground.src;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
    public static int[][] merge(int[][] intervals) {
        int curStart = -1, curEnd = -1;
        int preStart = -1, preEnd = -1;
        List<List<Integer>> outputLists = new ArrayList<List<Integer>>();
        for (int[] interval : intervals) {
            if (interval != null && interval.length > 0) {
                // init
                preStart = curStart;
                preEnd = curEnd;
                curStart = interval[0];
                curEnd = interval[interval.length - 1];
                System.out.println(curStart + ", end" + curEnd);
                // merge logic
                if (preEnd >= 0) { // not initial set up
                    if (preEnd >= curStart) { // need merge
                        curStart = preStart;
                        System.out.println(curStart + ", end" + curEnd);
                    } else { // no need merge, store it
                        List<Integer> preInterval = Arrays.asList(preStart, preEnd);
                        outputLists.add(preInterval);
                        System.out.println(curStart + ", end" + curEnd);
                        System.out.println(outputLists);
                    }
                }
            }
        }
        int[][] outputs = new int[outputLists.size()][];
        for (int i = 0; i < outputLists.size(); i++) {
            List<Integer> mergedInterval = outputLists.get(i);
            outputs[i] = mergedInterval.stream().mapToInt(x -> x).toArray();
        }
        return outputs;
    }
}

class Solution {
    public static void main(String[] args) {
        int[][] inputs = { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };
        int[][] outputs = { { 1, 6 }, { 8, 10 }, { 15, 18 } };
        int[][] result = MergeIntervals.merge(inputs);
        System.out.println(outputs.equals(result));
    }
}
