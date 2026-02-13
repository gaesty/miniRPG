import json
import os
from datetime import datetime


class SaveLoadAdapter:

    def __init__(self, save_directory="saves"):
        self.save_directory = save_directory
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

    def save_game(self, game_state: dict, save_name: str = None) -> str:
        if not game_state:
            raise ValueError("L'état du jeu ne peut pas être vide.")

        if save_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_name = f"save_{timestamp}"

        if not save_name.endswith(".json"):
            save_name += ".json"

        file_path = os.path.join(self.save_directory, save_name)

        game_state["save_metadata"] = {
            "save_date": datetime.now().isoformat(),
            "save_name": save_name,
        }

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(game_state, file, indent=4, ensure_ascii=False)
            print(f"Game saved successfully to: {file_path}")
            return file_path
        except Exception as e:
            raise IOError(f"Failed to save game: {e}")

    def load_game(self, save_name: str) -> dict:
        if not save_name.endswith(".json"):
            save_name += ".json"

        file_path = os.path.join(self.save_directory, save_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Save file not found: {file_path}. "
                f"Available saves: {self.list_saves()}"
            )

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                game_state = json.load(file)
            print(f"Game loaded successfully from: {file_path}")
            return game_state
        except json.JSONDecodeError as e:
            raise ValueError(f"Corrupted save file: {e}")
        except Exception as e:
            raise IOError(f"Failed to load game: {e}")

    def list_saves(self) -> list:
        if not os.path.exists(self.save_directory):
            return []

        saves = [
            f
            for f in os.listdir(self.save_directory)
            if f.endswith(".json")
        ]
        return sorted(saves, reverse=True)

    def delete_save(self, save_name: str) -> bool:
        if not save_name.endswith(".json"):
            save_name += ".json"

        file_path = os.path.join(self.save_directory, save_name)

        if not os.path.exists(file_path):
            print(f"Save file not found: {file_path}")
            return False

        try:
            os.remove(file_path)
            print(f"Save deleted successfully: {file_path}")
            return True
        except Exception as e:
            print(f"Failed to delete save: {e}")
            return False

    def create_game_state(
        self,
        player: dict,
        inventory: dict,
        quests: list,
        current_area: dict,
        game_progress: dict,
    ) -> dict:

        return {
            "player": player,
            "inventory": inventory,
            "quests": quests,
            "current_area": current_area,
            "game_progress": game_progress,
        }

    def get_save_info(self, save_name: str) -> dict:
        if not save_name.endswith(".json"):
            save_name += ".json"

        file_path = os.path.join(self.save_directory, save_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Save file not found: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                game_state = json.load(file)
            
            return {
                "save_name": save_name,
                "save_metadata": game_state.get("save_metadata", {}),
                "player_name": game_state.get("player", {}).get("name", "Unknown"),
                "player_class": game_state.get("player", {}).get("description", "Unknown"),
                "current_area": game_state.get("current_area", {}).get("name", "Unknown"),
            }
        except Exception as e:
            raise IOError(f"Failed to read save info: {e}")
