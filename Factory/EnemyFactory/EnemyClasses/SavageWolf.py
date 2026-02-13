class SavageWolf:
    def createEnemy(self, name):
        return {
            "name": name,
            "type": "standard",
            "description" : "Standard enemy, fast with multiple attacks",
            "pv" : 75,
            "standard_attack" : "Bite",
            "offensive_stat" : 5,
            "defensive_stat" : 0,
            "special_skill": "Multiple bite"
        }
