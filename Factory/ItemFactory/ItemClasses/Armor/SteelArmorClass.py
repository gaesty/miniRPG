from ArmorBase import ArmorBase


class SteelArmorClass(ArmorBase):
    """Armure en acier - haute protection, pas de bonus d'intelligence."""

    def get_data(self) -> dict:
        return {
            "name": "Steel Armor",
            "protection": 20,
            "intelligence": 0,
        }
