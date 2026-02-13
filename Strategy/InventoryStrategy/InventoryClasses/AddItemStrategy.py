from ..InventoryStrategy import InventoryStrategy

class AddItemStrategy(InventoryStrategy):
    def execute_action(self, inventory, item):
        if "items" not in inventory:
            inventory["items"] = []
        
        inventory["items"].append(item)
        print(f"Item '{item.get('name', 'Unknown')}' added to inventory!")
        print(f"Total items: {len(inventory['items'])}")
        return True
    
    def get_strategy_name(self):
        return "Add Item"

