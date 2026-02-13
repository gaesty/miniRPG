class MenuIterator:
    """Iterator pour parcourir les options d'un menu."""

    def __init__(self, menu_options):
        self._options = menu_options
        self._index = 0

    def __iter__(self):
        """Retourne l'itérateur lui-même."""
        return self

    def __next__(self):
        """Retourne la prochaine option du menu."""
        if self._index < len(self._options):
            option = self._options[self._index]
            self._index += 1
            return option
        raise StopIteration

    def has_next(self):
        """Vérifie s'il reste des options à afficher."""
        return self._index < len(self._options)

    def current(self):
        """Retourne l'option actuelle sans avancer."""
        if 0 < self._index <= len(self._options):
            return self._options[self._index - 1]
        return None

    def reset(self):
        """Réinitialise l'itérateur au début du menu."""
        self._index = 0

    def get_all_options(self):
        """Retourne toutes les options du menu."""
        return self._options

    def select_option(self, index):
        """Sélectionne une option par son index."""
        if 0 <= index < len(self._options):
            return self._options[index]
        return None
