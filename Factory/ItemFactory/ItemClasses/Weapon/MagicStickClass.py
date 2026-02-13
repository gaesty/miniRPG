from ItemClasses.Weapon.WeaponBase import WeaponBase


class MagicStickClass(WeaponBase):
    """Bâton magique - arme à forte intelligence."""

    def get_data(self) -> dict:
        return {
            "name": "Magic Stick",
            "damage": 15,
            "intelligence": 20,
        }
