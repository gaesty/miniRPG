import sys
import os

# Ajouter le répertoire du projet au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GameManager import GameManager
from Iterator.MenuIterator import MenuIterator


def display_main_menu():
    """Affiche le menu principal."""
    print("\n" + "="*50)
    print(" "*15 + "MINI RPG")
    print("="*50)
    print("1. New Game")
    print("2. Load Game")
    print("3. List Saves")
    print("4. Exit")
    print("="*50)


def display_game_menu():
    """Affiche le menu de jeu."""
    print("\n" + "="*50)
    print("GAME MENU")
    print("="*50)
    print("1. Explore (Move to next area)")
    print("2. Start Combat")
    print("3. View Inventory")
    print("4. View Quests")
    print("5. View Status")
    print("6. Save Game")
    print("7. Return to Main Menu")
    print("="*50)


def display_combat_menu():
    """Affiche le menu de combat."""
    print("\n--- COMBAT OPTIONS ---")
    print("1. Attack (Aggressive)")
    print("2. Attack (Balanced)")
    print("3. Attack (Defensive)")
    print("4. Defend")
    print("5. Use Item")
    print("6. View Combat Status")


def handle_new_game(game_manager):
    """Gère la création d'une nouvelle partie."""
    print("\n=== NEW GAME ===")
    print("Choose your class:")
    print("1. Warrior - Specialty: Close combat and resistance")
    print("2. Mage - Specialization: Offensive and Control Magic")
    print("3. Thief - Specialty: speed")
    
    class_choice = input("\nEnter choice (1-3): ").strip()
    
    class_map = {
        "1": "warrior",
        "2": "mage",
        "3": "thief"
    }
    
    player_class = class_map.get(class_choice, "warrior")
    game_manager.initialize_game(player_class)
    
    print(f"\nGame started with class: {player_class}")
    return True


def handle_load_game(game_manager):
    """Gère le chargement d'une partie."""
    saves = game_manager.save_adapter.list_saves()
    
    if not saves:
        print("\nNo save files found!")
        return False
    
    print("\n=== AVAILABLE SAVES ===")
    for i, save in enumerate(saves, 1):
        print(f"{i}. {save}")
    
    choice = input("\nEnter save number to load (or 0 to cancel): ").strip()
    
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(saves):
            save_name = saves[choice_idx]
            return game_manager.load_game(save_name)
    except ValueError:
        pass
    
    return False


def handle_combat(game_manager):
    """Gère une session de combat complète."""
    if not game_manager.current_combat:
        print("No active combat!")
        return
    
    while game_manager.current_combat and game_manager.current_combat.combat_active:
        display_combat_menu()
        choice = input("\nYour action: ").strip()
        
        if choice == "1":
            game_manager.execute_combat_turn("attack", "aggressive")
        elif choice == "2":
            game_manager.execute_combat_turn("attack", "balanced")
        elif choice == "3":
            game_manager.execute_combat_turn("attack", "defensive")
        elif choice == "4":
            game_manager.execute_combat_turn("defend")
        elif choice == "5":
            game_manager.execute_combat_turn("item")
        elif choice == "6":
            if game_manager.current_combat:
                game_manager.current_combat.display_combat_status()
        else:
            print("Invalid choice!")
        
        # Vérifier si le combat est terminé
        if not game_manager.current_combat or not game_manager.current_combat.combat_active:
            break
        
        input("\nPress Enter to continue...")


def handle_game_menu(game_manager):
    """Gère le menu principal du jeu."""
    while True:
        display_game_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            # Explorer la zone suivante
            if game_manager.explore_next_area():
                print("Moved to new area!")
            else:
                print("No more areas to explore!")
        
        elif choice == "2":
            # Démarrer un combat
            current_area = game_manager.exploration_system.get_current_area()
            if current_area.get("area_safe"):
                print("This area is safe - no enemies here!")
            else:
                if game_manager.start_combat():
                    handle_combat(game_manager)
        
        elif choice == "3":
            # Voir l'inventaire
            print("\n=== INVENTORY ===")
            if game_manager.inventory["items"]:
                for i, item in enumerate(game_manager.inventory["items"], 1):
                    print(f"{i}. {item.get('name')} ({item.get('category', 'unknown')})")
            else:
                print("Inventory is empty!")
            
            equipped = game_manager.inventory.get("equipped", {})
            if equipped:
                print("\n--- EQUIPPED ---")
                for slot, item in equipped.items():
                    print(f"{slot}: {item.get('name')}")
        
        elif choice == "4":
            # Voir les quêtes
            print("\n=== QUESTS ===")
            if game_manager.quests:
                for i, quest in enumerate(game_manager.quests, 1):
                    info = quest.get_info()
                    print(f"{i}. {info['name']} - Status: {info['status']}")
                    print(f"   {info['description']}")
            else:
                print("No quests available!")
        
        elif choice == "5":
            # Voir le statut
            game_manager.display_game_state()
        
        elif choice == "6":
            # Sauvegarder
            save_name = input("\nEnter save name (or press Enter for auto-name): ").strip()
            save_name = save_name if save_name else None
            file_path = game_manager.save_game(save_name)
            print(f"Game saved to: {file_path}")
        
        elif choice == "7":
            # Retour au menu principal
            print("Returning to main menu...")
            break
        
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")


def main():
    """Fonction principale du jeu."""
    game_manager = GameManager()
    game_active = False
    
    while True:
        display_main_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            # Nouvelle partie
            if handle_new_game(game_manager):
                game_active = True
                handle_game_menu(game_manager)
        
        elif choice == "2":
            # Charger une partie
            if handle_load_game(game_manager):
                game_active = True
                handle_game_menu(game_manager)
        
        elif choice == "3":
            # Liste des sauvegardes
            saves = game_manager.save_adapter.list_saves()
            if saves:
                print("\n=== SAVED GAMES ===")
                for i, save in enumerate(saves, 1):
                    try:
                        info = game_manager.save_adapter.get_save_info(save)
                        print(f"\n{i}. {save}")
                        print(f"   Player: {info['player_name']}")
                        print(f"   Class: {info['player_class']}")
                        print(f"   Area: {info['current_area']}")
                        print(f"   Date: {info['save_metadata'].get('save_date', 'Unknown')}")
                    except:
                        print(f"{i}. {save}")
            else:
                print("\nNo saved games found!")
            
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            # Quitter
            print("\nThank you for playing miniRPG!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1-4.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
        import traceback
        traceback.print_exc()
