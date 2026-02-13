class Thief:
    def createNewPlayer(self, name):
        return {
            "name": name,
            "description" : "Specialty: speed",
            "pv" : 300,
            "standard_attack" : "Knife",
            "offensive_stat_1" : 15,
            "offensive_stat_2" : 25,
            "defensive_stat_1" : 50,
            "special_skill_1" : "sneak attack",
            "special_skill_2" : "Perfect dodge"
        }