from BattleStrategy.BattleStrategy import BattleStrategy

class SpecialSkillStrategy(BattleStrategy):
    def execute_attack(self, attacker, defender):
        special_skill = attacker.get("special_skill_1", attacker.get("special_skill", "Special Attack"))
        damage = attacker.get("offensive_stat_3", attacker.get("offensive_stat_2", attacker.get("offensive_stat", 0))) + 10
        defense = defender.get("defensive_stat_1", defender.get("defensive_stat", 0))
        final_damage = max(damage - defense, 0)
        defender["pv"] -= final_damage
        print(f"{attacker['name']} uses special skill: {special_skill}!")
        print(f"{attacker['name']} deals {final_damage} damage to {defender['name']}!")
        return final_damage
    
    def get_strategy_name(self):
        return "Special Skill"
