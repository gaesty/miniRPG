# miniRPG

## Architecture RPG - Design Patterns & Python

![Architecture UML du projet](images/PlantUML_MiniRPG.png)

---

## Lancer le jeu

```bash
python main.py
```

---

## Design Patterns

Voici les choix que nous avons faits :

### Factory

- **Abstract Factory** pour le personnage du joueur, les ennemis, les items et les zones.
  > Le Design Pattern *Builder* est plus adapté au projet mais il est lourd à mettre en place. Au vu du manque de temps sur le projet, il vaut mieux se rabattre sur une Abstract Factory.

### Combat

- **Facade** (`CombatFacade`) qui coordonne le système de combat complet : stratégies, commandes et décorateurs.
- **Decorator** (`CombatDecorator`) pour ajouter dynamiquement des effets temporaires aux combattants (boost de force, boost de défense, poison, régénération).
- **Command** (`CommandInvoker`) pour encapsuler les actions de combat (attaque, défense, fuite, utilisation d'objet) avec support undo/redo.
- **Strategy** pour les stratégies de combat (agressive, défensive, équilibrée, compétence spéciale), les effets de statut (poison, bouclier, étourdissement) et la gestion de l'inventaire (ajout, retrait, équipement, utilisation).
- **Observer** pour le Boss final du donjon — le `DungeonEvent` notifie le `FinalBoss` lorsque suffisamment d'ennemis ont été vaincus.

### Systèmes de jeu

| Système | Design Pattern | Justification |
|---------|---------------|---------------|
| Exploration par menu | **Iterator** | On a hésité à choisir le State mais ce dernier n'est pas adapté à l'exploration step by step du RPG. `AreaIterator` parcourt les zones, `MenuIterator` parcourt les options de menu, et `ExplorationSystem` orchestre la navigation. |
| Combat tour par tour | **Command, Strategy & Facade** | `CommandInvoker` gère l'historique des actions (undo/redo). Les `BattleStrategy` définissent le comportement offensif/défensif. La `CombatFacade` simplifie l'ensemble. |
| Effets de combat | **Decorator** | Les `CombatDecorator` ajoutent dynamiquement des effets temporaires (poison, régénération, boost) aux combattants sans modifier leurs classes. |
| Effets de statut | **Strategy** | Les `StatusEffectStrategy` appliquent des effets (poison, bouclier, étourdissement) avec gestion de durée. |
| Inventaire + équipement | **Strategy** | Les `InventoryStrategy` encapsulent les différentes actions (ajouter, retirer, équiper, utiliser). |
| Mini-ligne de quête | **State** | Les états `NotStarted`, `InProgress`, `Completed` et `Failed` gèrent les transitions de la quête. |
| Sauvegarde / chargement | **Adapter** | On voulait choisir le Memento mais ce design pattern est fait pour stocker dans la RAM donc non persistant. L'Adapter permet de convertir en JSON. |

---

## Structure du projet

```
miniRPG/
├── main.py                          # Point d'entrée du jeu (menus)
├── GameManager.py                   # Orchestrateur principal de tous les systèmes
├── miniRPG_UML.puml                 # Diagramme UML PlantUML source
│
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
│
├── Command/
│   ├── Command.py                   # Interface de base (execute, undo)
│   ├── CommandInvoker.py            # Invocateur avec historique undo/redo
│   └── CommandClasses/
│       ├── AttackCommand.py
│       ├── DefendCommand.py
│       ├── FleeCommand.py
│       └── UseItemCommand.py
│
├── Decorator/
│   ├── CombatDecorator.py           # Decorator de base pour les combattants
│   └── DecoratorClasses/
│       ├── StrengthBoostDecorator.py
│       ├── DefenseBoostDecorator.py
│       ├── PoisonDecorator.py
│       └── RegenerationDecorator.py
│
├── Facade/
│   └── CombatFacade.py              # Facade coordonnant Strategy + Command + Decorator
│
├── Iterator/
│   ├── AreaIterator.py              # Iterator pour parcourir les zones
│   ├── MenuIterator.py              # Iterator pour parcourir les menus
│   └── ExplorationSystem.py         # Système d'exploration utilisant AreaIterator
│
├── Observer/
│   └── Observer.py                  # DungeonEvent + FinalBoss (Observer Pattern)
│
├── State/
│   └── QuestState.py                # États : NotStarted, InProgress, Completed, Failed
│
├── Strategy/
│   ├── BattleStrategy/
│   │   ├── BattleStrategy.py        # Interface abstraite
│   │   ├── BattleContext.py          # Contexte qui utilise la stratégie active
│   │   └── BattleClasses/
│   │       ├── AgressiveStrategy.py
│   │       ├── DefensiveStrategy.py
│   │       ├── MixedStrategy.py
│   │       └── SpecialSkillStrategy.py
│   ├── InventoryStrategy/
│   │   ├── InventoryStrategy.py      # Interface abstraite
│   │   ├── InventoryContext.py       # Contexte qui utilise la stratégie active
│   │   └── InventoryClasses/
│   │       ├── AddItemStrategy.py
│   │       ├── RemoveItemStrategy.py
│   │       ├── EquipItemStrategy.py
│   │       └── UseItemStrategy.py
│   └── StatusEffectStrategy/
│       ├── StatusEffectStrategy.py   # Interface abstraite
│       ├── StatusEffectContext.py    # Contexte qui utilise la stratégie active
│       └── StatusEffectClasses/
│           ├── Poison.py
│           ├── Shield.py
│           └── Dizziness.py
│
├── Adapter/
│   └── SaveLoadAdapter.py           # Conversion état du jeu ↔ JSON (persistance)
│
├── saves/                           # Répertoire des sauvegardes JSON
│
└── images/
    ├── PlantUML_MiniRPG.jpg
    └── PlantUML_MiniRPG.png
```

---

## Utilisation des Factories

### Créer un personnage

```python
from Factory.PlayerFactory.PlayerFactory import PlayerFactory

factory = PlayerFactory()
warrior = factory.create_player("warrior")   # dict avec les stats du guerrier
mage    = factory.create_player("mage")      # dict avec les stats du mage
thief   = factory.create_player("thief")     # dict avec les stats du voleur
```

### Créer un ennemi

```python
from Factory.EnemyFactory.EnemyFactory import EnemyFactory

factory = EnemyFactory()
wolf = factory.create_enemy("savage wolf")
boss = factory.create_enemy("corrupted champion")
```

### Créer un item

```python
from Factory.ItemFactory.ItemFactory import ItemFactory

factory = ItemFactory()
sword  = factory.create_item("weapon", "steel sword")
armor  = factory.create_item("armor", "leather armor")
potion = factory.create_item("consumable", "health potion")
key    = factory.create_item("quest", "key")
```

### Créer une zone

```python
from Factory.AreaFactory.AreaFactory import AreaFactory

factory = AreaFactory()
forest  = factory.create_area("forest")
village = factory.create_area("village")
dungeon = factory.create_area("dungeon")
```

### Générer du loot

```python
from Factory.LootFactory import LootFactory

loot_factory = LootFactory()
loot      = loot_factory.generate_loot("forest")
boss_loot = loot_factory.generate_boss_loot("Dungeon Keeper")
```

---

## Utilisation du système de combat (Facade + Command + Decorator)

### Lancer un combat complet

```python
from Facade.CombatFacade import CombatFacade
from Factory.PlayerFactory.PlayerFactory import PlayerFactory
from Factory.EnemyFactory.EnemyFactory import EnemyFactory

# Créer joueur et ennemi
player = PlayerFactory().create_player("warrior")
enemy  = EnemyFactory().create_enemy("savage wolf")

# Initialiser le combat via la Facade
combat = CombatFacade(player, enemy)
combat.start_combat()

# Tour du joueur : attaquer avec une stratégie
combat.player_attack("aggressive")   # ou "balanced", "defensive"

# Tour de l'ennemi
combat.enemy_attack()

# Se défendre
combat.player_defend()

# Appliquer des effets (Decorators)
combat.apply_effect_to_player("strength", boost=10)
combat.apply_effect_to_enemy("poison", damage=5, duration=3)
combat.apply_effect_to_player("regeneration", heal=10, duration=3)

# Traiter les effets en début de tour
combat.process_turn_effects()

# Voir l'état du combat
combat.display_combat_status()

# Annuler la dernière action (undo via CommandInvoker)
combat.undo_last_action()
```

---

## Utilisation de l'exploration (Iterator)

```python
from Factory.AreaFactory.AreaFactory import AreaFactory
from Iterator.AreaIterator import AreaIterator
from Iterator.ExplorationSystem import ExplorationSystem

# Créer les zones
area_factory = AreaFactory()
areas = [
    area_factory.create_area("village"),
    area_factory.create_area("forest"),
    area_factory.create_area("dungeon"),
]

# Initialiser le système d'exploration
iterator = AreaIterator(areas)
exploration = ExplorationSystem(iterator)

# Commencer l'exploration
exploration.start_exploration()

# Se déplacer à la zone suivante
exploration.move_to_next_area()

# Consulter la zone actuelle
current = exploration.get_current_area()
print(current["name"])

# Vérifier si la zone est sûre
print(exploration.is_area_safe())

# Voir la progression
print(exploration.get_exploration_progress())
```

---

## Utilisation des quêtes (State)

```python
from State.QuestState import Quest

quest = Quest(
    "Defeat the Dungeon Keeper",
    "Explore the dungeon and defeat the final boss",
    {"gold": 100, "experience": 500}
)

print(quest.get_status())  # "Not Started"

quest.start()              # → "In Progress"
quest.complete()           # → "Completed"

# Consulter les infos
info = quest.get_info()
# {"name": "...", "description": "...", "reward": {...}, "status": "Completed"}
```

---

## Utilisation de l'Observer (Boss final)

```python
from Observer.Observer import DungeonEvent, FinalBoss

# Créer l'événement et le boss
dungeon_event = DungeonEvent()
final_boss = FinalBoss()

# Enregistrer le boss comme observateur
dungeon_event.register(final_boss)

# Notifier quand assez d'ennemis sont vaincus
dungeon_event.enemy_defeated(1)  # "Final Boss is ready!"
print(final_boss.is_awake)       # True
```

---

## Sauvegarde / Chargement (Adapter)

```python
from Adapter.SaveLoadAdapter import SaveLoadAdapter

adapter = SaveLoadAdapter(save_directory="saves")

# Créer un état de jeu
game_state = adapter.create_game_state(
    player={"name": "Hero", "pv": 100},
    inventory={"items": [], "equipped": {}},
    quests=[],
    current_area={"name": "Village"},
    game_progress={"level": 1, "enemies_defeated": 0}
)

# Sauvegarder en JSON
file_path = adapter.save_game(game_state, "my_save")

# Charger une sauvegarde
loaded_state = adapter.load_game("my_save")

# Lister les sauvegardes disponibles
saves = adapter.list_saves()

# Supprimer une sauvegarde
adapter.delete_save("my_save")
```

---

## GameManager — Orchestrateur principal

Le `GameManager` est le point central qui connecte tous les systèmes :

- **Factories** : création du joueur, des ennemis, des zones, des items et du loot
- **Facade** : initialisation et gestion des combats
- **Iterator** : navigation entre les zones via `ExplorationSystem`
- **Observer** : notification du boss final
- **State** : gestion des quêtes
- **Adapter** : sauvegarde et chargement de la partie

```python
from GameManager import GameManager

gm = GameManager()

# Nouvelle partie
gm.initialize_game("warrior")

# Explorer
gm.explore_next_area()

# Démarrer un combat
gm.start_combat()
gm.execute_combat_turn("attack", "aggressive")

# Gérer les quêtes
gm.manage_quests(quest_index=0, action="start")

# Sauvegarder / Charger
gm.save_game("my_save")
gm.load_game("my_save")

# Voir l'état du jeu
gm.display_game_state()
```
