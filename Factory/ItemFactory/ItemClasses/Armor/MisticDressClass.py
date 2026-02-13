from .ArmorBase import ArmorBase


class MysticDress(ArmorBase):
    """Robe mystique offrant une haute intelligence."""

    def get_data(self) -> dict:
        return {
            "name": "Mystic Dress",
            "protection": 10,
            "intelligence": 20,
        }
