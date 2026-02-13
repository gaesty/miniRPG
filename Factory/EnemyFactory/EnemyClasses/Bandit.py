class Bandit:
    def createEnemy(self, name):
        return {
            "name": name,
            "type": "standard",
            "description" : "Standard enemy with possible item theft",
            "pv" : 100,
            "standard_attack" : "Knife",
            "offensive_stat" : 5,
            "defensive_stat" : 3,
            "special_skill": "Object theft"
        }