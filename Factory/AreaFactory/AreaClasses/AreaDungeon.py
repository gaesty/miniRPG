from AreaClasses.AreaBase import AreaBase


class AreaDungeon(AreaBase):
    """Zone de type donjon avec des combats et un boss."""

    def get_data(self) -> dict:
        return {
            "name": "dungeon",
            "area_type": "dungeon",
            "event_type": ["fight", "chest", "quest"],
            "area_safe": False,
            "enemy_type": ["CorruptedChampion", "DungeonKeeper"],
            "rooms": 2,
            "key": True,
        }
