from .QuestItemBase import QuestItemBase


class KeyClass(QuestItemBase):
    """Clé permettant d'accéder à la salle du boss."""

    def get_data(self) -> dict:
        return {
            "name": "Key",
            "description": "La clé pour la salle du boss au fond du donjon",
        }
