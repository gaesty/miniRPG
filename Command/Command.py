class Command:
    """Interface de base pour toutes les commandes de combat."""

    def execute(self):
        """Exécute la commande."""
        pass

    def undo(self):
        """Annule la commande."""
        pass

    def get_description(self):
        """Retourne une description de la commande."""
        pass
