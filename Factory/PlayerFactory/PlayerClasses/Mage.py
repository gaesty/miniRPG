class Mage:
    def createNewPlayer(self, name):
        return {
            "name": name,
            "description" : "Specialization: Offensive and Control Magic",
            "pv" : 300,
            "standard_attack" : "Spell",
            "offensive_stat_1" : 25,
            "offensive_stat_2" : 30,
            "defensive_stat_1" : 50,
            "special_skill_1" : "Fireball",
            "special_skill_2" : "Arcane shield"
        }