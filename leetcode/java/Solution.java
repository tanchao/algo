import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

public class Solution {
    public Solution() {}
    public int numBusesToDestination(int[][] routes, int source, int target) {
        // build graph
        Map<Integer, Set<Integer>> g = buildGraph(routes);
        // search route
        int num = bfsPQ(g, source, target);
        return num;
    }

    private int bfsPQ(Map<Integer, Set<Integer>> g, int src, int dst) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(final int[] it, final int[] that) {
                return Integer.compare(it[1], that[1]);
            }
        });
        pq.offer(new int[]{src, 0}); // stop, count
        Set<Integer> visited = new HashSet<>();
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int stop = cur[0], count = cur[1];
            if (visited.contains(stop)) continue;
            visited.add(stop);
            if (stop == dst) return count;
            if (!g.containsKey(stop)) continue;
            
            for (int next: g.get(stop)) {
                if (visited.contains(next)) continue;
                pq.offer(new int[] {next, count+1});
            }
        }
        return -1;
    }
    
    private int bfs(Map<Integer, Set<Integer>> g, int src, int dst) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{src, 0}); // stop, count
        int num = Integer.MAX_VALUE;
        Set<Integer> visited = new HashSet<>();
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int stop = cur[0], count = cur[1];
            if (visited.contains(stop)) continue;
            visited.add(stop);
            if (stop == dst) num = Math.min(num, count);
            if (!g.containsKey(stop)) continue;
            
            for (int next: g.get(stop)) {
                if (visited.contains(next)) continue;
                q.offer(new int[] {next, count+1});
            }
        }
        return num == Integer.MAX_VALUE ? -1 : num;
    }
    
    private Map<Integer, Set<Integer>> buildGraph(int[][] routes) {
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for (int[] route: routes) {
            for (int stop: route) {
                Set<Integer> others = new HashSet<>();
                for (int s: route) {
                    if (s != stop) others.add(s);
                }
                if (map.containsKey(stop)) {
                    map.get(stop).addAll(others);
                } else {
                    map.put(stop, others);
                }
            }
        }
        return map;
    }

    public static void main(String[] args) {
        int[][] routes = {{1,2,7},{3,6,7}};
        Solution s = new Solution();
        System.out.println(s.numBusesToDestination(routes, 1, 6));
    }
}