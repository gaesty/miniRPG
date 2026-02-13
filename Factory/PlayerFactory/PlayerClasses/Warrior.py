from .PlayerBase import PlayerBase


class Warrior(PlayerBase):
    """Classe représentant un guerrier."""

    def get_data(self) -> dict:
        return {
            "name": "Warrior",
            "description": "Specialty: Close combat and resistance",
            "pv": 300,
            "standard_attack": "Punch",
            "strength": 40,
            "intelligence": 20,
            "defense": 50,
            "special_skill_1": "Powerful blow",
            "special_skill_2": "Heroic charge",
        }
