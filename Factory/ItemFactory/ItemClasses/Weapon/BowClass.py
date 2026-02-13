from WeaponBase import WeaponBase


class BowClass(WeaponBase):
    """Arme à distance avec bonus d'intelligence."""

    def get_data(self) -> dict:
        return {
            "name": "Bow",
            "damage": 10,
            "intelligence": 20,
        }
