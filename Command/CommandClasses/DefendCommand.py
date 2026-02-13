from ..Command import Command


class DefendCommand(Command):
    """Commande pour se défendre et réduire les dégâts du prochain tour."""

    def __init__(self, defender):
        self.defender = defender
        self.defense_boost = 15
        self.applied = False

    def execute(self):
        """Augmente temporairement la défense."""
        if not self.applied:
            for stat in ["defensive_stat", "defensive_stat_1"]:
                if stat in self.defender:
                    self.defender[stat] += self.defense_boost
            self.applied = True
            print(f"{self.defender['name']} takes a defensive stance! (+{self.defense_boost} defense)")
        return True

    def undo(self):
        """Retire le bonus de défense."""
        if self.applied:
            for stat in ["defensive_stat", "defensive_stat_1"]:
                if stat in self.defender:
                    self.defender[stat] -= self.defense_boost
            self.applied = False
            print(f"{self.defender['name']} drops defensive stance")

    def get_description(self):
        """Retourne une description de l'action."""
        return f"{self.defender['name']} defends"
