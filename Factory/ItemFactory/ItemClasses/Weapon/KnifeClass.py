from .WeaponBase import WeaponBase


class KnifeClass(WeaponBase):
    """Couteau - arme légère et rapide."""

    def get_data(self) -> dict:
        return {
            "name": "Knife",
            "damage": 10,
            "intelligence": 3,
        }
