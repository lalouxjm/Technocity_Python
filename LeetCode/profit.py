prices = [7,1,5,3,6,4]


def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    sell = profit = 0

    for price in prices:

        if price < buy:
            buy = price
            sell = 0

        if price > sell:
            sell = price

        if sell - buy > profit:
            profit = sell - buy

    return profit

print(maxProfit(prices))