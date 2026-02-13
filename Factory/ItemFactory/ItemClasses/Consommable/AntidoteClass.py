from .ConsumableBase import ConsumableBase


class AntidoteClass(ConsumableBase):
    """Antidote permettant de soigner le poison."""

    def get_data(self) -> dict:
        return {
            "name": "Antidote",
            "pv_restore": None,
            "damage": None,
            "status": "cure_poison",
        }
