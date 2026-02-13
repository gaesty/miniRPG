from Strategy.StatusEffectStrategy.StatusEffectStrategy import StatusEffectStrategy


class StatusEffectContext:
    def __init__(self):
        self._strategy = None

    def set_status_effect_context(self, battle_strategy):
        if not isinstance(battle_strategy, StatusEffectStrategy):
            raise TypeError(
                "battle_strategy must be an instance of StatusEffectStrategy"
            )
        self._strategy = battle_strategy
        print(f"Status effect set to: {self._strategy.__class__.__name__}")

    def make_status_effect(self):
        if self._strategy is None:
            return "No status effect set."
        return self._strategy.addStatusEffect()
