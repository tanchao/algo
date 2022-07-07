package com.tanchao.patreon;

public interface IPCache<K, V> {
    void put(K key, V value);
    V get(K key);
}
