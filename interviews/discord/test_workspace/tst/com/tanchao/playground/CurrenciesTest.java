package com.tanchao.playground;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class CurrenciesTest {
    Currencies testCurrencies;

    @BeforeEach
    public void init() {
        testCurrencies = new Currencies();
    }

    @Test
    public void test_happyCase() {
        ExchangeOffer offer1 = new ExchangeOffer("BTC", "USD", 50000, 50005);
        ExchangeOffer offer2 = new ExchangeOffer("BTC", "ETH", 500, 500.1);
        ExchangeOffer offer3 = new ExchangeOffer("ETH", "USD", 500, 502);
        ExchangeOffer offer4 = new ExchangeOffer("ETH", "DOG", 234, 235);
        testCurrencies.accept(offer1);
        testCurrencies.accept(offer2);
        testCurrencies.accept(offer3);
        testCurrencies.accept(offer4);
        testCurrencies.maxProfitExchangePath("BTC", "USD");
    }
}
