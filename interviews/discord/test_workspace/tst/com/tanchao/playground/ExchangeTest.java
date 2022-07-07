package com.tanchao.playground;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ExchangeTest {
    @Test
    public void testExchange() {
        Exchange exchange = new Exchange();
        exchange.sell(99.9);
        exchange.sell(99.5);
        exchange.buy(99.0);
        exchange.buy(98.0);
        exchange.sell(97.0); // expect to trade happen with 99.0

        Assertions.assertEquals(1, exchange.getTrades().size());
    }
}
