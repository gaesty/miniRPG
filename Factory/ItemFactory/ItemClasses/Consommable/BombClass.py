from ConsumableBase import ConsumableBase


class BombClass(ConsumableBase):
    """Bombe infligeant des dégâts à l'ennemi."""

    def get_data(self) -> dict:
        return {
            "name": "Bomb",
            "pv_restore": None,
            "damage": 30,
            "status": None,
        }
