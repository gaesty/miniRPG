from abc import ABC, abstractmethod


class StatusEffectStrategy(ABC):
    """Interface abstraite pour les effets de statut (Strategy Pattern).

    Chaque effet concret (Poison, Shield, Dizziness, etc.) doit
    hériter de cette classe et implémenter la méthode addStatusEffect().
    """

    @abstractmethod
    def addStatusEffect(self):
        """Applique l'effet de statut sur la cible.

        Cette méthode est appelée à chaque tour par le StatusEffectContext
        pour déclencher la logique propre à l'effet (dégâts, défense, skip, etc.).
        """
        pass

    @abstractmethod
    def delay(self):
        """Gère la durée restante de l'effet.

        Décrémente le compteur de durée et retourne True si l'effet
        est encore actif, False s'il a expiré.

        Returns:
            bool: True si l'effet est encore actif, False sinon.
        """
        pass

    def is_expired(self):
        """Vérifie si l'effet a expiré.

        Returns:
            bool: True si l'effet a expiré, False sinon.
        """
        return self.duration <= 0

    def __str__(self):
        return f"{self.__class__.__name__} (durée restante: {self.duration})"
