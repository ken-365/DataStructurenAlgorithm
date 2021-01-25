# Uses python3
import sys

# %%
def get_change_slow(m):
    coins = [1,3,4]
    if m == 0:
        return 0
    MinNumCoins = float('inf')
    for i in range(len(coins)):
        if m >= coins[i]:
            numcoin = get_change_slow(m - coins[i])
            if numcoin +1 < MinNumCoins:
                MinNumCoins = numcoin +1

    return MinNumCoins

# print(get_change_slow(5))



# %%
def get_change(money):
    coins = [1,3,4]
    MinNumCoins = [0]  * ((money) +1 )
    for m in range(1,money+1): # fill in a list
        MinNumCoins[m] = math.inf
        for i in coins:
            if m>= i:
                numcoin = MinNumCoins[m - i] +1
                if numcoin < MinNumCoins[m]:
                    MinNumCoins[m] = numcoin
    return MinNumCoins[money]


# print(get_change(34))

# %% test
import math

money = 34
denominations = [1, 3, 4]
minCoins = [0] + [math.inf]*money

for i in range(1, money+1):
    for j in denominations:
        if i>=j:
            
            coins = minCoins[i-j]+1
            if coins < minCoins[i]:
                minCoins[i] = coins

# print(minCoins[money])

# %% Run
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))