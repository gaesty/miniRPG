from EnemyClasses.Bandit import Bandit
from EnemyClasses.CorruptedChampion import CorruptedChampion
from EnemyClasses.DungeonKeeper import DungeonKeeper
from EnemyClasses.SavageWolf import SavageWolf
from EnemyClasses.Skeleton import Skeleton


class EnemyFactory:
    def createEnemy(self, name):
        if name == "savage wolf":
            return SavageWolf()
        elif name == "bandit":
            return Bandit()
        elif name == "skeleton":
            return Skeleton()
        elif name == "corrupted champion":
            return CorruptedChampion()
        elif name == "dungeon keeper":
            return DungeonKeeper()
        else:
            pass
