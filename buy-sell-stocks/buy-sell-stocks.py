def maxProfit(prices):
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):

        # Checking for lower buy value
        if (buy > prices[i]):
            buy = prices[i]

        # Checking for higher profit
        elif (prices[i] - buy > profit):
            profit = prices[i] - buy
    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    profit = maxProfit(prices)
    print(profit)
