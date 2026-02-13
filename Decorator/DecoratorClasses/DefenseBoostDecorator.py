from ..CombatDecorator import CombatDecorator


class DefenseBoostDecorator(CombatDecorator):
    """Décorator qui augmente la défense."""

    def __init__(self, combatant, boost_amount=10):
        super().__init__(combatant)
        self.boost_amount = boost_amount
        self.applied = False

    def apply_effect(self):
        """Augmente les stats défensives."""
        if not self.applied:
            for stat in ["defensive_stat", "defensive_stat_1"]:
                if stat in self._combatant:
                    self._combatant[stat] += self.boost_amount
            self.applied = True
            print(f"{self._combatant['name']} gains +{self.boost_amount} defense!")

    def remove_effect(self):
        """Retire le boost de défense."""
        if self.applied:
            for stat in ["defensive_stat", "defensive_stat_1"]:
                if stat in self._combatant:
                    self._combatant[stat] -= self.boost_amount
            self.applied = False
            print(f"{self._combatant['name']} loses the defense boost.")
