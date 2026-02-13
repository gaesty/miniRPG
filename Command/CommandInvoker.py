class CommandInvoker:
    """Invocateur qui gère l'exécution et l'historique des commandes."""

    def __init__(self):
        self.history = []
        self.current_index = -1

    def execute_command(self, command):
        """Exécute une commande et l'ajoute à l'historique."""
        result = command.execute()
        
        # Supprimer les commandes après l'index actuel si on en exécute une nouvelle
        self.history = self.history[:self.current_index + 1]
        
        self.history.append(command)
        self.current_index += 1
        
        return result

    def undo_last(self):
        """Annule la dernière commande exécutée."""
        if self.current_index >= 0:
            command = self.history[self.current_index]
            command.undo()
            self.current_index -= 1
            print(f"Undid: {command.get_description()}")
            return True
        else:
            print("No command to undo")
            return False

    def redo_last(self):
        """Refait la dernière commande annulée."""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            command = self.history[self.current_index]
            command.execute()
            print(f"Redid: {command.get_description()}")
            return True
        else:
            print("No command to redo")
            return False

    def get_history(self):
        """Retourne l'historique des commandes."""
        return [cmd.get_description() for cmd in self.history]

    def clear_history(self):
        """Efface l'historique des commandes."""
        self.history = []
        self.current_index = -1
