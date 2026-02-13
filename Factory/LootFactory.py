import random


class LootFactory:
    """Factory pour générer du loot aléatoire selon le type de zone."""

    _loot_table = {
        "forest": {
            "weapons": ["Wooden Sword", "Knife", "Bow"],
            "armors": ["Cape", "Leather Armor"],
            "consumables": ["Health Potion", "Antidote"],
        },
        "dungeon": {
            "weapons": ["Steel Sword", "Axe", "Magic Stick"],
            "armors": ["Steel Armor", "Mystic Dress"],
            "consumables": ["Health Potion", "Bomb", "Antidote"],
        },
        "village": {
            "weapons": [],
            "armors": [],
            "consumables": ["Health Potion", "Antidote"],
        },
    }

    _drop_chances = {
        "forest": 0.4,
        "dungeon": 0.6,
        "village": 0.0,
    }

    def generate_loot(self, area_name: str) -> list[dict]:
        """Génère une liste de loot aléatoire pour une zone donnée.

        Args:
            area_name: Le nom de la zone ("forest", "dungeon", "village").

        Returns:
            Liste de dictionnaires décrivant les objets obtenus.

        Raises:
            ValueError: Si le nom de la zone est inconnu.
        """
        if area_name not in self._loot_table:
            raise ValueError(
                f"Zone inconnue : '{area_name}'. "
                f"Disponibles : {list(self._loot_table.keys())}"
            )

        drop_chance = self._drop_chances[area_name]
        if random.random() > drop_chance:
            return []

        table = self._loot_table[area_name]
        loot = []

        category = random.choice(["weapons", "armors", "consumables"])
        pool = table[category]

        if pool:
            item_name = random.choice(pool)
            loot.append(
                {
                    "name": item_name,
                    "category": category.rstrip("s"),
                    "source": area_name,
                }
            )

        return loot

    def generate_boss_loot(self, boss_name: str) -> list[dict]:
        """Génère du loot garanti après un combat de boss.

        Args:
            boss_name: Le nom du boss vaincu.

        Returns:
            Liste de dictionnaires décrivant les objets obtenus.

        Raises:
            ValueError: Si le nom du boss est inconnu.
        """
        boss_loot_table = {
            "Corrupted Champion": [
                {
                    "name": "Magic Stick",
                    "category": "weapon",
                    "source": "Corrupted Champion",
                },
                {
                    "name": "Mystic Dress",
                    "category": "armor",
                    "source": "Corrupted Champion",
                },
            ],
            "Dungeon Keeper": [
                {"name": "Axe", "category": "weapon", "source": "Dungeon Keeper"},
                {
                    "name": "Steel Armor",
                    "category": "armor",
                    "source": "Dungeon Keeper",
                },
            ],
        }

        if boss_name not in boss_loot_table:
            raise ValueError(
                f"Boss inconnu : '{boss_name}'. "
                f"Disponibles : {list(boss_loot_table.keys())}"
            )

        pool = boss_loot_table[boss_name]
        return [random.choice(pool)]
