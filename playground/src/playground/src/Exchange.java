package playground.src;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class Exchange {
    private static final PriorityQueue<Long> SELL_BOOK = new PriorityQueue<>(100);
    private static final PriorityQueue<Long> BUY_BOOK = new PriorityQueue<>(100, Collections.reverseOrder());
    private static final List<Double> TRADE_RECORDS = new ArrayList<>();
    public void sell(double price) {}
    public void buy(double price) {}

    public List<Double> getTrades() {
        return TRADE_RECORDS;
    }
    
    public static void main(String[] args) {
        System.out.println("hi");
    }
}