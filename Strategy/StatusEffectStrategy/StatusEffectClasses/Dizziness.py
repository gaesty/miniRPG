from ..StatusEffectStrategy import StatusEffectStrategy


class Dizziness(StatusEffectStrategy):
    """Concrete status effect strategy that causes the target to skip their turn."""

    def __init__(self, target, duration=2):
        self.target = target
        self.duration = duration
        self.active = True

    def passTurn(self):
        """Force the target to skip their turn."""
        print(f"{self.target['name']} is dizzy and skips their turn!")

    def delay(self):
        """Decrement the remaining duration. Deactivates the effect when expired."""
        self.duration -= 1
        if self.duration <= 0:
            self.active = False
            print(f"Dizziness on {self.target['name']} has worn off.")

    def addStatusEffect(self):
        """Apply the dizziness effect for this turn: skip turn then tick duration."""
        if not self.active:
            return
        self.passTurn()
        self.delay()
