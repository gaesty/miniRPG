from .AreaClasses.AreaDungeon import AreaDungeon
from .AreaClasses.AreaForest import AreaForest
from .AreaClasses.AreaVillage import AreaVillage


class AreaFactory:
    """Factory pour créer des zones de jeu."""

    _area_map = {
        "forest": AreaForest,
        "village": AreaVillage,
        "dungeon": AreaDungeon,
    }

    def create_area(self, name: str) -> dict:
        """Crée et retourne les données d'une zone."""
        area_class = self._area_map.get(name)
        if area_class is None:
            raise ValueError(
                f"Zone inconnue : '{name}'. Disponibles : {list(self._area_map.keys())}"
            )
        return area_class().get_data()
