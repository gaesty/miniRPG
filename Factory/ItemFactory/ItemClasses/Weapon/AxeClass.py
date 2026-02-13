from ItemClasses.Weapon.WeaponBase import WeaponBase


class AxeClass(WeaponBase):
    """Classe représentant une hache."""

    def get_data(self) -> dict:
        return {
            "name": "Axe",
            "damage": 20,
            "intelligence": 5,
        }
