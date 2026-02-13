from .EnemyBase import EnemyBase


class Skeleton(EnemyBase):
    """Ennemi standard résistant aux dégâts physiques."""

    def get_data(self) -> dict:
        return {
            "name": "Skeleton",
            "type": "standard",
            "description": "Standard enemy resistant to physical damage",
            "pv": 125,
            "standard_attack": "Slap",
            "offensive_stat": 1,
            "defensive_stat": 10,
            "special_skill": "Blocking",
        }
