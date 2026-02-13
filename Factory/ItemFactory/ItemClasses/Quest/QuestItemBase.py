from abc import ABC, abstractmethod


class QuestItemBase(ABC):
    """Classe abstraite représentant un objet de quête."""

    @abstractmethod
    def get_data(self) -> dict:
        """Retourne les données de l'objet de quête sous forme de dictionnaire."""
        pass
