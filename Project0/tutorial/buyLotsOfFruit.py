# buyLotsOfFruit.py
# -----------------
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


"""
To run this script, type

  python buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""
from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """orderList: List of (fruit, numPounds) tuples
    Returns cost of order"""

    totalCost = 0.0
    # Compare the fruits in the list with those in fruitPrices to see if they appear in fruitPrices
    # I calculate the totalCost with the summarize of the second item in the tuple and the price of that
    # t is a counter
    t = 0
    for i in fruitPrices:
        if orderList[0][0] == i:
            totalCost = totalCost + orderList[0][1] * fruitPrices[i]
            t = t + 1
        if orderList[1][0] == i:
            totalCost = totalCost + orderList[1][1] * fruitPrices[i]
            t = t + 1
        if orderList[2][0] == i:
            totalCost = totalCost + orderList[2][1] * fruitPrices[i]
            t = t + 1

    # If t is not 3 then some fruit doesn't appear in fruitPrices
    if t != 3:
        print("Error")
        return None

    return totalCost


# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
