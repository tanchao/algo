import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class BusRoutes {
    static Map<Integer, Set<Integer>> stopAccesses = new HashMap<>();
    static int min = Integer.MAX_VALUE;

    public static int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;
        int len = routes.length;

        List<List<Integer>> g = new ArrayList<>();
        for (int[] route: routes) {
            Arrays.sort(route);
            g.add(new ArrayList<>());
        }
        Set<Integer> seens = new HashSet<>(); // source routes
        Set<Integer> targets = new HashSet<>(); // target routes
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < len; i++) { // build interaction graph between routes
            for (int j=i+1; j<len; j++) {
                if (intersect(routes[i], routes[j])) {
                    g.get(i).add(j);
                    g.get(j).add(i);
                }
            }
        }

        for (int i = 0; i< len; i++) { // init seen and targets
            if (Arrays.binarySearch(routes[i], source) >= 0) {
                seens.add(i);
                q.offer(new int[]{i, 0});
            }
            if (Arrays.binarySearch(routes[i], target) >= 0) targets.add(i);
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int routeId = cur[0], count = cur[1];
            if (targets.contains(routeId)) return count + 1;
            for (int next: g.get(routeId)) {
                if (!seens.contains(next)) {
                    seens.add(next);
                    q.offer(new int[]{next, count + 1});
                }
            }
        }

        return -1;  
    }

    private static boolean intersect(int[] a, int[] b) {
        int i=0, j=0;
        while (i < a.length && j < b.length) {
            if (a[i] == b[j]) return true;
            if (a[i] < b[j]) i++; // both were sorted
            else j++;
        }
        return false;
    }

    public static int numBusesToDestination2(int[][] routes, int source, int target) {
        Set<Integer> routeStops;
        for (int[] route: routes) {
            routeStops = new HashSet<>();
            for (int stop: route) {
                routeStops.add(stop);
            }
            populateStopAccesses(routeStops);
        }
        dfs(source, target, 0);
        return min == Integer.MAX_VALUE ? -1 : min;    
    }

    private static void dfs(int src, int dst, int count) {
        if (src == dst) {
            min = Math.min(min, count);
            return;
        }
        if (!stopAccesses.containsKey(src)) return;
        for (int next: stopAccesses.get(src)) {
            if (count + 1 > min) continue;
            dfs(next, dst, count+1);
        }

    }

    private static void populateStopAccesses(Set<Integer> stops) {
        Set<Integer> others;
        for (int stop: stops) {
            others = new HashSet<>();
            stops.stream().filter(x -> x != stop).map(others::add);
            if (stopAccesses.containsKey(stop)) { // exists
                stopAccesses.get(stop).addAll(others);
            } else {
                stopAccesses.put(stop, others);
            }
        }
        System.out.println(stopAccesses.size());
    }

    public static void main(String[] args) {
        int[][] routes = {{1,2,7},{3,6,7}};
        System.out.println(numBusesToDestination(routes, 1, 6));
    }
}

class Node {
    public Set<Node> otherStops;
    public int stop;

    public Node(int stop) {
        this.stop = stop;
        this.otherStops = new HashSet<>();
    }

    public Node(int stop, Set<Node> otherStops) {
        this.stop = stop;
        this.otherStops = otherStops;
    }
}