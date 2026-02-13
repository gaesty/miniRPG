from .AreaBase import AreaBase


class AreaVillage(AreaBase):
    """Zone village - zone sûre avec quêtes et marchands."""

    def get_data(self) -> dict:
        return {
            "name": "village",
            "area_type": "village",
            "event_type": ["quest", "seller"],
            "area_safe": True,
            "enemy_type": None,
            "rooms": None,
            "key": False,
        }
