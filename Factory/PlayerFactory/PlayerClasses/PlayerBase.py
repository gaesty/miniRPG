from abc import ABC, abstractmethod


class PlayerBase(ABC):
    """Classe abstraite représentant un personnage joueur."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données du personnage sous forme de dictionnaire."""
        pass
