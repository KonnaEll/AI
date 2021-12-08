# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Κωνσταντίνα Έλληνα 1115201600046

"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop

from shop import FruitShop

def shopSmart(orderList, fruitShops):
    """orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops"""

    shop1 = fruitShops[0]

    # Compare the prices of the shops based on the result of the function getPriceOfOrder from class FruitShop that is given in shop.py
    minim = shop1
    for i in fruitShops:
        if i.getPriceOfOrder(orderList) <= minim.getPriceOfOrder(orderList):
            minim = i
    return minim # return the shop with the minimum price


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    dir3 = {'apples': 1.5, 'oranges': 2.0} # make a third shop that can win shop1 in the last question
    shop3 = shop.FruitShop('shop3', dir3)
    shops = [shop1, shop2, shop3]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())