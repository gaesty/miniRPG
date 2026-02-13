import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Strategy.BattleStrategy.BattleClasses.AgressiveStrategy import AggressiveStrategy
from Strategy.BattleStrategy.BattleClasses.DefensiveStrategy import DefensiveStrategy
from Strategy.BattleStrategy.BattleClasses.MixedStrategy import BalancedStrategy
from Strategy.BattleStrategy.BattleContext import BattleContext
from Command.CommandInvoker import CommandInvoker
from Command.CommandClasses.AttackCommand import AttackCommand
from Command.CommandClasses.DefendCommand import DefendCommand
from Decorator.DecoratorClasses.StrengthBoostDecorator import StrengthBoostDecorator
from Decorator.DecoratorClasses.DefenseBoostDecorator import DefenseBoostDecorator
from Decorator.DecoratorClasses.PoisonDecorator import PoisonDecorator
from Decorator.DecoratorClasses.RegenerationDecorator import RegenerationDecorator


class CombatFacade:
    """Facade qui simplifie et coordonne le système de combat complet."""

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.command_invoker = CommandInvoker()
        self.battle_context = BattleContext(BalancedStrategy())
        
        # Decorators actifs
        self.player_effects = []
        self.enemy_effects = []
        
        # État du combat
        self.turn_count = 0
        self.combat_log = []
        self.combat_active = True

    def start_combat(self):
        """Initialise et démarre le combat."""
        print("\n" + "="*50)
        print(f"COMBAT START: {self.player['name']} VS {self.enemy['name']}")
        print("="*50)
        print(f"{self.player['name']} HP: {self.player['pv']}")
        print(f"{self.enemy['name']} HP: {self.enemy['pv']}")
        print("="*50 + "\n")
        self.combat_active = True
        return True

    def player_attack(self, strategy_type="balanced"):
        """Le joueur attaque l'ennemi avec une stratégie choisie."""
        if not self.combat_active:
            print("Combat is not active!")
            return False

        # Sélectionner la stratégie
        strategy = self._get_strategy(strategy_type)
        self.battle_context.set_strategy(strategy)

        # Créer et exécuter la commande d'attaque
        attack_cmd = AttackCommand(self.player, self.enemy, self.battle_context.strategy)
        damage = self.command_invoker.execute_command(attack_cmd)

        self.turn_count += 1
        self.combat_log.append(f"Turn {self.turn_count}: {attack_cmd.get_description()} - {damage} damage")

        # Vérifier si l'ennemi est vaincu
        if self.enemy["pv"] <= 0:
            self._end_combat(winner=self.player)
            return True

        return True

    def enemy_attack(self):
        """L'ennemi attaque le joueur."""
        if not self.combat_active:
            return False

        # L'ennemi utilise une stratégie agressive
        strategy = AggressiveStrategy()
        attack_cmd = AttackCommand(self.enemy, self.player, strategy)
        damage = self.command_invoker.execute_command(attack_cmd)

        self.combat_log.append(f"Turn {self.turn_count}: {self.enemy['name']} attacks - {damage} damage")

        # Vérifier si le joueur est vaincu
        if self.player["pv"] <= 0:
            self._end_combat(winner=self.enemy)
            return True

        return True

    def player_defend(self):
        """Le joueur se met en défense."""
        if not self.combat_active:
            return False

        defend_cmd = DefendCommand(self.player)
        self.command_invoker.execute_command(defend_cmd)
        
        self.turn_count += 1
        self.combat_log.append(f"Turn {self.turn_count}: {self.player['name']} defends")
        
        return True

    def apply_effect_to_player(self, effect_type, **kwargs):
        """Applique un effet (decorator) au joueur."""
        decorator = self._create_decorator(effect_type, self.player, **kwargs)
        if decorator:
            decorator.apply_effect()
            self.player_effects.append(decorator)
            return True
        return False

    def apply_effect_to_enemy(self, effect_type, **kwargs):
        """Applique un effet (decorator) à l'ennemi."""
        decorator = self._create_decorator(effect_type, self.enemy, **kwargs)
        if decorator:
            decorator.apply_effect()
            self.enemy_effects.append(decorator)
            return True
        return False

    def process_turn_effects(self):
        """Traite les effets actifs (poison, régénération, etc.) en début de tour."""
        print("\n--- Processing active effects ---")
        
        # Traiter les effets du joueur
        self.player_effects = [
            effect for effect in self.player_effects
            if hasattr(effect, 'is_active') and effect.is_active() and effect.apply_effect()
        ]

        # Traiter les effets de l'ennemi
        self.enemy_effects = [
            effect for effect in self.enemy_effects
            if hasattr(effect, 'is_active') and effect.is_active() and effect.apply_effect()
        ]

        # Vérifier les conditions de victoire après les effets
        if self.enemy["pv"] <= 0:
            self._end_combat(winner=self.player)
        elif self.player["pv"] <= 0:
            self._end_combat(winner=self.enemy)

    def get_combat_status(self):
        """Retourne l'état actuel du combat."""
        return {
            "turn": self.turn_count,
            "player_hp": self.player["pv"],
            "enemy_hp": self.enemy["pv"],
            "player_effects": len(self.player_effects),
            "enemy_effects": len(self.enemy_effects),
            "combat_active": self.combat_active
        }

    def display_combat_status(self):
        """Affiche l'état du combat."""
        print(f"\n--- Turn {self.turn_count} ---")
        print(f"{self.player['name']} HP: {self.player['pv']}")
        print(f"{self.enemy['name']} HP: {self.enemy['pv']}")
        print(f"Active effects on player: {len(self.player_effects)}")
        print(f"Active effects on enemy: {len(self.enemy_effects)}")

    def _get_strategy(self, strategy_type):
        """Retourne une instance de stratégie selon le type."""
        strategies = {
            "aggressive": AggressiveStrategy(),
            "defensive": DefensiveStrategy(),
            "balanced": BalancedStrategy()
        }
        return strategies.get(strategy_type, BalancedStrategy())

    def _create_decorator(self, effect_type, target, **kwargs):
        """Crée un decorator selon le type d'effet."""
        decorators = {
            "strength": lambda: StrengthBoostDecorator(target, kwargs.get("boost", 10)),
            "defense": lambda: DefenseBoostDecorator(target, kwargs.get("boost", 10)),
            "poison": lambda: PoisonDecorator(target, kwargs.get("damage", 5), kwargs.get("duration", 3)),
            "regeneration": lambda: RegenerationDecorator(target, kwargs.get("heal", 10), kwargs.get("duration", 3))
        }
        creator = decorators.get(effect_type)
        return creator() if creator else None

    def _end_combat(self, winner):
        """Termine le combat et affiche le résultat."""
        self.combat_active = False
        print("\n" + "="*50)
        print(f"COMBAT END - {winner['name']} WINS!")
        print("="*50)
        print(f"Combat lasted {self.turn_count} turns")
        
        # Nettoyer les effets
        for effect in self.player_effects + self.enemy_effects:
            if hasattr(effect, 'remove_effect'):
                effect.remove_effect()
        
        self.player_effects.clear()
        self.enemy_effects.clear()

    def get_combat_log(self):
        """Retourne l'historique complet du combat."""
        return self.combat_log

    def undo_last_action(self):
        """Annule la dernière action (si possible)."""
        return self.command_invoker.undo_last()
