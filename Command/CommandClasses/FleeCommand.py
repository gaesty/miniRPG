from ..Command import Command


class FleeCommand(Command):
    """Commande pour tenter de fuir le combat."""

    def __init__(self, player):
        self.player = player
        self.success = False

    def execute(self):
        """Tente de fuir le combat (50% de chance)."""
        import random
        self.success = random.random() > 0.5
        
        if self.success:
            print(f"{self.player['name']} successfully fled from battle!")
        else:
            print(f"{self.player['name']} failed to flee!")
        
        return self.success

    def undo(self):
        """On ne peut pas annuler une fuite."""
        print("Cannot undo flee attempt")

    def get_description(self):
        """Retourne une description de l'action."""
        return f"{self.player['name']} attempts to flee"
