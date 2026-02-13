from .CapeClass import CapeClass
from .LeatherArmorClass import LeatherArmorClass
from .MisticDressClass import MysticDress
from .SteelArmorClass import SteelArmorClass


class ArmorFactory:
    """Factory pour créer des armures."""

    _armor_map = {
        "cape": CapeClass,
        "leather armor": LeatherArmorClass,
        "mystic dress": MysticDress,
        "steel armor": SteelArmorClass,
    }

    def create_armor(self, name: str) -> dict:
        """Crée et retourne les données d'une armure."""
        armor_class = self._armor_map.get(name)
        if armor_class is None:
            raise ValueError(
                f"Armure inconnue : '{name}'. "
                f"Disponibles : {list(self._armor_map.keys())}"
            )
        return armor_class().get_data()
