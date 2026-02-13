from ..Command import Command


class UseItemCommand(Command):
    """Commande pour utiliser un objet."""

    def __init__(self, user, item, inventory_strategy):
        self.user = user
        self.item = item
        self.inventory_strategy = inventory_strategy
        self.inventory = {"items": [item]} if item else {"items": []}
        self.user_pv_before = 0
        self.item_used = None

    def execute(self):
        """Utilise l'objet via la stratégie d'inventaire."""
        self.user_pv_before = self.user.get("pv", 0)
        self.item_used = self.inventory_strategy.execute_action(self.inventory, self.item)
        
        if self.item_used:
            effect = self.item_used.get("effect", None)
            value = self.item_used.get("value", 0)
            
            if effect == "heal":
                self.user["pv"] += value
                print(f"{self.user['name']} heals {value} HP!")
            elif effect == "damage":
                print(f"{self.user['name']} uses {self.item['name']}!")
        
        return self.item_used

    def undo(self):
        """Annule l'utilisation de l'objet."""
        if self.item_used:
            self.user["pv"] = self.user_pv_before
            self.inventory["items"].append(self.item_used)
            print(f"Item use undone! {self.item_used['name']} returned to inventory")

    def get_description(self):
        """Retourne une description de l'action."""
        return f"{self.user['name']} uses item: {self.item.get('name', 'Unknown')}"
