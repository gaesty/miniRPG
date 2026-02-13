class Skeleton:
    def createEnemy(self, name):
        return {
            "name": name,
            "type": "standard",
            "description" : "Standard enemy resistant to physical damage",
            "pv" : 125,
            "standard_attack" : "Slap",
            "offensive_stat" : 1,
            "defensive_stat" : 10,
            "special_skill": "Blocking" 
        }