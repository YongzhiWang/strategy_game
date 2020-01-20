import json
import sys
import coredata
import random
import coredata

def computeBasePowerAttack(playerA, playerB):

    return 100

def computePowerAttack(playerA, playerB, targetRatio):
    if isinstance(playerA, coredata.MajorInfo) and isinstance(playerB, coredata.MajorInfo) :
        baseNumber = computeBasePowerAttack(playerA, playerB)
        actualRatio = targetRatio + playerA.attackIncrementPortion - playerB.defenseIncrementPortion

        if random.randint(0, 100) < playerA.attackDoubleProb:
            actualRatio = actualRatio * (100 + playerA.attackDoubleIncrementPortion) / 100

        return baseNumber * actualRatio / 100

    return 1


def computeBaseIQAttack(playerA, playerB):

    return 100

def computeIQAttack(playerA, playerB, targetRatio):
    if isinstance(playerA, coredata.MajorInfo) and isinstance(playerB, coredata.MajorInfo) :
        baseNumber = computeBasePowerAttack(playerA, playerB)
        actualRatio = targetRatio + playerA.attackIncrementPortion - playerB.defenseIncrementPortion

        if random.randint(0, 100) < playerA.attackDoubleProb:
            actualRatio = actualRatio * (100 + playerA.attackDoubleIncrementPortion) / 100

        return baseNumber * actualRatio / 100

    return 1


def computeBaseIQAttack(playerA, playerB):

    return 100

