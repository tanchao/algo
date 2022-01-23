```
Part1: 一个player有5个颜色的tokens, 比如 2个蓝色的tokens和1个绿色的tokens可以购买一个cards. 那么你现在手上已经有的tokens可不可以买cards. 因为是一个OOD, tokens的数量都是自己设计, 然后购买cards的条件也是自己设计的. 然后写一个方程来判断是否可以买这个cards.
Part2: 和part1差不多, 只是要你打印出还剩下多少tokens 和 cards的数量
Part3: 和之前有些不一样了. 如果现在有2个绿色的card 然后2个绿色的tokens, 然后告诉你要3个绿色的票才能换 一个白色的card. 要你输出 你的钱包里面有哪些card和tokens. cards要先被消耗, 一个cards等于一个票. 所以最后的结果就是 一个白色的card 0个绿色的card 1个绿色的tokens.
```

```
abstractions:

part I:
entities: player, token, card
functions: canBuy(player, card)

part II:
+func: listTokens(player), listCards()
+entity: cardStore?

part III:
so the card's cost not limited to tokens, say:
it was:
card.price = List<Token>

now:
card.price = List<Item>

Item {
    getValue()
    equals()
}

Token extends Item
Card extends Item

```