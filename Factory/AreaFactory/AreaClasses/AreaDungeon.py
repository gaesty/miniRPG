class AreaDungeon:
    def createArea(self, name):
        return {
            "name": name,
            "area_type": name,
            "evenment_type": ["fight", "chest", "quest"],
            "area_safe": False,
            "enemy_type": ["CorruptedChampion", "DungeonKeeper"],
            "rooms": 2,
            "key": True,
        }