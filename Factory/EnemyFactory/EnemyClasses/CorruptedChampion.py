from EnemyClasses.EnemyBase import EnemyBase


class CorruptedChampion(EnemyBase):
    def get_data(self) -> dict:
        return {
            "name": "Corrupted Champion",
            "type": "boss",
            "description": "Final boss with 2 distinct combat phases",
            "pv": 500,
            "standard_attack": "Dark Slash",
            "offensive_stat": 25,
            "defensive_stat": 15,
            "special_skill": "Phase Shift",
        }
