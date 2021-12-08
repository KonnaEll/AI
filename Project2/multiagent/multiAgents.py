# multiAgents.py
# --------------
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
from typing import Any, Union

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        newfood = newFood.asList()  # vriskw thn apostash tou pacman apo to faghto
        food_dis = []
        for f in newfood:
            food_dis.append(manhattanDistance(newPos, f))  # xrhsimopoiw thn apostash manhattan

        if newfood:
            min_food_dis = 300 / min(food_dis)  # pairnw to mikrotero
        else:
            min_food_dis = 0

        ghost_dis = []  # vriskw thn apostash tou pacman apo to fantasmataki
        for i in newGhostStates:
            ghost_dis.append(manhattanDistance(newPos, i.getPosition()))
            if manhattanDistance(newPos, i.getPosition()) < 3:  # an einai konta sto fantasmataki
                return -1
        min_ghost_dis = min(ghost_dis)  # pairnw to mikrotero

        if ghost_dis > food_dis:  # an einai pio makria to fantasmataki prohgeitai to faghto
            score = min_food_dis * 300 + min_ghost_dis * 20
        else:
            score = min_food_dis * 20 + min_ghost_dis * 300

        scared = min(newScaredTimes)  # mikroterh kinhsh tou fovismenou
        score = score + scared * 50

        x, y = newPos  # syntetagmenes ths kainoyrgias theshs
        currentFood = currentGameState.getFood()
        if currentFood[x][y]:  # an yparxei faghto sto (x,y)
            return 100000000

        return score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        def maximum(gamestate, depth, index):   # gia to max
            if self.depth == depth or gamestate.isWin() or gamestate.isLose():  # ta states pou teleiwnei to paixnidi
                return self.evaluationFunction(gamestate), None

            legalActions = gamestate.getLegalActions(index)
            inf = -float("inf")     # -apeiro gia arxikh katastash
            LA = 0  # krataei tis kinhseis
            for i in legalActions:  # opws leitourgei o minimax gia thn kalyterh kinhsh
                succ = gamestate.generateSuccessor(index, i)
                agent = minimum(succ, depth, 1)
                if agent[0] > inf:  # an to min einai megalytero exw auta pou thelw
                    inf = agent[0]
                    LA = i
            return inf, LA

        def minimum(gamestate, depth, index):   # antistoixa gia to min
            if self.depth == depth or gamestate.isWin() or gamestate.isLose():
                return self.evaluationFunction(gamestate), None

            legalActions = gamestate.getLegalActions(index)
            finished = gamestate.getNumAgents() - 1     # fantasmatakia
            inf = float("inf")  # apeiro gia arxikh katastash
            LA = 0
            for i in legalActions:
                succ = gamestate.generateSuccessor(index, i)
                if index == finished:   # h teleiwnei h seira tou fantasmatos kai aujanei o depth
                    agent = maximum(succ, depth + 1, 0)
                else:   # h einai h seira tou epomenou fantasmatos
                    agent = minimum(succ, depth, index + 1)
                if agent[0] < inf:  # antistoixh sigkrisi me to apeiro
                    inf = agent[0]
                    LA = i
            return inf, LA

        return maximum(gameState, 0, 0)[1]  # kalw prwta to max, to opoio kalei to min kok..
                                            # etsi dhmiourgeitai to dentro pou orizei o minimax algorithmos

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # Akrivws to idio me to prohgoumeno mono pou edw xrhsimopoiw tis metavlhtes alpha, beta.

        alpha = -float("inf")
        beta = float("inf")

        def maximum(gamestate, depth, index, alpha, beta):
            if self.depth == depth or gamestate.isWin() or gamestate.isLose():
                return self.evaluationFunction(gamestate), None

            legalActions = gamestate.getLegalActions(index)
            inf = -float("inf")
            LA = 0
            for i in legalActions:
                succ = gamestate.generateSuccessor(index, i)
                agent = minimum(succ, depth, 1, alpha, beta)
                if agent[0] > inf:
                    inf = agent[0]
                    LA = i
                if beta < inf:      # edw, gia sigkrisi me to -apeiro
                    return inf, LA
                alpha = max(inf, alpha)
            return inf, LA

        def minimum(gamestate, depth, index, alpha, beta):
            if self.depth == depth or gamestate.isWin() or gamestate.isLose():
                return self.evaluationFunction(gamestate), None

            legalActions = gamestate.getLegalActions(index)
            finished = gamestate.getNumAgents() - 1
            inf = float("inf")
            LA = 0
            for i in legalActions:
                succ = gamestate.generateSuccessor(index, i)
                if index == finished:
                    agent = maximum(succ, depth + 1, 0, alpha, beta)
                else:
                    agent = minimum(succ, depth, index + 1, alpha, beta)
                if agent[0] < inf:
                    inf = agent[0]
                    LA = i
                if alpha > inf:     # edw, gia sigkrisi me to apeiro
                    return inf, LA
                beta = min(inf, beta)
            return inf, LA

        return maximum(gameState, 0, 0, alpha, beta)[1]  # opws einai o orismos tou algorithmou alphabeta

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        # Idia h maximum kai allazei mono h minimum ginetai expectimax

        def maximum(gamestate, depth, index):
            if self.depth == depth or gamestate.isWin() or gamestate.isLose():
                return self.evaluationFunction(gamestate), None

            legalActions = gamestate.getLegalActions(index)
            inf = -float("inf")
            LA = 0
            for i in legalActions:
                succ = gamestate.generateSuccessor(index, i)
                agent = expectimax(succ, depth, 1)
                if agent[0] > inf:
                    inf = agent[0]
                    LA = i
            return inf, LA

        def expectimax(gamestate, depth, index):    # opws o orismos ths expectimax gia na doume pws symperiferetai to fantasmataki
            if self.depth == depth or gamestate.isWin() or gamestate.isLose():
                return self.evaluationFunction(gamestate), None

            legalActions = gamestate.getLegalActions(index)
            finished = gamestate.getNumAgents() - 1
            inf = 0
            LA = 0
            for i in legalActions:
                succ = gamestate.generateSuccessor(index, i)
                if index == finished:
                    agent = maximum(succ, depth + 1, 0)
                else:
                    agent = expectimax(succ, depth, index + 1)
                length = len(legalActions)  # edw
                inf = inf + (agent[0] / length)
            return inf, LA

        return maximum(gameState, 0, 0)[1]

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <Shmantikotera ta chapakia dynamhs kai meta ta fantasmatakia kai to faghto>
    """
    "*** YOUR CODE HERE ***"

    pacmanPosition = currentGameState.getPacmanPosition()
    ghostState = currentGameState.getGhostStates()
    capsules = currentGameState.getCapsules()
    food = currentGameState.getFood()

    newfood = food.asList()
    food_dis = []
    for i in newfood:
        food_dis.append(manhattanDistance(pacmanPosition, i))   # pairnw apostash apo faghto
    if newfood:
        min_f = min(food_dis)  # pairnw to mikrotero
    else:
        min_f = 0

    ghost_dis = []
    for i in ghostState:
        ghost_dis.append(manhattanDistance(pacmanPosition, i.getPosition()))    # pairnw apostash apo fantasmataki
    min_ghost = min(ghost_dis)

    if min_ghost == 0:
        min_g = 0
    else:
        min_g = 1.0 / min_ghost     # pairnw to mikrotero

    if len(capsules) == 0:  # arithmos apo chapia
        caps = 0
    else:
        caps = 1.0 / len(capsules)

    first_score = 15 * scoreEvaluationFunction(currentGameState)    # pairnw to score
    new_score = 10 * min_f + min_g * 10 + 20 * caps     # shmantikothta
    final_score = first_score - new_score

    return final_score


# Abbreviation
better = betterEvaluationFunction
