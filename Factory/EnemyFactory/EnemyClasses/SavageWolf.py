from .EnemyBase import EnemyBase


class SavageWolf(EnemyBase):
    """Loup sauvage - ennemi standard rapide avec attaques multiples."""

    def get_data(self) -> dict:
        return {
            "name": "Savage Wolf",
            "type": "standard",
            "description": "Standard enemy, fast with multiple attacks",
            "pv": 75,
            "standard_attack": "Bite",
            "offensive_stat": 5,
            "defensive_stat": 0,
            "special_skill": "Multiple bite",
        }
