package com.tanchao.patreon;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class LRUPCache extends AbstractPCache implements IPCache<String, Integer> {
    private static final int CAPACITY = 1000;
    private static Map<String, DLNode> CACHE_MAP = new HashMap<>();
    private static DLNode head;
    private static DLNode tail;

    private static final Map<String, Integer> map = new LinkedHashMap<>(100, 0.75f, true);

    @Override
    public void put(String key, Integer value) {

    }

    @Override
    public Integer get(String key) {
        DLNode node = CACHE_MAP.get(key);
        if (node == null) { // doesn't exists
            if (CACHE_MAP.size() >= CAPACITY) {
                // remove key (tail)
                // insert newest
                //
            }
        } else {
            // remove key
            // insert to head
            return node.val;
        }
        return null;
    }
}

class DLNode {
    DLNode pre;
    DLNode next;
    String key;
    int val;
    long lastAccessTime; // System.currentTimeInMillis();
}
