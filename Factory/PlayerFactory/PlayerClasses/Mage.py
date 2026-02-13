from .PlayerBase import PlayerBase


class Mage(PlayerBase):
    """Classe représentant un personnage Mage."""

    def get_data(self) -> dict:
        return {
            "name": "Mage",
            "description": "Specialization: Offensive and Control Magic",
            "pv": 300,
            "standard_attack": "Spell",
            "strength": 25,
            "intelligence": 30,
            "defense": 50,
            "offensive_stat": 25,
            "defensive_stat": 50,
            "special_skill_1": "Fireball",
            "special_skill_2": "Arcane shield",
        }
