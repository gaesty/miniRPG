from .WeaponBase import WeaponBase


class WoodenSwordClass(WeaponBase):
    """Épée en bois - arme de départ basique."""

    def get_data(self) -> dict:
        return {
            "name": "Wooden Sword",
            "damage": 5,
            "intelligence": 0,
        }
