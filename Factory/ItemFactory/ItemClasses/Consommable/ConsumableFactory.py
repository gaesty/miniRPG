from .AntidoteClass import AntidoteClass
from .BombClass import BombClass
from .HealtPotionClass import HealthPotion


class ConsumableFactory:
    """Factory pour créer des consommables."""

    _consumable_map = {
        "health potion": HealthPotion,
        "antidote": AntidoteClass,
        "bomb": BombClass,
    }

    def create_consumable(self, name: str) -> dict:
        """Crée et retourne les données d'un consommable."""
        consumable_class = self._consumable_map.get(name)
        if consumable_class is None:
            raise ValueError(
                f"Consommable inconnu : '{name}'. "
                f"Disponibles : {list(self._consumable_map.keys())}"
            )
        return consumable_class().get_data()
