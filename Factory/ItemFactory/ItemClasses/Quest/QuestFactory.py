from KeyClass import KeyClass


class QuestFactory:
    """Factory pour créer des objets de quête."""

    _quest_item_map = {
        "key": KeyClass,
    }

    def create_quest_item(self, name: str) -> dict:
        """Crée et retourne les données d'un objet de quête."""
        quest_class = self._quest_item_map.get(name)
        if quest_class is None:
            raise ValueError(
                f"Objet de quête inconnu : '{name}'. "
                f"Disponibles : {list(self._quest_item_map.keys())}"
            )
        return quest_class().get_data()
