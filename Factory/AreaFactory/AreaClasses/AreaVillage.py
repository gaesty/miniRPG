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