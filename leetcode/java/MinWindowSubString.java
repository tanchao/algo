import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class MinWindowSubString {
    public static void main(String[] args) {
        //System.out.println(minWindow("ADOBECODEBANC", "ABC"));

        System.out.println(minWindow("wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon", "ozgzyywxvtublcl"));
    }
    
    public static String minWindow(String s, String t) { // O(n^3)
        if (s==null || s.isEmpty()) return "";
        if (t==null || t.isEmpty()) return s;

        if (s.length() < t.length()) return "";

        String minWindow = s;
        boolean updated = false;
        for (int i=0; i <= s.length() - t.length(); i++) { // O(n)
            for (int j = i + t.length(); j <= s.length(); j++) { // O(n)
                String sub = s.substring(i, j);
                if (minWindow.length() >= sub.length() && containsAll(sub, t)) { // O(n)
                    updated = true;
                    minWindow = sub;
                }
            }
        }
        if (!updated) return "";
        return minWindow;
    }

    private static boolean containsAll(String sub, String t) { // O(n)
        Map<Character, Integer> subCC = parse(sub);
        Map<Character, Integer> tCC = parse(t);
        for (Entry<Character, Integer> entry: tCC.entrySet()) {
            if (subCC.containsKey(entry.getKey()) && subCC.get(entry.getKey()) >= entry.getValue()) continue;
            else return false;
        }
        return true;
    }

    private static Map<Character, Integer> parse(String s) {
        Map<Character, Integer> charCounts = new HashMap<>();
        for (char c: s.toCharArray()) {
            if (charCounts.containsKey(c)) {
                charCounts.put(c, charCounts.get(c) + 1);
            } else {
                charCounts.put(c, 1);
            }
        }
        return charCounts;
    }
}