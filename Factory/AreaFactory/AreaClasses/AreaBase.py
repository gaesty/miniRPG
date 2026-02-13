from abc import ABC, abstractmethod


class AreaBase(ABC):
    """Classe abstraite représentant une zone du jeu."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données de la zone sous forme de dictionnaire."""
        pass
