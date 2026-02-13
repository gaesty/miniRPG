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