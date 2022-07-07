package com.tanchao.playground;

import lombok.Data;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class Exchange {
    private static final PriorityQueue<Double> SELL_BOOK = new PriorityQueue<>(100);
    private static final PriorityQueue<Double> BUY_BOOK = new PriorityQueue<>(100, Collections.reverseOrder());
    private static final List<Double> TRADE_RECORDS = new ArrayList<>();

    public void sell(double price) {
        if (BUY_BOOK.peek() != null && BUY_BOOK.peek() > price) {
            System.out.println("willing to sell at: " + price);
            System.out.println("offer to buy at: " + BUY_BOOK.peek());
            TRADE_RECORDS.add(BUY_BOOK.poll());
            System.out.println("traded");
        } else {
            SELL_BOOK.add(price);
            System.out.println("willing to sell at: " + price);
        }
        System.out.println(SELL_BOOK);
    }

    public void buy(double price) {
        if (SELL_BOOK.peek() != null && SELL_BOOK.peek() < price) {
            System.out.println("willing to buy at: " + price);
            System.out.println("offer to sell at: " + SELL_BOOK.peek());
            TRADE_RECORDS.add(SELL_BOOK.poll());
            System.out.println("traded");
        } else {
            BUY_BOOK.add(price);
            System.out.println("willing to buy at: " + price);
        }
        System.out.println(BUY_BOOK);
    }

    public List<Double> getTrades() {
        return TRADE_RECORDS;
    }
}

@Data
class Offer {
    double price;
    long timestamp;
}

class SellOfferComparator implements Comparator<Offer> {
    @Override
    public int compare(Offer o1, Offer o2) {
        if (o1.price > o2.price) return -1;
        if (o1.price < o2.price) return 1;
        return 0;
    }
}
class BuyOfferComparator implements Comparator<Offer> {
    @Override
    public int compare(Offer o1, Offer o2) {
        if (o1.price > o2.price) return 1;
        if (o1.price < o2.price) return -1;
        return 0;
    }
}
