import java.util.*;
import java.util.Map.Entry;

class Test {
    public static void main(String[] args) {
        Map<String, Integer> pairs = new HashMap<>();
        for(Entry entry: pairs.entrySet()) {
            entry.getKey();
        }

    }

    class Pair {
        String word;
        int freq;

        public int compare(Pair o) {
            if (Integer.compare(this.freq, o.freq) == 0) return this.word.compareTo(o.word);
            return Integer.compare(this.freq, o.freq);
        }
    }
}