from EnemyClasses.Bandit import Bandit
from EnemyClasses.CorruptedChampion import CorruptedChampion
from EnemyClasses.DungeonKeeper import DungeonKeeper
from EnemyClasses.SavageWolf import SavageWolf
from EnemyClasses.Skeleton import Skeleton


class EnemyFactory:
    """Factory pour créer des ennemis."""

    _enemy_map = {
        "savage wolf": SavageWolf,
        "bandit": Bandit,
        "skeleton": Skeleton,
        "corrupted champion": CorruptedChampion,
        "dungeon keeper": DungeonKeeper,
    }

    def create_enemy(self, name: str) -> dict:
        """Crée et retourne les données d'un ennemi."""
        enemy_class = self._enemy_map.get(name)
        if enemy_class is None:
            raise ValueError(
                f"Ennemi inconnu : '{name}'. "
                f"Disponibles : {list(self._enemy_map.keys())}"
            )
        return enemy_class().get_data()
