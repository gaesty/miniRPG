from abc import ABC, abstractmethod


class WeaponBase(ABC):
    """Classe abstraite représentant une arme du jeu."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données de l'arme sous forme de dictionnaire."""
        pass
