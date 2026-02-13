# miniRPG

## Architecture RPG - Simple Factory & Python

![Architecture UML du projet](images/PlantUML_MiniRPG.jpg)

---

## Design Patterns

Voici les choix que nous avons faits :

### Factory

- **Abstract Factory** pour le personnage du joueur, les ennemis, les items et les zones.
  > Le Design Pattern *Builder* est plus adapté au projet mais il est lourd à mettre en place. Au vu du manque de temps sur le projet, il vaut mieux se rabattre sur une Abstract Factory.

### Combat

- **Facade** qui initialise des **Decorators** pour le moteur de combat.
- **Strategy** pour les effets et les statuts.
- **Observer** pour le Boss.

### Systèmes de jeu

| Système | Design Pattern | Justification |
|---------|---------------|---------------|
| Exploration par menu | **Iterator** | On a hésité à choisir le State mais ce dernier n'est pas adapté à l'exploration step by step du RPG. |
| Combat tour par tour | **Command & Strategy** | |
| Inventaire + équipement | **Strategy** | |
| Mini-ligne de quête | **State** | |
| Sauvegarde / chargement | **Adapter** | On voulait choisir le Memento mais ce design pattern est fait pour stocker dans la RAM donc non persistant. L'Adapter permet de convertir en JSON. |

---

## Structure du projet

```
miniRPG/
├── Factory/
│   ├── AreaFactory/
│   │   ├── AreaClasses/
│   │   │   ├── AreaBase.py
│   │   │   ├── AreaForest.py
│   │   │   ├── AreaVillage.py
│   │   │   └── AreaDungeon.py
│   │   └── AreaFactory.py
│   ├── EnemyFactory/
│   │   ├── EnemyClasses/
│   │   │   ├── EnemyBase.py
│   │   │   ├── SavageWolf.py
│   │   │   ├── Bandit.py
│   │   │   ├── Skeleton.py
│   │   │   ├── CorruptedChampion.py
│   │   │   └── DungeonKeeper.py
│   │   └── EnemyFactory.py
│   ├── ItemFactory/
│   │   ├── ItemClasses/
│   │   │   ├── Armor/
│   │   │   │   ├── ArmorBase.py
│   │   │   │   ├── CapeClass.py
│   │   │   │   ├── LeatherArmorClass.py
│   │   │   │   ├── MisticDressClass.py
│   │   │   │   ├── SteelArmorClass.py
│   │   │   │   └── ArmorFactory.py
│   │   │   ├── Consommable/
│   │   │   │   ├── ConsumableBase.py
│   │   │   │   ├── HealtPotionClass.py
│   │   │   │   ├── AntidoteClass.py
│   │   │   │   ├── BombClass.py
│   │   │   │   └── ConsumableFactory.py
│   │   │   ├── Quest/
│   │   │   │   ├── QuestItemBase.py
│   │   │   │   ├── KeyClass.py
│   │   │   │   └── QuestFactory.py
│   │   │   └── Weapon/
│   │   │       ├── WeaponBase.py
│   │   │       ├── WoodenSwordClass.py
│   │   │       ├── SteelSwordClass.py
│   │   │       ├── AxeClass.py
│   │   │       ├── KnifeClass.py
│   │   │       ├── BowClass.py
│   │   │       ├── MagicStickClass.py
│   │   │       └── WeaponFactory.py
│   │   └── ItemFactory.py
│   ├── PlayerFactory/
│   │   ├── PlayerClasses/
│   │   │   ├── PlayerBase.py
│   │   │   ├── Warrior.py
│   │   │   ├── Mage.py
│   │   │   └── Thief.py
│   │   └── PlayerFactory.py
│   └── LootFactory.py
├── Adapter/
│   └── SaveLoadAdapter.py
├── Observer/
│   └── Observer.py
├── State/
│   └── QuestState.py
├── Strategy/
│   ├── BattleStrategy.py
│   └── InventoryStrategy.py
└── images/
    └── PlantUML_MiniRPG.jpg
```

---

## Utilisation des Factories

### Créer un personnage

```python
from PlayerFactory.PlayerFactory import PlayerFactory

factory = PlayerFactory()
warrior = factory.create_player("warrior")   # dict avec les stats du guerrier
mage    = factory.create_player("mage")      # dict avec les stats du mage
thief   = factory.create_player("thief")     # dict avec les stats du voleur
```

### Créer un ennemi

```python
from EnemyFactory.EnemyFactory import EnemyFactory

factory = EnemyFactory()
wolf = factory.create_enemy("savage wolf")
boss = factory.create_enemy("corrupted champion")
```

### Créer un item

```python
from ItemFactory.ItemFactory import ItemFactory

factory = ItemFactory()
sword  = factory.create_item("weapon", "steel sword")
armor  = factory.create_item("armor", "leather armor")
potion = factory.create_item("consumable", "health potion")
key    = factory.create_item("quest", "key")
```

### Créer une zone

```python
from AreaFactory.AreaFactory import AreaFactory

factory = AreaFactory()
forest  = factory.create_area("forest")
village = factory.create_area("village")
dungeon = factory.create_area("dungeon")
```

### Générer du loot

```python
from LootFactory import LootFactory

loot_factory = LootFactory()
loot      = loot_factory.generate_loot("forest")
boss_loot = loot_factory.generate_boss_loot("Dungeon Keeper")
```
