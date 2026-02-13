from .WeaponBase import WeaponBase


class SteelSwordClass(WeaponBase):
    """Épée en acier - arme équilibrée entre dégâts et intelligence."""

    def get_data(self) -> dict:
        return {
            "name": "Steel Sword",
            "damage": 15,
            "intelligence": 5,
        }
