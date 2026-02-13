from ..BattleStrategy import BattleStrategy

class BalancedStrategy(BattleStrategy):
    def execute_attack(self, attacker, defender):
        damage = attacker.get("offensive_stat_1", attacker.get("offensive_stat", 0))
        defense = defender.get("defensive_stat_1", defender.get("defensive_stat", 0))
        final_damage = max(damage - defense, 0)
        defender["pv"] -= final_damage
        print(f"{attacker['name']} uses balanced strategy!")
        print(f"{attacker['name']} attacks {defender['name']} for {final_damage} damage!")
        return final_damage
    
    def get_strategy_name(self):
        return "Balanced"