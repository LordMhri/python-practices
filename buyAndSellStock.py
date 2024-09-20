def maxProfit(prices:list[int]) -> int:
    minCost = prices[0]
    profit = 0
    
    for price in prices:
        if price < minCost:
            minCost = price
        else:
            profit = max(profit,price-minCost)
    
    return profit
        
    


price = [7,1,5,3,6,4]
print(maxProfit(price))


# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.