# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
from random import randint

coins = []
numberOfCoins = 10
def FillList(coins: list, numberOfCoins: int):
    for i in range(0,numberOfCoins):
        coins.append(randint(0,1))
    return coins

def HeadsOrTails (coins: list, count_Heads = 0):
    if coins.count(1) > len(coins)/2:
        return coins.count(0)
    else:
        return coins.count(1)

print(FillList(coins, numberOfCoins))
print(HeadsOrTails(coins))

