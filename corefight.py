import json
import sys
import coredata

def battle(teamA, teamB):

    allPlayers = teamA + teamB
    for player in allPlayers:
        updateInitialSodierData(player) # Update all user's status, based on fitness, Zhi Hui, Passive Algo

    for player in allPlayers:
        runZhiHuiAlgor(player)

    for player in allPlayers:
        runPassiveAlgor(player)

    for round in range(8):
        for player in allPlayers:
            updateRoundGlobalPriorityStatus(player) # Update player infor per round

        remainingPlayers = allPlayers
        while len(remainingPlayers) > 0:
            nextPlayer = selectNexPlayer(remainingPlayers)
            fightOneRound(nextPlayer)
            remainingPlayers.remove(nextPlayer)

    return;

def updateInitialSodierData(player): #input list of players.
    return

def runZhiHuiAlgor(player): # input: one player, the algo
    return

def runPassiveAlgor(player): # input: one player, the algo
    return

def updateRoundGlobalPriorityStatus(player): # input: one player, the algo
    return


def selectNexPlayer(remainingPlayers, finishedPlayers): #input: list of unplayers.
    return


def updateSodierData(): #input player to target player status...

    return

def fightOneRound(nextPlayer):

    # Get One user status, affect by all the numbers
    #SoldierInfo = SoldierInfo()

    # update the current status first
    # and update its status list
    # while (!preSelfRoundStatusList.isEmpty())
    # update the user status.

    # while (!zhihuiRoundStatusList.isEmpty())
    #     for each algor
    #          check the preparition, if yes, launch and move to the post phase
    #          check the launch prob
    #               if yes, launch and move to the post phase
    #          check the post zhihui status.
    #          run the execution phase. List may contain self or others.
    #               target user selections
    #               check pre attack status on target users
    #               check the post attack status on target users.
    #

    # while (!preSelfActiveRoundStatusList.isEmpty())
    # {
    #     check algor enable status.
    #     for each algor
    #          check the preparition, if yes, launch and move to the post phase
    #          check the launch prob
    #               if yes, launch and move to the post phase
    #          check the post active status.
    #          run the execution phase. List may contain self or others.
    #               target user selections
    #               check pre attack status on target users
    #               check the post attack status on target users.
    # }
    #

    # is able to attack
    # while (!prePreAttackRoundStatusList.isEmpty())
    # {
    #     execute all preAttackStatusList and update the status
    #     decide attack count.
    #     for each attach number
    #           target user selections
    #           check pre attack status on target users
    #           check the post attack status on target users.
    #
    # }
    #

    return

def runActiveAlgo(): # input: one player, the algo

    # Get One user status
    #SoldierInfo = SoldierInfo()

    # update the current status first

    # check active enablement status

    # check the prob

    # run the post-active hook?

    # enter the preparation phase?

    # run the actual algo.

    return;

def runSelfPassiveAlgo(): # input: one player, the algo

    return


def runOthersPassiveAlgo(): # input: one player, the algo

    return