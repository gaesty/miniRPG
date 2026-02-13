class DungeonKeeper:
    def createEnemy(self, name):
        return {
            "name": name,
            "type": "boss",
            "description" : "Standard enemy, fast with multiple attacks",
            "pv" : 500,
            "standard_attack" : "attack",
            "offensive_stat" : 50,
            "defensive_stat" : 45,
            "special_skill": "special_attack"
        }
