from AxeClass import AxeClass
from BowClass import BowClass
from KnifeClass import KnifeClass
from MagicStickClass import MagicStickClass
from SteelSwordClass import SteelSwordClass
from WeaponBase import WeaponBase
from WoodenSwordClass import WoodenSwordClass


class WeaponFactory:
    """Factory pour créer des armes."""

    _weapon_map = {
        "wooden sword": WoodenSwordClass,
        "steel sword": SteelSwordClass,
        "magic stick": MagicStickClass,
        "knife": KnifeClass,
        "axe": AxeClass,
        "bow": BowClass,
    }

    def create_weapon(self, name: str) -> dict:
        """Crée et retourne les données d'une arme."""
        weapon_class = self._weapon_map.get(name)
        if weapon_class is None:
            raise ValueError(
                f"Arme inconnue : '{name}'. "
                f"Disponibles : {list(self._weapon_map.keys())}"
            )
        return weapon_class().get_data()
