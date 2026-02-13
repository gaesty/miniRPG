from AreaClasses.AreaBase import AreaBase


class AreaForest(AreaBase):
    """Zone de type forêt avec des combats, coffres et quêtes."""

    def get_data(self) -> dict:
        return {
            "name": "forest",
            "area_type": "forest",
            "event_type": ["fight", "chest", "quest"],
            "area_safe": False,
            "enemy_type": ["SavageWolf", "Bandit", "Skeleton"],
            "rooms": None,
            "key": True,
        }
