class AreaIterator:
    """Iterator de base pour parcourir les zones du jeu."""

    def __init__(self, areas):
        self._areas = areas
        self._index = 0

    def __iter__(self):
        """Retourne l'itérateur lui-même."""
        return self

    def __next__(self):
        """Retourne la prochaine zone."""
        if self._index < len(self._areas):
            area = self._areas[self._index]
            self._index += 1
            return area
        raise StopIteration

    def has_next(self):
        """Vérifie s'il reste des zones à parcourir."""
        return self._index < len(self._areas)

    def current(self):
        """Retourne la zone actuelle sans avancer."""
        if 0 < self._index <= len(self._areas):
            return self._areas[self._index - 1]
        return None

    def reset(self):
        """Réinitialise l'itérateur au début."""
        self._index = 0

    def get_position(self):
        """Retourne la position actuelle dans l'itération."""
        return self._index
