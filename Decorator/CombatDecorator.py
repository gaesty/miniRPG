class CombatDecorator:
    """Decorator de base pour ajouter des effets aux combattants."""

    def __init__(self, combatant):
        self._combatant = combatant

    def get_stat(self, stat_name):
        """Retourne une statistique du combattant."""
        return self._combatant.get(stat_name, 0)

    def apply_effect(self):
        """Applique l'effet du decorator."""
        pass

    def remove_effect(self):
        """Retire l'effet du decorator."""
        pass

    def get_combatant(self):
        """Retourne le combattant décoré."""
        return self._combatant
