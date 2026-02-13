from abc import ABC, abstractmethod


class ConsumableBase(ABC):
    """Classe abstraite représentant un consommable."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données du consommable sous forme de dictionnaire."""
        pass
