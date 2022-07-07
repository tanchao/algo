package com.tanchao.playground;

import lombok.Value;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Currencies {
    private static final Map<String, List<ExOffer>> ALL_CUR_RATES = new HashMap<>();

    public static final String PATHNAME = "/tmp/full.data.txt";
    public static final String DELIMITER = "->";

    // {"id":"WCFG-EUR","bids":[["1.31","3778.15","9"]],"asks":[["1.32","3853.76","11"]]}
    public static void main(String[] args) {
        System.out.println("test");
        File file = new File(PATHNAME);
        System.out.println(file.canRead());
        System.out.println(file.isFile());
        try {
            Scanner scanner = new Scanner(file);
            List<String> content = Files.readAllLines(Paths.get(PATHNAME));
            System.out.println(content.size());
            String first = content.get(0);
            //JSONReader jr = new JSONStreamReaderImpl()
            //JSONObject
            System.out.println("exit");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String maxProfitExchangePath(String from, String target) {
        Map<String, Double> exchangePaths = new HashMap<>();
        Set<String> visitedCurrencies = new HashSet<>();
        double initValue = 1.0;
        if (ALL_CUR_RATES.containsKey(from)) {
            traverse(from, target, from, initValue, exchangePaths, visitedCurrencies);
            if (!exchangePaths.isEmpty()) {
                double max = 1.0;
                String maxPath = "";
                for (Map.Entry<String, Double> entry : exchangePaths.entrySet()) {
                    if (entry.getValue() > max) {
                        max = entry.getValue();
                        maxPath = entry.getKey();
                    }
                }
                System.out.println("final result:");
                System.out.println("path:" + maxPath);
                System.out.println("value:" + max);
                System.out.println("exchangePaths:" + exchangePaths);
                return maxPath;
            }
        }
        System.out.println("no final result!");
        return "";
    }

    private void traverse(String from, String target, String prePath, Double preValue, Map<String, Double> exPaths, Set<String> visitedCurs) {
        if (visitedCurs.contains(from)) {
            return; // no need to continue
        } else {
            visitedCurs.add(from);
        }
        for (ExOffer offer : ALL_CUR_RATES.get(from)) {
            String other = offer.getOtherSymbol();
            String curPath = prePath + DELIMITER + other;
            Double curValue = preValue * offer.getPrice();
            if (target.equals(other)) { // success path
                System.out.println(curPath);
                exPaths.put(curPath, curValue);
            } else {
                traverse(other, target, curPath, curValue, exPaths, visitedCurs);
            }
        }
    }

    //{"btc-eth": {"bid": 123.0, "ask": 123.5}}
    public void accept(ExchangeOffer offer) {
        updateOfferRates(offer.getFromCur(), new ExOffer(offer.getToCur(), offer.getAsk()));
        updateOfferRates(offer.getToCur(), new ExOffer(offer.getFromCur(), offer.getBid()));
    }

    public void updateOfferRates(String symbol, ExOffer newOffer) {
        if (!ALL_CUR_RATES.containsKey(symbol)) {
            List<ExOffer> initOfferList = new ArrayList<>();
            ALL_CUR_RATES.put(symbol, initOfferList);
        }
        // todo: clarify update?
        List<ExOffer> offerList = ALL_CUR_RATES.get(symbol);
        offerList.add(newOffer);
    }

    public void accept(String offerStr) {
        ExchangeOffer offer = parse(offerStr);
        accept(offer);
    }

    private ExchangeOffer parse(String input) {
        return null;
    }
}

@Value
class ExchangeOffer {
    String fromCur;
    String toCur;
    double bid;
    double ask;
}

@Value
class ExOffer {
    String otherSymbol;
    double price;
}
