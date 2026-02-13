class ExplorationSystem:
    """Système d'exploration utilisant l'iterator pour naviguer entre zones."""

    def __init__(self, area_iterator):
        self.area_iterator = area_iterator
        self.current_area = None
        self.visited_areas = []

    def start_exploration(self):
        """Commence l'exploration avec la première zone."""
        self.area_iterator.reset()
        if self.area_iterator.has_next():
            self.current_area = next(self.area_iterator)
            self.visited_areas.append(self.current_area)
            print(f"\n=== Entering {self.current_area['name']} ===")
            self._display_area_info()
            return self.current_area
        return None

    def move_to_next_area(self):
        """Se déplace vers la zone suivante."""
        if self.area_iterator.has_next():
            self.current_area = next(self.area_iterator)
            self.visited_areas.append(self.current_area)
            print(f"\n=== Moving to {self.current_area['name']} ===")
            self._display_area_info()
            return self.current_area
        else:
            print("No more areas to explore!")
            return None

    def get_current_area(self):
        """Retourne la zone actuelle."""
        return self.current_area

    def get_available_events(self):
        """Retourne les événements disponibles dans la zone actuelle."""
        if self.current_area:
            return self.current_area.get("event_type", [])
        return []

    def is_area_safe(self):
        """Vérifie si la zone actuelle est sûre."""
        if self.current_area:
            return self.current_area.get("area_safe", False)
        return True

    def get_enemies_in_area(self):
        """Retourne les types d'ennemis dans la zone actuelle."""
        if self.current_area:
            return self.current_area.get("enemy_type", [])
        return []

    def _display_area_info(self):
        """Affiche les informations de la zone actuelle."""
        if not self.current_area:
            return
        
        print(f"Area Type: {self.current_area.get('area_type', 'Unknown')}")
        print(f"Safe Zone: {'Yes' if self.current_area.get('area_safe', False) else 'No'}")
        
        events = self.current_area.get("event_type", [])
        if events:
            print(f"Available Events: {', '.join(events)}")
        
        enemies = self.current_area.get("enemy_type")
        if enemies:
            print(f"Possible Enemies: {', '.join(enemies)}")

    def get_exploration_progress(self):
        """Retourne la progression de l'exploration."""
        return {
            "current_area": self.current_area.get("name") if self.current_area else None,
            "visited_areas": len(self.visited_areas),
            "areas_list": [area.get("name") for area in self.visited_areas]
        }
