# My solution but wrong, passed first 3 test cases but not with other inputs

def coinChange(coins, amount):
        coins= sorted(coins)
        print("Coins:",coins)
        amountOfCoins= 0
        for coin in range(len(coins)-1, -1, -1):
            while coins[coin] <= amount:
                amount -= coins[coin]
                amountOfCoins += 1
        if amountOfCoins > 0:
            return amountOfCoins
        return -1
        
coinChange([186,419,83,408], 6249)