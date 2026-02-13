from PlayerClasses.Mage import Mage
from PlayerClasses.Thief import Thief
from PlayerClasses.Warrior import Warrior


class PlayerFactory:
    """Factory pour créer des personnages joueurs."""

    _player_map = {
        "warrior": Warrior,
        "mage": Mage,
        "thief": Thief,
    }

    def create_player(self, name: str) -> dict:
        """Crée et retourne les données d'un personnage joueur."""
        player_class = self._player_map.get(name)
        if player_class is None:
            raise ValueError(
                f"Classe de personnage inconnue : '{name}'. "
                f"Disponibles : {list(self._player_map.keys())}"
            )
        return player_class().get_data()
