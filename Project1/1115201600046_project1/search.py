# search.py
# ---------
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


#Κωνσταντίνα Έλληνα 1115201600046

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:"""

    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    # Xrhsh stoivas, wste na apothikeutoun ta paidia tou komvou kai epeita ta paidia twn paidiwn k.o.k.
    # Me auto ton tropo tha petyxoume thn anazhthsh kata vathos kai oxi kata platos
    frontier = util.Stack()
    explored = []

    # Xrhsh dictionary gia thn apothikeush ths theshs tautoxrona me to monopati ews ekei
    frontier.push({
        'state': start,
        'path': []
    })

    while True:
        if frontier.isEmpty():
            raise ValueError
        current = frontier.pop()
        node = current['state']
        path_until_now = current['path']
        if problem.isGoalState(node):
            # Ean vrethei h lysh exoume apeutheias to monopati ews th thesi pou vriskomaste kai to epistrefoume
            return path_until_now
        if node not in explored:  # Ean exoume exereunhsei ton komvo ton prospername
            explored.append(node)
            for state_position, next_move, cost in problem.getSuccessors(node):
                if state_position not in explored:  # Ean ena apo ta paidia exei exereunhthei to prospername
                    frontier.push({
                        'state': state_position,
                        'path': path_until_now + [next_move]
                        })

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    
    # H logikh einai akrivws idia me ton DFS, apla xrhsimopoioume oura
    # Etsi exereunountai prwta ola ta paidia tou komvou kai epeita ta paidia twn paidiwn (kata platos)
    frontier = util.Queue()
    explored = []

    frontier.push({
        'state': start,
        'path': []
    })

    while True:
        if frontier.isEmpty():
            raise ValueError
        current = frontier.pop()
        node = current['state']
        path_until_now = current['path']
        if problem.isGoalState(node):
            return path_until_now
        if node not in explored:
            explored.append(node)
            for state_position, next_move, cost in problem.getSuccessors(node):
                if state_position not in explored:
                    frontier.push({
                        'state': state_position,
                        'path': path_until_now + [next_move]
                        })

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    
    # Xrhsh ouras proteraiothtas se syndyasmo me BFS
    # Etsi apo ta paidia tou komvou akolouthame prwta auto me to xamhlotero kostos
    frontier = util.PriorityQueue()
    explored = []

    frontier.push({
        'state': start,
        'path': []
    }, 0)

    while True:
        if frontier.isEmpty():
            raise ValueError
        current = frontier.pop()
        node = current['state']
        path_until_now = current['path']
        if problem.isGoalState(node):
            return path_until_now
        if node not in explored:
            explored.append(node)
            for state_position, next_move, cost in problem.getSuccessors(node):
                if state_position not in explored:
                    movement = path_until_now + [next_move]
                    priority = problem.getCostOfActions(movement)  # Ti kostos tha exei h kinhsh gia na ftasw sto paidi
                    frontier.push({
                        'state': state_position,
                        'path': movement
                        }, priority) # To xrhsimopoiw ws priority gia thn PriorityQueue


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    
    # Idia logikh me to uniformCost
    # H monadikh allagh einai na prosthesw to heuristic sto kostos ths epomenhs kinhshs
    frontier = util.PriorityQueue()
    explored = []

    frontier.push({
        'state': start,
        'path': []
    }, 0)

    while True:
        if frontier.isEmpty():
            raise ValueError
        current = frontier.pop()
        node = current['state']
        path_until_now = current['path']
        if problem.isGoalState(node):
            return path_until_now
        if node not in explored:
            explored.append(node)
            for state_position, next_move, cost in problem.getSuccessors(node):
                if state_position not in explored:
                    movement = path_until_now + [next_move]
                    priority = problem.getCostOfActions(movement) + heuristic(state_position, problem)  # Edw
                    frontier.push({
                        'state': state_position,
                        'path': movement
                        }, priority)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
