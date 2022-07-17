import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

/*
 * VO 2 coding，给了一堆卡片(楼主写python 卡片用tuple表示），每个卡片有4个attribute，
 * 每个attribute有三个value(0,1,2)。三个满足条件的卡片可以凑成一个卡片组合。给一堆卡片，
 * 问最多能凑成多少组合。条件是: 
 * i.三张的每个attri都一样 或者 
 * ii.三个卡片的每个attri都不同
 * 
 * eg：满足条件的组合：
 * (0,0,2‍‍‌‌‌‌‌‌‍‍‌‍‌‌‍‍‌,1),
 * (0,1,2,1),
 * (0,2,2,1)
 * 因为每个attribute（每一列）都相同或者都不同。
 * 先用dfs解，复杂度高。提示以后发现任意两张卡片是可以满足条件的，通过前两张卡片就可以得出唯一满足条件的第三张卡片。复杂度可以从O(N^3) -> O(N^2)
 */
public class CardGame {
    public int allCards(int[][] cards) {
        Arrays.sort(cards, (a,b) -> a[0] - b[0] + a[1] - b[1] + a[2] - b[2] + a[3] - b[3]);
        int len = cards.length;
        Set<int[]> cardSet = new HashSet<>();
        for (int[] card: cards) {
            cardSet.add(card);
        }
        List<int[][]> res = new LinkedList<>();
        for (int i = 0; i < len - 2; i++) {
            for (int j = i + 1; j < len - 1; j++) {
                // if target exist
                int[] target = target(cards[i], cards[j]);
                if (isLarger(target, cards[i]) && isLarger(target, cards[j])) {
                    if (containsTarget(cardSet, target)) {
                        int[][] cur = {cards[i], cards[j], target};
                        res.add(cur);
                    } 
                }

            }
        }
        for (int[][] r: res) System.out.println(Arrays.deepToString(r));
        return res.size();
    }

    private boolean isLarger(int[] a, int[] b) {
        return a[0] - b[0] + a[1] - b[1] + a[2] - b[2] + a[3] - b[3] > 0;
    }

    private boolean containsTarget(Set<int[]> S, int[] T) {
        for (int[] c: S) 
            if (Arrays.equals(c, T)) 
                return true;
        return false;
    }

    private int[] target(int[] c1, int[] c2) {
        int[] c3 = new int[4];
        for (int i = 0; i < c1.length; i++) {
            if (c1[i] == c2[i]) c3[i] = c1[i];
            else c3[i] = 3 - c1[i] - c2[i];
        }
        return c3;
    }

    public int allCardsBrute(int[][] cards) {
        int len = cards.length;
        List<int[][]> res = new LinkedList<>();
        for (int i = 0; i < len - 2; i++) {
            for (int j = i + 1; j < len - 1; j++) {
                for (int k = i + 2; k < len; k++) {
                    if (isTuple(cards[i], cards[j], cards[k])) {
                        int[][] cur = {cards[i], cards[j], cards[k]};
                        res.add(cur);
                    }
                }
            }
        }
        return res.size();
    }

    private boolean isTuple(int[] c1, int[] c2, int[] c3) {
        int i = -1;
        while (i++ < 3) {
            if (c1[i] == c2[i] && c2[i] == c3[i]) continue;
            if (c1[i] != c2[i] && c2[i] != c3[i] && c1[i] != c3[i]) continue; // sum = 3?
            return false;
        }
        return true;
    }

    public void quickTest() {
        int[] a = {1,2,3};
        int[] b = {1,2,3};
        Set<int[]> s = new HashSet<>();
        s.add(a);
        System.out.println(a == b);
        System.out.println(s.contains(a));
        System.out.println(s.contains(b));
    }

    public static void main(String[] args) {
        int[][] cards = {
            {0,0,2,1},
            {0,1,2,1},
            {0,2,2,1},
            {0,2,1,1},
            {0,2,0,1}
        };
        CardGame cg = new CardGame();
        //cg.quickTest();
        System.out.println(cg.allCards(cards));
        System.out.println(cg.allCardsBrute(cards));
    }
}

class Card {
    int a;
    int b;
    int c;
    int d;
    public Card(int[] ins) {
        a = ins[0];
        b = ins[1];
        c = ins[2];
        d = ins[3];
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Card) {
            Card C = (Card) o;
            return this.a == C.a && this.b == C.b && this.c == C.c && this.d == C.d;
        }
        return false;
    }
}
