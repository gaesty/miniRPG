from .ArmorBase import ArmorBase


class LeatherArmorClass(ArmorBase):
    """Armure en cuir offrant une protection légère."""

    def get_data(self) -> dict:
        return {
            "name": "Leather Armor",
            "protection": 10,
            "intelligence": 3,
        }
