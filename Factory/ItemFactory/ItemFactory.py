from ItemClasses.Armor.ArmorFactory import ArmorFactory
from ItemClasses.Consommable.ConsumableFactory import ConsumableFactory
from ItemClasses.Quest.QuestFactory import QuestFactory
from ItemClasses.Weapon.WeaponFactory import WeaponFactory


class ItemFactory:
    """Factory centrale pour créer n'importe quel type d'item."""

    def __init__(self):
        self._weapon_factory = WeaponFactory()
        self._armor_factory = ArmorFactory()
        self._consumable_factory = ConsumableFactory()
        self._quest_factory = QuestFactory()

    def create_item(self, category: str, name: str) -> dict:
        """Crée un item selon sa catégorie et son nom.

        Args:
            category: Type d'item parmi 'weapon', 'armor', 'consumable', 'quest'.
            name: Nom de l'item à créer.

        Returns:
            Dictionnaire contenant les données de l'item.

        Raises:
            ValueError: Si la catégorie est inconnue.
        """
        factory_map = {
            "weapon": self._weapon_factory.create_weapon,
            "armor": self._armor_factory.create_armor,
            "consumable": self._consumable_factory.create_consumable,
            "quest": self._quest_factory.create_quest_item,
        }
        creator = factory_map.get(category)
        if creator is None:
            raise ValueError(
                f"Catégorie inconnue : '{category}'. "
                f"Disponibles : {list(factory_map.keys())}"
            )
        return creator(name)
