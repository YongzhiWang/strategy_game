import json
import sys



class SoldierInfo:

    def __init__(self, attack, IQ, defense, speed, fitProb, attackDoubleProb, IQDoubleProb, NoHurtProb, attackGainProb, IQGainProb):
        self.attack = attack;
        self.IQ = IQ;
        self.defense = defense;
        self.speed = speed;
        self.fitProb = fitProb;  # Shi Ying
        self.attackDoubleProb = attackDoubleProb; # Hui Xin
        self.IQDoubleProb = IQDoubleProb;  # Qi Mou
        self.NoHurtProb = NoHurtProb;  # Gui Bi
        self.attackGainProb = attackGainProb;  # Dao Ge
        self.IQGainProb = IQGainProb;  # Gong Xin
