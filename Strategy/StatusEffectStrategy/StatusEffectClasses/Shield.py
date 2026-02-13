from Strategy.StatusEffectStrategy.StatusEffectStrategy import StatusEffectStrategy


class Shield(StatusEffectStrategy):
    """Concrete status effect strategy that temporarily boosts the target's defense."""

    def __init__(self, target, defense_boost=5, duration=3):
        self.target = target
        self.defense_boost = defense_boost
        self.duration = duration
        self.applied = False

    def defense(self):
        """Apply the defense boost to the target."""
        if not self.applied:
            defense_key = (
                "defensive_stat_1"
                if "defensive_stat_1" in self.target
                else "defensive_stat"
            )
            self.target[defense_key] = (
                self.target.get(defense_key, 0) + self.defense_boost
            )
            self.applied = True
            print(
                f"{self.target['name']} gains a shield! Defense boosted by {self.defense_boost}."
            )
        else:
            print(
                f"{self.target['name']}'s shield holds strong. ({self.duration} turn(s) remaining)"
            )

    def delay(self):
        """Decrement the shield duration and remove the boost when expired."""
        self.duration -= 1
        if self.duration <= 0:
            defense_key = (
                "defensive_stat_1"
                if "defensive_stat_1" in self.target
                else "defensive_stat"
            )
            self.target[defense_key] = (
                self.target.get(defense_key, 0) - self.defense_boost
            )
            self.applied = False
            print(
                f"{self.target['name']}'s shield has faded. Defense returned to normal."
            )
            return False
        return True

    def addStatusEffect(self):
        """Apply the shield effect for this turn."""
        self.defense()
        still_active = self.delay()
        return still_active
