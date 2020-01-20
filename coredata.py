import json
import sys


class AddtiveStatus:
    def __init__(self, startRound, EndRound, count, name, statusData):
        self.startRound = startRound
        self.EndRound = EndRound
        self.count = count
        self.name = name
        self.statusData = statusData

class NonAdditiveStatus:
    def __init__(self, startRound, EndRound, count, name, statusData):
        self.startRound = startRound
        self.EndRound = EndRound
        self.count = count
        self.name = name
        self.statusData = statusData

class MajorInfo:

    def __init__(self, soldierNum, hurtsoldierNum, attack, IQ, defense, speed, fitProb,
                 attackDoubleProb, attackDoubleIncrementPortion,
                 IQDoubleProb, IQDoubleIncrementPortion,
                 NoHurtProb,
                 attackGainProb, IQGainProb,
                 attackPowerIncrementPortion, defensePowerIncrementPortion,
                 attackIQIncrementPortion, defenseIQIncrementPortion,
                 canRecover,
                 canAttack,
                 isXuRuo,
                 isMad,
                 attackNumber,
                 canTriggerActiveAlgo,
                 preGlobalRoundStatusList,
                 preSelfRoundStatusList,
                 zhihuiRoundStatusList,
                 preSelfActiveRoundStatusList,
                 postSelfActiveRoundStatusList,
                 preAttackRoundStatusList,
                 postAttackRoundStatusList,
                 preBeAttackedRoundStatusList,
                 postBeAttackedRoundStatusList,
                 addtiveStatusList,
                 NonAdditiveStatus,
                 priorityStatusList):
        self.soldierNum = soldierNum
        self.hurtsoldierNum = hurtsoldierNum
        self.attack = attack;
        self.IQ = IQ;
        self.defense = defense;
        self.speed = speed;
        self.fitProb = fitProb;  # Shi Ying
        self.attackDoubleProb = attackDoubleProb; # Hui Xin
        self.attackDoubleIncrementPortion = attackDoubleIncrementPortion; # Hui Xin Shang Hai
        self.IQDoubleProb = IQDoubleProb;  # Qi Mou
        self.NoHurtProb = NoHurtProb;  # Gui Bi
        self.attackGainProb = attackGainProb;  # Dao Ge
        self.IQGainProb = IQGainProb;  # Gong Xin
        self.attackIncrementPortion = attackIncrementPortion; # Gong ji Zeng Qiang
        self.defenseIncrementPortion = defenseIncrementPortion; # Fang Shou Zeng Qiang
        self.addtiveStatusList = addtiveStatusList # Ge Ren Zhuang Tai
        self.NonAdditiveStatus = NonAdditiveStatus # Bu Ke Die Jia Zhuang Tai
        self.priorityStatusList = priorityStatusList # status to update before each round
        self.canAttack = canAttack # status to update before each round
        self.canRecover = canRecover
        self.canTriggerActiveAlgo = canTriggerActiveAlgo # status to update before each round
        self.preGlobalRoundStatusList = preGlobalRoundStatusList # status to update before each round
        self.preSelfActiveRoundStatusList = preSelfActiveRoundStatusList # status to update before each round
        self.postSelfActiveRoundStatusList = postSelfActiveRoundStatusList # status to update before each round
        self.preAttackRoundStatusList = preAttackRoundStatusList # status to update before each round
        self.postAttackRoundStatusList = postAttackRoundStatusList # status to update before each round
        self.preBeAttackedRoundStatusList = preBeAttackedRoundStatusList # status to update before each round
        self.postBeAttackedRoundStatusList = postBeAttackedRoundStatusList # status to update before each round
