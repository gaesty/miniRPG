from .PlayerBase import PlayerBase


class Thief(PlayerBase):
    """Classe représentant le voleur."""

    def get_data(self) -> dict:
        return {
            "name": "Thief",
            "description": "Specialty: speed",
            "pv": 300,
            "standard_attack": "Knife",
            "strength": 15,
            "intelligence": 25,
            "defense": 50,
            "offensive_stat": 15,
            "defensive_stat": 50,
            "special_skill_1": "Sneak Attack",
            "special_skill_2": "Perfect Dodge",
        }
