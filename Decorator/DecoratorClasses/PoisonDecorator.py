from Decorator.CombatDecorator import CombatDecorator


class PoisonDecorator(CombatDecorator):
    """Décorator qui applique un effet de poison (dégâts sur la durée)."""

    def __init__(self, combatant, damage_per_turn=5, duration=3):
        super().__init__(combatant)
        self.damage_per_turn = damage_per_turn
        self.duration = duration
        self.turns_remaining = duration

    def apply_effect(self):
        """Applique les dégâts de poison."""
        if self.turns_remaining > 0:
            self._combatant["pv"] -= self.damage_per_turn
            self.turns_remaining -= 1
            print(f"{self._combatant['name']} takes {self.damage_per_turn} poison damage! ({self.turns_remaining} turns remaining)")
            return True
        return False

    def remove_effect(self):
        """Retire l'effet de poison."""
        self.turns_remaining = 0
        print(f"{self._combatant['name']} is no longer poisoned.")

    def is_active(self):
        """Vérifie si l'effet est toujours actif."""
        return self.turns_remaining > 0
