from ..CombatDecorator import CombatDecorator


class StrengthBoostDecorator(CombatDecorator):
    """Décorator qui augmente la force d'attaque."""

    def __init__(self, combatant, boost_amount=10):
        super().__init__(combatant)
        self.boost_amount = boost_amount
        self.applied = False

    def apply_effect(self):
        """Augmente les stats offensives."""
        if not self.applied:
            for stat in ["offensive_stat", "offensive_stat_1", "offensive_stat_2", "offensive_stat_3"]:
                if stat in self._combatant:
                    self._combatant[stat] += self.boost_amount
            self.applied = True
            print(f"{self._combatant['name']} gains +{self.boost_amount} attack power!")

    def remove_effect(self):
        """Retire le boost de force."""
        if self.applied:
            for stat in ["offensive_stat", "offensive_stat_1", "offensive_stat_2", "offensive_stat_3"]:
                if stat in self._combatant:
                    self._combatant[stat] -= self.boost_amount
            self.applied = False
            print(f"{self._combatant['name']} loses the strength boost.")
