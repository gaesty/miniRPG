from EnemyClasses.EnemyBase import EnemyBase


class DungeonKeeper(EnemyBase):
    """Gardien du donjon, boss puissant protégeant les profondeurs."""

    def get_data(self) -> dict:
        return {
            "name": "Dungeon Keeper",
            "type": "boss",
            "description": "Powerful guardian of the dungeon",
            "pv": 500,
            "standard_attack": "Crushing Blow",
            "offensive_stat": 50,
            "defensive_stat": 45,
            "special_skill": "Earthquake",
        }
