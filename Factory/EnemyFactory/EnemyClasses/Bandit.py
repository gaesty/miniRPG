from EnemyClasses.EnemyBase import EnemyBase


class Bandit(EnemyBase):
    """Ennemi standard avec possibilité de vol d'objets."""

    def get_data(self) -> dict:
        return {
            "name": "Bandit",
            "type": "standard",
            "description": "Standard enemy with possible item theft",
            "pv": 100,
            "standard_attack": "Knife",
            "offensive_stat": 5,
            "defensive_stat": 3,
            "special_skill": "Object theft",
        }
