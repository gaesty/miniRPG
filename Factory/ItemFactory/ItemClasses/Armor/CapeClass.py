from ArmorBase import ArmorBase


class CapeClass(ArmorBase):
    """Armure légère offrant un bonus en intelligence."""

    def get_data(self) -> dict:
        return {
            "name": "Cape",
            "protection": 5,
            "intelligence": 10,
        }
