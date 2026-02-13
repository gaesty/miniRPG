from abc import ABC, abstractmethod


class ArmorBase(ABC):
    """Classe abstraite représentant une armure."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données de l'armure sous forme de dictionnaire."""
        pass
