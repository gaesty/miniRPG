from abc import ABC, abstractmethod


class EnemyBase(ABC):
    """Classe abstraite représentant un ennemi du jeu."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données de l'ennemi sous forme de dictionnaire."""
        pass
