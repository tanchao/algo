package uber;

import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

public class CheapestFlight {
    static Map<Integer, Map<Integer, Integer>> flightGraph = new HashMap<>();
    static int cheapest = Integer.MAX_VALUE;

    public static int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        buildFlightGraph(flights);
        dfsCheapest(src, dst, k + 1, 0);

        System.out.println("DFS result:" + cheapest);
        System.out.println("BFS result:" + bfs(flights, src, dst, k + 1));
        System.out.println("Dijkstra result:" + dijkstra(flights, src, dst, k + 1));
        return cheapest == Integer.MAX_VALUE ? -1 : cheapest;
    }

    private static void dfsCheapest(int src, int dst, int stops, int cost) {
        if (stops < 0) return;
        if (src == dst) {
            cheapest = Math.min(cost, cheapest);
            return;
        }
        if (!flightGraph.containsKey(src)) return;

        for (int next : flightGraph.get(src).keySet()) {
            int cur = flightGraph.get(src).get(next);
            if (cost + cur >= cheapest) continue;
            dfsCheapest(next, dst, stops - 1, cost + cur);
        }
    }

    private static int dijkstra(int[][] flights, int src, int dst) {
        Queue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] it, int[] that) {
                return it[1] - that[1]; // cost
            }
        });
        Set<int[]> visited = new HashSet<>();
        Map<Integer, Integer> costs = new HashMap<>();
        for (int[] f: flights) {
            if (!costs.containsKey(f[0])) costs.put(f[0], Integer.MAX_VALUE);
            if (!costs.containsKey(f[1])) costs.put(f[1], Integer.MAX_VALUE);
        } // preset all costs to max
        Map<Integer, Set<int[]>> map = build(flights);

        q.offer(new int[]{src, 0, 0});

        int min = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int stop = cur[0], cost = cur[1], count = cur[2];
            if (costs.get(stop) <= cost) continue;
            else costs.put(stop, cost);
            if (visited.contains(cur)) continue;
            visited.add(cur);
            if (stop == dst) {
                min = Math.min(min, cost);
            }
            if (!map.containsKey(stop)) continue;
            for (int[] f : map.get(stop)) {
                q.offer(new int[]{f[0], cost + f[1], count + 1});
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }

    private static int bfs(int[][] flights, int src, int dst, int k) {
        Queue<int[]> q = new LinkedList<>();
        Map<Integer, Set<int[]>> map = build(flights);
        Set<int[]> visited = new HashSet<>();
        q.offer(new int[]{src, 0, 0});
        int min = Integer.MAX_VALUE;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (cur[2] > k) continue;
            if (visited.contains(cur)) continue;
            visited.add(cur);
            if (cur[0] == dst) {
                min = Math.min(min, cur[1]);
            }
            if (!map.containsKey(cur[0])) continue;
            for (int[] f : map.get(cur[0])) {
                if (cur[1] + f[1] >= min) continue;
                q.offer(new int[]{f[0], cur[1] + f[1], cur[2] + 1});
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }

    private static Map<Integer, Set<int[]>> build(int[][] flights) {
        Map<Integer, Set<int[]>> map = new HashMap<>();
        for (int[] f : flights) {
            if (map.containsKey(f[0])) {
                map.get(f[0]).add(new int[]{f[1], f[2]});
            } else {
                Set<int[]> set = new HashSet<>();
                set.add(new int[]{f[1], f[2]});
                map.put(f[0], set);
            }
        }
        return map;
    }

    private static void buildFlightGraph(int[][] flights) {
        for (int[] flight : flights) {
            int src = flight[0], dst = flight[1], price = flight[2];
            if (flightGraph.containsKey(src)) {
                flightGraph.get(src).put(dst, price);
            } else {
                Map<Integer, Integer> map = new HashMap<>();
                map.put(dst, price);
                flightGraph.put(src, map);
            }
        }
    }

    public static void main(String[] args) {
        int[][] flights = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
        System.out.println(findCheapestPrice(4, flights, 0, 3, 1));
    }
}

class Stop {
    public int city;
    public int price;
    public int curCheapest;

    public Stop() {
    }

    public Stop(int city, int price) {
        this.city = city;
        this.price = price;
    }
}
