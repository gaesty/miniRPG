from EnemyClasses import SavageWolf, Bandit, Skeleton, CorruptedChampion, DungeonKeeper

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
