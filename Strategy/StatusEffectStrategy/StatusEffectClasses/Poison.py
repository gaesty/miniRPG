from Strategy.StatusEffectStrategy.StatusEffectStrategy import StatusEffectStrategy


class Poison(StatusEffectStrategy):
    """Concrete status effect strategy that deals damage over time to the target."""

    def __init__(self, target, damage=5, duration=3):
        self.target = target
        self.damage = damage
        self.duration = duration
        self.active = True

    def attack(self):
        """Deal poison damage to the target."""
        self.target["pv"] -= self.damage
        if self.target["pv"] < 0:
            self.target["pv"] = 0
        print(
            f"  [Poison] {self.target['name']} takes {self.damage} poison damage! (PV: {self.target['pv']})"
        )

    def delay(self):
        """Decrement the remaining duration. Deactivates when duration reaches 0."""
        self.duration -= 1
        if self.duration <= 0:
            self.active = False
            print(f"  [Poison] The poison on {self.target['name']} has worn off.")

    def addStatusEffect(self):
        """Apply one tick of poison: deal damage then reduce remaining duration."""
        if not self.active:
            return
        print(
            f"  [Poison] {self.target['name']} is poisoned! ({self.duration} turn(s) remaining)"
        )
        self.attack()
        self.delay()
