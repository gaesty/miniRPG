from ..Command import Command


class AttackCommand(Command):
    """Commande pour effectuer une attaque basique."""

    def __init__(self, attacker, defender, strategy):
        self.attacker = attacker
        self.defender = defender
        self.strategy = strategy
        self.damage_dealt = 0
        self.defender_pv_before = 0

    def execute(self):
        """Exécute l'attaque avec la stratégie donnée."""
        self.defender_pv_before = self.defender.get("pv", 0)
        self.damage_dealt = self.strategy.execute_attack(self.attacker, self.defender)
        return self.damage_dealt

    def undo(self):
        """Annule les dégâts de l'attaque."""
        self.defender["pv"] = self.defender_pv_before
        print(f"Attack undone! {self.defender['name']} HP restored to {self.defender_pv_before}")

    def get_description(self):
        """Retourne une description de l'attaque."""
        return f"{self.attacker['name']} attacks {self.defender['name']} with {self.strategy.get_strategy_name()} strategy"
