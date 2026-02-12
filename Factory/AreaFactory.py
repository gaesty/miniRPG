class AreaFactory:
    def createArea(self, name):
        if name == "forest":
            return AreaForest()
        elif name == "village":
            return AreaVillage()
        elif name == "dungeon":
            return AreaDungeon()
        else:
            pass


class AreaForest:
    def createArea(self, name):
        return {
            "name": name,
            "area_type": name,
            "evenment_type": ["fight", "chest", "quest"],
            "area_safe": False,
            "enemy_type": ["SavageWolf", "Bandit", "Skeleton"],
            "rooms": None,
            "key": True,
        }


class AreaVillage:
    def createArea(self, name):
        return {
            "name": name,
            "area_type": name,
            "evenment_type": ["quest", "seller"],
            "area_safe": True,
            "enemy_type": None,
            "rooms": None,
            "key": None,
        }


class AreaDungeon:
    def createArea(self, name):
        return {
            "name": name,
            "area_type": name,
            "evenment_type": ["fight", "chest", "quest"],
            "area_safe": False,
            "enemy_type": ["CorruptedChampion", "DunjeonKeeper"],
            "rooms": 2,
            "key": True,
        }
