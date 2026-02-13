from ConsumableBase import ConsumableBase


class HealthPotion(ConsumableBase):
    """Potion de soin restaurant des points de vie."""

    def get_data(self) -> dict:
        return {
            "name": "Health Potion",
            "pv_restore": 30,
            "damage": None,
            "status": None,
        }
