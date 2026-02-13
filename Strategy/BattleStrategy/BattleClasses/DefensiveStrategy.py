from ..BattleStrategy import BattleStrategy


class DefensiveStrategy(BattleStrategy):
    def execute_attack(self, attacker, defender):
        damage = (
            attacker.get("offensive_stat_1", attacker.get("offensive_stat", 0)) // 2
        )
        defense = defender.get("defensive_stat_1", defender.get("defensive_stat", 0))
        final_damage = max(damage - defense, 1)
        defender["pv"] -= final_damage
        attacker["defensive_stat_1"] = (
            attacker.get("defensive_stat_1", attacker.get("defensive_stat", 0)) + 5
        )
        print(f"{attacker['name']} uses defensive strategy!")
        print(
            f"{attacker['name']} attacks carefully for {final_damage} damage and increases defense!"
        )
        return final_damage

    def get_strategy_name(self):
        return "Defensive"
