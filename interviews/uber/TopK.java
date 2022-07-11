import java.util.*;
import java.util.Map.Entry;

class TopK {

    public List<String> topKFrequent(String[] words, int k) {
        // build word: freq map
        Map<String, Integer> pairs = build(words);
        // sort with pq
        List<String> result = topKPQ(k, pairs);
        return result;
    }

    private List<String> topKPQ(int k, Map<String, Integer> pairs) {
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>((a, b) -> a.compareTo(b));
        for(Entry<String, Integer> entry: pairs.entrySet()) {
            pq.add(new Pair(entry.getKey(), entry.getValue()));
            if (pq.size() > k) pq.poll();
        }
        List<String> result = new LinkedList<>();
        while (!pq.isEmpty()) result.add(0, pq.poll().word);
        return result;
    }
    
    
    private Map<String, Integer> build(String[] words) {
        Map<String, Integer> pairs = new HashMap<>();
        for (String word: words) {
            if (!pairs.containsKey(word)) pairs.put(word, 1);
            else pairs.put(word, pairs.get(word) + 1);
        }
        return pairs;
    }
    
    class Pair {
        String word;
        int freq;
        
        public int compareTo(Pair o) {
            if (this.freq == o.freq) return -1 * this.word.compareTo(o.word);
            return this.freq - o.freq;
        }
        
        public Pair(String w, int f) {
            this.word = w;
            this.freq = f;
        }
    }

    private List<String> topKDQ(int k, Map<String, Integer> pairs) {
        Deque<Pair> dq = new LinkedList<Pair>();
        for(Entry<String, Integer> entry: pairs.entrySet()) {
            dq.addLast(new Pair(entry.getKey(), entry.getValue()));
            if (dq.size() > k) dq.removeFirst();
        }
        List<String> result = new LinkedList<>();
        while (!dq.isEmpty()) result.add(dq.removeFirst().word);
        return result;
    }

    class DLNode {
        DLNode left;
        DLNode right;
        String w;
        int f;
        public DLNode(String w, int f) {
            this.w = w;
            this.f = f;
        }
    }

    public static void main(String[] args) {
        TopK topK = new TopK();
        List<String> res = topK.topKFrequent(new String[]{"i","love","leetcode","i","love","coding"}, 2);
        System.out.println(res);
    }
}