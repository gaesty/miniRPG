from ..CombatDecorator import CombatDecorator


class RegenerationDecorator(CombatDecorator):
    """Décorator qui régénère des PV sur la durée."""

    def __init__(self, combatant, heal_per_turn=10, duration=3):
        super().__init__(combatant)
        self.heal_per_turn = heal_per_turn
        self.duration = duration
        self.turns_remaining = duration

    def apply_effect(self):
        """Applique la régénération."""
        if self.turns_remaining > 0:
            self._combatant["pv"] += self.heal_per_turn
            self.turns_remaining -= 1
            print(f"{self._combatant['name']} regenerates {self.heal_per_turn} HP! ({self.turns_remaining} turns remaining)")
            return True
        return False

    def remove_effect(self):
        """Retire l'effet de régénération."""
        self.turns_remaining = 0
        print(f"{self._combatant['name']}'s regeneration ends.")

    def is_active(self):
        """Vérifie si l'effet est toujours actif."""
        return self.turns_remaining > 0
