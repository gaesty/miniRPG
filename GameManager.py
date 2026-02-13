import os
import random
import sys

# Ajouter le répertoire parent au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Adapter.SaveLoadAdapter import SaveLoadAdapter
from Facade.CombatFacade import CombatFacade
from Factory.AreaFactory.AreaFactory import AreaFactory
from Factory.EnemyFactory.EnemyFactory import EnemyFactory
from Factory.ItemFactory.ItemFactory import ItemFactory
from Factory.LootFactory import LootFactory
from Factory.PlayerFactory.PlayerFactory import PlayerFactory
from Iterator.AreaIterator import AreaIterator
from Iterator.ExplorationSystem import ExplorationSystem
from Iterator.MenuIterator import MenuIterator
from Observer.Observer import DungeonEvent, FinalBoss
from State.QuestState import Completed, InProgress, NotStarted, Quest


class GameManager:
    """Gestionnaire principal qui orchestre tous les systèmes du jeu."""

    def __init__(self):
        # Factories
        self.player_factory = PlayerFactory()
        self.enemy_factory = EnemyFactory()
        self.area_factory = AreaFactory()
        self.item_factory = ItemFactory()
        self.loot_factory = LootFactory()

        # Systèmes
        self.save_adapter = SaveLoadAdapter()
        self.dungeon_event = DungeonEvent()
        self.final_boss = FinalBoss()

        # État du jeu
        self.player = None
        self.inventory = {"items": [], "equipped": {}}
        self.quests = []
        self.areas = []
        self.exploration_system = None
        self.current_combat = None
        self.game_progress = {
            "level": 1,
            "enemies_defeated": 0,
            "bosses_defeated": 0,
            "areas_explored": 0,
        }

        # Observer pour le boss final
        self.dungeon_event.register(self.final_boss)

    def initialize_game(self, player_class="warrior"):
        """Initialise une nouvelle partie."""
        print("\n=== INITIALIZING NEW GAME ===")

        # Créer le joueur
        self.player = self.player_factory.create_player(player_class)
        print(f"Player created: {self.player['description']}")

        # Créer les zones
        self.areas = [
            self.area_factory.create_area("village"),
            self.area_factory.create_area("forest"),
            self.area_factory.create_area("dungeon"),
        ]

        # Initialiser le système d'exploration
        area_iterator = AreaIterator(self.areas)
        self.exploration_system = ExplorationSystem(area_iterator)
        self.exploration_system.start_exploration()

        # Créer une quête initiale
        starter_quest = Quest(
            "Defeat the Dungeon Keeper",
            "Explore the dungeon and defeat the final boss",
            {"gold": 100, "experience": 500},
        )
        self.quests.append(starter_quest)

        # Ajouter quelques objets de départ
        starting_potion = self.item_factory.create_item("consumable", "health potion")
        self.inventory["items"].append(starting_potion)

        print(f"Starting area: {self.exploration_system.get_current_area()['name']}")
        print("Game initialized successfully!\n")

    def start_combat(self, enemy_name=None):
        """Démarre un combat contre un ennemi."""
        current_area = self.exploration_system.get_current_area()

        # Sélectionner un ennemi
        if enemy_name is None:
            enemy_types = current_area.get("enemy_type", [])
            if not enemy_types:
                print("No enemies in this area!")
                return False
            enemy_name = random.choice(enemy_types).lower()

        try:
            enemy = self.enemy_factory.create_enemy(enemy_name)
            print(f"\nEncountered: {enemy['name']} - {enemy['description']}")

            # Créer la facade de combat
            self.current_combat = CombatFacade(self.player, enemy)
            self.current_combat.start_combat()

            return True
        except ValueError as e:
            print(f"Error creating enemy: {e}")
            return False

    def execute_combat_turn(self, action="attack", strategy="balanced"):
        """Exécute un tour de combat."""
        if not self.current_combat or not self.current_combat.combat_active:
            print("No active combat!")
            return False

        # Traiter les effets de début de tour
        self.current_combat.process_turn_effects()

        if not self.current_combat.combat_active:
            return self._handle_combat_end()

        # Action du joueur
        if action == "attack":
            self.current_combat.player_attack(strategy)
        elif action == "defend":
            self.current_combat.player_defend()
        elif action == "item":
            # Utiliser un objet de soin si disponible
            health_potions = [
                item
                for item in self.inventory["items"]
                if item.get("name") == "Health Potion"
            ]
            if health_potions:
                potion = health_potions[0]
                heal_amount = potion.get("pv_restore", potion.get("value", 30))
                self.player["pv"] += heal_amount
                self.inventory["items"].remove(potion)
                print(f"{self.player['name']} used Health Potion! (+{heal_amount} HP)")
            else:
                print("No items to use!")

        if not self.current_combat.combat_active:
            return self._handle_combat_end()

        # Tour de l'ennemi
        self.current_combat.enemy_attack()

        # Afficher l'état du combat
        self.current_combat.display_combat_status()

        if not self.current_combat.combat_active:
            return self._handle_combat_end()

        return True

    def _handle_combat_end(self):
        """Gère la fin d'un combat."""
        if self.player["pv"] <= 0:
            print("\n=== GAME OVER ===")
            return False
        else:
            enemy_name = self.current_combat.enemy["name"]
            print(f"\nVictory! {enemy_name} defeated!")

            # Progression
            self.game_progress["enemies_defeated"] += 1

            # Vérifier si c'est un boss
            if self.current_combat.enemy.get("type") == "boss":
                self.game_progress["bosses_defeated"] += 1
                print("Boss defeated! Legendary loot obtained!")

                # Notifier l'observer pour le boss final
                if self.game_progress["bosses_defeated"] >= 1:
                    self.dungeon_event.enemy_defeated(
                        self.game_progress["bosses_defeated"]
                    )

            # Générer du loot
            area_name = self.exploration_system.get_current_area()["name"]
            loot = self.loot_factory.generate_loot(area_name)
            if loot:
                for item in loot:
                    self.inventory["items"].append(item)
                    print(f"Found: {item['name']}")

            self.current_combat = None
            return True

    def explore_next_area(self):
        """Se déplace vers la zone suivante."""
        next_area = self.exploration_system.move_to_next_area()
        if next_area:
            self.game_progress["areas_explored"] += 1
            return True
        return False

    def manage_quests(self, quest_index=0, action="start"):
        """Gère les quêtes (start, complete, fail)."""
        if quest_index < len(self.quests):
            quest = self.quests[quest_index]

            if action == "start":
                quest.start()
            elif action == "complete":
                quest.complete()
            elif action == "fail":
                quest.fail()

            return True
        return False

    def save_game(self, save_name=None):
        """Sauvegarde l'état actuel du jeu."""
        game_state = self.save_adapter.create_game_state(
            player=self.player,
            inventory=self.inventory,
            quests=[q.get_info() for q in self.quests],
            current_area=self.exploration_system.get_current_area(),
            game_progress=self.game_progress,
        )

        file_path = self.save_adapter.save_game(game_state, save_name)
        return file_path

    def load_game(self, save_name):
        """Charge une partie sauvegardée."""
        try:
            game_state = self.save_adapter.load_game(save_name)

            self.player = game_state.get("player")
            self.inventory = game_state.get("inventory")
            self.game_progress = game_state.get("game_progress")

            # Recréer les zones et le système d'exploration
            self.areas = [
                self.area_factory.create_area("village"),
                self.area_factory.create_area("forest"),
                self.area_factory.create_area("dungeon"),
            ]
            area_iterator = AreaIterator(self.areas)
            self.exploration_system = ExplorationSystem(area_iterator)

            # Avancer l'itérateur jusqu'à la zone sauvegardée
            saved_area_name = game_state.get("current_area", {}).get("name")
            self.exploration_system.start_exploration()
            if saved_area_name:
                while (
                    self.exploration_system.get_current_area()
                    and self.exploration_system.get_current_area().get("name")
                    != saved_area_name
                    and area_iterator.has_next()
                ):
                    self.exploration_system.move_to_next_area()

            # Recréer les quêtes
            self.quests = []
            for quest_info in game_state.get("quests", []):
                quest = Quest(
                    quest_info["name"], quest_info["description"], quest_info["reward"]
                )
                # Restaurer l'état de la quête
                status = quest_info.get("status")
                if status == "In Progress":
                    quest.start()
                elif status == "Completed":
                    quest.start()
                    quest.complete()
                elif status == "Failed":
                    quest.start()
                    quest.fail()

                self.quests.append(quest)

            print("Game loaded successfully!")
            return True
        except Exception as e:
            print(f"Failed to load game: {e}")
            return False

    def get_game_state_summary(self):
        """Retourne un résumé de l'état du jeu."""
        return {
            "player": self.player["name"] if self.player else "None",
            "player_hp": self.player["pv"] if self.player else 0,
            "current_area": self.exploration_system.get_current_area()["name"]
            if self.exploration_system
            else "None",
            "inventory_items": len(self.inventory["items"]),
            "active_quests": len(
                [q for q in self.quests if q.get_status() == "In Progress"]
            ),
            "completed_quests": len(
                [q for q in self.quests if q.get_status() == "Completed"]
            ),
            "enemies_defeated": self.game_progress["enemies_defeated"],
            "bosses_defeated": self.game_progress["bosses_defeated"],
            "areas_explored": self.game_progress["areas_explored"],
        }

    def display_game_state(self):
        """Affiche l'état actuel du jeu."""
        print("\n" + "=" * 50)
        print("GAME STATE")
        print("=" * 50)

        if self.player:
            print(f"Player: {self.player['name']}")
            print(f"HP: {self.player['pv']}")
            print(f"Description: {self.player['description']}")

        if self.exploration_system:
            area = self.exploration_system.get_current_area()
            print(f"\nCurrent Area: {area['name']}")
            print(f"Area Type: {area['area_type']}")

        print(f"\nInventory: {len(self.inventory['items'])} items")
        print(
            f"Active Quests: {len([q for q in self.quests if q.get_status() == 'In Progress'])}"
        )

        print(f"\nProgress:")
        print(f"  Enemies Defeated: {self.game_progress['enemies_defeated']}")
        print(f"  Bosses Defeated: {self.game_progress['bosses_defeated']}")
        print(f"  Areas Explored: {self.game_progress['areas_explored']}")
        print("=" * 50 + "\n")
